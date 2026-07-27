#!/usr/bin/env python
"""Chequeo de integridad del wiki — implementa CLAUDE.md S6.3 como checks automatizados.

Deriva su logica de la estructura REAL de este proyecto (moldes.md, erratas.md,
CLAUDE.md), no de un patron generico de wiki. Ver references/checks.md para el
razonamiento detras de cada chequeo.

Uso:
    python lint.py            # informe completo por stdout
    python lint.py --json     # mismo informe, como JSON (para tooling)

Exit code: 0 si no hay hallazgos ERROR, 1 si hay al menos uno (WARNING/INFO no afectan
al exit code -- son para revision humana, no bloquean nada).
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Localizacion del repo: sube desde este fichero hasta encontrar CLAUDE.md.
# Evita depender de cuantos niveles de carpeta tiene la skill.
# ---------------------------------------------------------------------------
def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "CLAUDE.md").is_file():
            return candidate
    raise SystemExit("No se encontro CLAUDE.md subiendo desde " + str(start))


REPO_ROOT = find_repo_root(Path(__file__).resolve())
WIKI = REPO_ROOT / "wiki"
CURSO = WIKI / "curso"
ERRATAS_MD = WIKI / "erratas.md"
MOLDES_MD = WIKI / "_estructura" / "moldes.md"

# "Documentos que NO son fichas" en wiki/curso/ (CLAUDE.md S4): sin frontmatter,
# no llevan molde. Se excluyen de los checks 3 y 5 (frontmatter, estado);
# SI cuentan para el check 2 (huerfanas) -- son paginas del wiki como cualquier otra.
NON_FICHA_DOCS = {"capa_decision", "mapa_tematico"}

# Alcance "vivo" del wiki: de aqui se leen los wikilinks para los checks 1 y 2.
# wiki/_provisional/ y wiki/_archivo/ quedan fuera a proposito -- CLAUDE.md las
# declara superadas/con moldes viejos, y _provisional en concreto documenta sus
# propios enlaces rotos con un "[HUECO]" o "no existe" explicito (piloto_friccion.md,
# balance_general.md): son traza historica, no bugs vivos. Meterlas en el chequeo
# solo produciria ruido sobre contenido que el propio proyecto ya dio por cerrado.
LIVE_SOURCE_FILES: list[Path] = (
    sorted(CURSO.glob("*.md"))
    + sorted((WIKI / "ejemplos").glob("*.md"))
    + sorted((WIKI / "_estructura").glob("*.md"))
    + [ERRATAS_MD, WIKI / "capturas_pendientes.md", REPO_ROOT / "index.md"]
)

# Universo de destinos validos para un wikilink: CUALQUIER .md bajo wiki/, para no
# marcar como "roto" un enlace que apunte a algo real en _provisional/_archivo.
ALL_WIKI_FILES = sorted(WIKI.rglob("*.md"))
VALID_TARGETS = {p.stem for p in ALL_WIKI_FILES}

VALID_ESTADOS = {"piloto", "borrador", "parcial", "completo"}
COMMON_FRONTMATTER_KEYS = ["concepto", "modulo", "molde", "estado", "fuentes", "enlaces"]

# Tal como los declara erratas.md SS10-25 (leido, no inventado). Un estado se
# considera valido si CONTIENE alguna de estas cadenas -- las variantes reales
# llevan sufijos libres ("DICTAMINADO - GRADIENTE COMPATIBLE", "DICTAMINADO -
# GANA LA VOZ"...) que no tiene sentido enumerar una a una.
VALID_ERRATA_STATE_MARKERS = [
    "PENDIENTE DE REVISIÓN HUMANA",
    "CANDIDATO A LAPSUS",
    "DICTAMINADO POR EVIDENCIA",
    "DICTAMINADO — VERIFICADO CONTRA EL AUDIO",
    "SIN DICTAMEN — TENSIÓN REGISTRADA",
    "NO ES ERRATA",
    "DICTAMINADO",  # el mas generico va al final; los de arriba ya lo contienen
]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
ERRATA_ID_RE = re.compile(r"\b(\d{2}-E\d+)\b")
ERRATA_ROW_RE = re.compile(r"^\|\s*\*\*(\d{2}-E\d+)\*\*[^|]*\|(.+)\|\s*$")
VIDEO_SOURCE_RE = re.compile(r"VIDEO-(\d+)")


@dataclass
class Finding:
    severity: str  # "ERROR" | "WARNING" | "INFO"
    check: str
    message: str
    location: str = ""


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)

    def add(self, severity: str, check: str, message: str, location: str = "") -> None:
        self.findings.append(Finding(severity, check, message, location))

    def by_severity(self, severity: str) -> list[Finding]:
        return [f for f in self.findings if f.severity == severity]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT)).replace("\\", "/")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Frontmatter simple linea='clave: valor', sin dependencia de PyYAML.
    Devuelve None si el fichero no abre con '---' (documentos sin molde)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


# ---------------------------------------------------------------------------
# Check 1 -- wikilinks rotos
# ---------------------------------------------------------------------------
def check_broken_wikilinks(report: Report) -> None:
    for path in LIVE_SOURCE_FILES:
        text = read(path)
        for lineno, line in enumerate(text.splitlines(), start=1):
            for match in WIKILINK_RE.finditer(line):
                target = match.group(1).strip()
                if not target:
                    continue  # ej. el "[[ ]]" de ejemplo en moldes.md, no es un link real
                if target not in VALID_TARGETS:
                    report.add(
                        "ERROR",
                        "wikilinks-rotos",
                        f"[[{target}]] no resuelve a ningun fichero de wiki/",
                        f"{rel(path)}:{lineno}",
                    )


# ---------------------------------------------------------------------------
# Check 2 -- fichas huerfanas en wiki/curso/
# ---------------------------------------------------------------------------
def check_orphan_fichas(report: Report) -> None:
    incoming: set[str] = set()
    for path in LIVE_SOURCE_FILES:
        text = read(path)
        source_stem = path.stem
        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            if target and target != source_stem:
                incoming.add(target)

    for path in sorted(CURSO.glob("*.md")):
        if path.stem not in incoming:
            report.add(
                "WARNING",
                "fichas-huerfanas",
                "Ninguna otra pagina del wiki enlaza a esta ficha con [[...]]",
                rel(path),
            )


# ---------------------------------------------------------------------------
# Check 3 -- consistencia de frontmatter contra el molde declarado
# Check 5 -- estados 'parcial'/'borrador' que no deberian quedar (corpus 19/19)
# ---------------------------------------------------------------------------
def check_frontmatter_and_estado(report: Report) -> None:
    for path in sorted(CURSO.glob("*.md")):
        if path.stem in NON_FICHA_DOCS:
            continue
        text = read(path)
        fm = parse_frontmatter(text)
        if fm is None:
            report.add(
                "ERROR",
                "frontmatter",
                "Ficha sin bloque de frontmatter ('---' inicial) -- CLAUDE.md S4 la exige en toda ficha de curso/",
                rel(path),
            )
            continue

        missing = [k for k in COMMON_FRONTMATTER_KEYS if k not in fm]
        if missing:
            report.add(
                "ERROR",
                "frontmatter",
                f"Faltan claves obligatorias (moldes.md, 'Frontmatter comun a los seis moldes'): {', '.join(missing)}",
                rel(path),
            )

        molde = fm.get("molde", "").strip()
        if molde and molde not in {"1", "2", "3", "4", "5", "6"}:
            report.add(
                "ERROR",
                "frontmatter",
                f"molde: {molde!r} no es uno de los seis moldes vigentes (1-6)",
                rel(path),
            )
        if molde == "5" and "variante" not in fm:
            report.add(
                "ERROR",
                "frontmatter",
                "molde: 5 exige 'variante' (FILTRO/SCORING/REGLAS) -- moldes.md SMOLDE 5, campo 1",
                rel(path),
            )

        modulo = fm.get("modulo", "")
        if modulo and not re.fullmatch(r"\d{2}", modulo.strip("\"'")):
            report.add(
                "WARNING",
                "frontmatter",
                f"modulo: {modulo!r} no tiene forma 'NN' con cero a la izquierda",
                rel(path),
            )

        estado = fm.get("estado", "").strip()
        if estado and estado not in VALID_ESTADOS:
            report.add(
                "ERROR",
                "frontmatter",
                f"estado: {estado!r} no es uno de los valores validos ({', '.join(sorted(VALID_ESTADOS))})",
                rel(path),
            )
        elif estado in {"parcial", "borrador"}:
            report.add(
                "WARNING",
                "estado-abierto",
                f"estado: {estado} -- el corpus esta cerrado (19/19 videos ingeridos); "
                "verificar si sigue siendo intencional o es un resto sin actualizar",
                rel(path),
            )


# ---------------------------------------------------------------------------
# Check 4 -- estados invalidos en erratas.md
# ---------------------------------------------------------------------------
def iter_errata_rows(text: str):
    """Genera (id, tipo_cell, estado_cell, lineno) para cada fila de errata."""
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = ERRATA_ROW_RE.match(line)
        if not m:
            continue
        errata_id = m.group(1)
        rest = m.group(2)
        cells = [c.strip() for c in rest.split("|")]
        if len(cells) < 2:
            continue
        tipo_cell = cells[0]
        estado_cell = cells[-1]
        yield errata_id, tipo_cell, estado_cell, lineno


def check_errata_states(report: Report) -> None:
    text = read(ERRATAS_MD)
    for errata_id, _tipo, estado_cell, lineno in iter_errata_rows(text):
        if not any(marker in estado_cell for marker in VALID_ERRATA_STATE_MARKERS):
            report.add(
                "ERROR",
                "estados-erratas",
                f"{errata_id}: estado {estado_cell!r} no usa ninguno de los vocablos "
                "declarados en erratas.md SSestados",
                f"{rel(ERRATAS_MD)}:{lineno}",
            )


# ---------------------------------------------------------------------------
# Check 6 -- el recuento agregado de erratas.md cuadra con las filas reales
# (este es el chequeo que habria detectado el desfase 32-vs-33 de la sesion
#  anterior antes de que hiciera falta contarlo a mano)
# ---------------------------------------------------------------------------
def check_errata_recount(report: Report) -> None:
    text = read(ERRATAS_MD)

    real_total = 0
    real_dictaminadas = 0
    real_by_type: dict[str, int] = {"T1": 0, "T2": 0, "T3": 0, "T4": 0}

    for errata_id, tipo_cell, estado_cell, lineno in iter_errata_rows(text):
        if "NO ES ERRATA" in estado_cell:
            continue  # sacada del recuento, por regla del propio proyecto
        real_total += 1
        if "SIN DICTAMEN" not in estado_cell:
            real_dictaminadas += 1

        type_match = re.search(r"T([1-4])", tipo_cell)
        if type_match:
            real_by_type[f"T{type_match.group(1)}"] += 1
        else:
            report.add(
                "WARNING",
                "recuento-erratas",
                f"{errata_id}: no se pudo determinar el tipo primario (T1-T4) desde la celda {tipo_cell!r}",
                f"{rel(ERRATAS_MD)}:{lineno}",
            )

    declared_by_type: dict[str, tuple[int, int]] = {}
    declared_total: tuple[int, int] | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = re.match(r"^\|\s*\*\*T([1-4])\*\*.*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*$", line)
        if m:
            declared_by_type[f"T{m.group(1)}"] = (int(m.group(2)), int(m.group(3)))
            continue
        m = re.match(r"^\|\s*\*\*TOTAL\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*$", line)
        if m:
            declared_total = (int(m.group(1)), int(m.group(2)))

    if declared_total is None:
        report.add(
            "WARNING",
            "recuento-erratas",
            "No se encontro la fila '**TOTAL**' de la tabla de Recuento -- revisar formato manualmente",
            rel(ERRATAS_MD),
        )
    else:
        decl_n, decl_d = declared_total
        if decl_n != real_total:
            report.add(
                "ERROR",
                "recuento-erratas",
                f"Tabla de Recuento dice TOTAL={decl_n}, pero hay {real_total} filas activas "
                "(sin contar las 'NO ES ERRATA') en las tablas de modulo",
                rel(ERRATAS_MD),
            )
        if decl_d != real_dictaminadas:
            report.add(
                "ERROR",
                "recuento-erratas",
                f"Tabla de Recuento dice Dictaminadas={decl_d}, pero {real_dictaminadas} filas "
                "activas no contienen 'SIN DICTAMEN'",
                rel(ERRATAS_MD),
            )

    for tipo, real_n in real_by_type.items():
        decl = declared_by_type.get(tipo)
        if decl is None:
            continue
        decl_n, _decl_d = decl
        if decl_n != real_n:
            report.add(
                "ERROR",
                "recuento-erratas",
                f"Tabla de Recuento dice {tipo}={decl_n}, pero se contaron {real_n} filas de tipo {tipo}",
                rel(ERRATAS_MD),
            )


# ---------------------------------------------------------------------------
# Check 7 -- IDs de errata citados en fichas/ejemplos que no existen como fila
#            en erratas.md (referencia colgando), y a la inversa (informativo)
# ---------------------------------------------------------------------------
def check_errata_id_crossref(report: Report) -> None:
    errata_text = read(ERRATAS_MD)
    indexed_ids = {eid for eid, _, _, _ in iter_errata_rows(errata_text)}

    cited_ids: dict[str, list[str]] = {}
    citing_files = sorted(CURSO.glob("*.md")) + sorted((WIKI / "ejemplos").glob("*.md"))
    for path in citing_files:
        text = read(path)
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in ERRATA_ID_RE.finditer(line):
                eid = m.group(1)
                cited_ids.setdefault(eid, []).append(f"{rel(path)}:{lineno}")

    for eid, locations in cited_ids.items():
        if eid not in indexed_ids:
            report.add(
                "ERROR",
                "erratas-huerfanas",
                f"{eid} se cita en fichas pero no existe como fila en erratas.md",
                locations[0],
            )

    uncited = sorted(indexed_ids - cited_ids.keys())
    if uncited:
        report.add(
            "INFO",
            "erratas-huerfanas",
            f"{len(uncited)} erratas indexadas en erratas.md que ninguna ficha ni ejemplo cita "
            f"por numero: {', '.join(uncited)} -- puede ser normal (viven solo en su tabla de modulo)",
            rel(ERRATAS_MD),
        )


# ---------------------------------------------------------------------------
# Check 8 -- fichas que citan >1 video en 'fuentes' sin llevar transversal:true
# (moldes.md: transversal = "si el concepto se alimenta de varios modulos".
#  Adivinar la intencion no es tarea del script -- se reporta como INFO para
#  que una persona (o Claude leyendo la ficha) decida si es D-76 (enriquecimiento
#  legitimo sin ser 'transversal') o un flag que faltaba.)
# ---------------------------------------------------------------------------
def check_transversal_consistency(report: Report) -> None:
    for path in sorted(CURSO.glob("*.md")):
        if path.stem in NON_FICHA_DOCS:
            continue
        fm = parse_frontmatter(read(path))
        if not fm:
            continue
        fuentes = fm.get("fuentes", "")
        videos = set(VIDEO_SOURCE_RE.findall(fuentes))
        is_transversal = fm.get("transversal", "").strip().lower() == "true"
        if len(videos) > 1 and not is_transversal:
            report.add(
                "INFO",
                "transversal",
                f"cita {len(videos)} videos distintos en 'fuentes' ({sorted(videos)}) sin "
                "'transversal: true' -- revisar si es enriquecimiento D-76 (normal) o un flag que falta",
                rel(path),
            )


CHECKS = [
    ("1. Wikilinks rotos", check_broken_wikilinks),
    ("2. Fichas huerfanas en wiki/curso/", check_orphan_fichas),
    ("3+5. Frontmatter y estado (molde, estado, corpus cerrado)", check_frontmatter_and_estado),
    ("4. Estados invalidos en erratas.md", check_errata_states),
    ("6. Recuento de erratas.md desincronizado", check_errata_recount),
    ("7. Cruce de IDs de errata (ficha <-> erratas.md)", check_errata_id_crossref),
    ("8. Fichas multi-video sin 'transversal: true'", check_transversal_consistency),
]


def run() -> Report:
    report = Report()
    for _label, fn in CHECKS:
        fn(report)
    return report


def print_text_report(report: Report) -> None:
    order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    findings = sorted(report.findings, key=lambda f: (order[f.severity], f.check, f.location))

    print(f"Lint del cerebro de analisis fundamental -- {REPO_ROOT.name}")
    print("=" * 70)
    if not findings:
        print("Sin hallazgos. Todos los checks pasaron limpio.")
        return

    current_check = None
    for f in findings:
        if f.check != current_check:
            current_check = f.check
            print(f"\n-- {f.check} --")
        loc = f" ({f.location})" if f.location else ""
        print(f"[{f.severity}] {f.message}{loc}")

    n_err = len(report.by_severity("ERROR"))
    n_warn = len(report.by_severity("WARNING"))
    n_info = len(report.by_severity("INFO"))
    print("\n" + "=" * 70)
    print(f"Total: {n_err} ERROR, {n_warn} WARNING, {n_info} INFO")


def print_json_report(report: Report) -> None:
    payload = [
        {"severity": f.severity, "check": f.check, "message": f.message, "location": f.location}
        for f in report.findings
    ]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main(argv: list[str]) -> int:
    report = run()
    if "--json" in argv:
        print_json_report(report)
    else:
        print_text_report(report)
    return 1 if report.by_severity("ERROR") else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
