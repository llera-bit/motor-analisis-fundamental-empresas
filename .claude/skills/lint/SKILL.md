---
name: lint
description: Chequeo automatizado de integridad del wiki del cerebro de análisis fundamental (enlaces [[wikilink]] rotos, fichas huérfanas, frontmatter inconsistente con el molde declarado, estados inválidos en erratas.md, recuento de erratas desincronizado). Usar cuando el usuario pida verificar la integridad del wiki, buscar enlaces rotos, páginas huérfanas, o hacer un chequeo de salud del cerebro — incluye la pasada de lint que CLAUDE.md §6.3 pide hacer periódicamente.
---

# Lint del cerebro de análisis fundamental

Convierte en chequeos deterministas el protocolo que `CLAUDE.md` §6.3 describe en prosa
(«buscar: contradicciones entre fichas · claims obsoletos · páginas huérfanas · conceptos
mencionados sin ficha propia · cross-references ausentes»). No sustituye una lectura humana —
la mayoría de esos puntos exigen juicio— pero automatiza la parte que **sí** es mecánica:
¿resuelve cada enlace? ¿tiene cada ficha lo que su molde exige? ¿el recuento de erratas
cuadra con las filas reales?

## Cuándo usar esta skill

Cuando el usuario pida:
- Verificar la integridad del wiki, o un «chequeo de salud del cerebro»
- Buscar enlaces `[[...]]` rotos
- Buscar páginas huérfanas
- Hacer la pasada de lint periódica de `CLAUDE.md` §6.3
- Verificar que el frontmatter de las fichas está bien, o que `erratas.md` está consistente

## Cómo ejecutarla

```bash
python .claude/skills/lint/scripts/lint.py
```

Funciona desde cualquier directorio de trabajo — localiza la raíz del repo subiendo desde su
propia ubicación hasta encontrar `CLAUDE.md`. Con `--json` en vez de texto:

```bash
python .claude/skills/lint/scripts/lint.py --json
```

**Exit code:** `0` si no hay hallazgos `ERROR` (los `WARNING`/`INFO` no lo afectan — son para
criterio humano, no bloquean nada). Sin dependencias externas: solo la librería estándar de
Python 3.

## Los ocho chequeos

| # | Qué mira | Severidad si falla |
|---|---|---|
| 1 | Todo `[[wikilink]]` usado en el wiki resuelve a un fichero real | `ERROR` |
| 2 | Toda ficha de `wiki/curso/` recibe al menos un enlace entrante desde otra página del wiki | `WARNING` |
| 3 | El frontmatter de cada ficha tiene las claves que `moldes.md` exige (y `variante` si `molde: 5`) | `ERROR` |
| 4 | Cada entrada de `erratas.md` usa uno de los estados que el propio archivo declara válidos | `ERROR` |
| 5 | Ninguna ficha queda `estado: parcial` o `borrador` (el corpus está cerrado, 19/19 vídeos) | `WARNING` |
| 6 | La tabla «Recuento» de `erratas.md` (por tipo T1-T4 y total) cuadra con las filas reales | `ERROR` |
| 7 | Todo `NN-EXX` citado en una ficha existe como fila en `erratas.md`, y viceversa | `ERROR` / `INFO` |
| 8 | Fichas que citan más de un vídeo en `fuentes:` sin llevar `transversal: true` | `INFO` |

**Por qué estos ocho y no otros:** derivados leyendo la estructura real del proyecto, no de un
patrón de wiki genérico. El razonamiento completo de cada uno —qué cuenta como «ficha»,
por qué `wiki/_provisional/` y `wiki/_archivo/` quedan fuera del barrido, por qué el 6 y el 7 no
estaban en el encargo original— está en `references/checks.md`. Léelo antes de tocar el script:
explica también qué haría falta ajustar si el proyecto cambia de convención (nuevo molde, nuevo
estado de errata, etc.).

## Qué NO hace

- No corrige nada. Solo reporta — la corrección sigue siendo una decisión humana (`CLAUDE.md`
  RD-4: un hueco visible vale más que un relleno plausible, y eso aplica también a los hallazgos
  del lint).
- No detecta «contradicciones entre fichas» ni «claims obsoletos» en el sentido de `CLAUDE.md`
  §6.3 — eso exige leer y comparar significado, no forma. Sigue siendo trabajo de una sesión de
  lint con criterio, como las que ya se han hecho a mano en este proyecto.
- No toca `wiki/_provisional/` ni `wiki/_archivo/` como fuente de hallazgos: son contenido
  superado a propósito, con sus propios enlaces rotos ya documentados como parte de su traza
  histórica. Meterlos en el barrido produciría ruido sobre algo que el proyecto ya dio por
  cerrado — ver `references/checks.md` para el caso concreto que lo motivó.

## Interpretar los hallazgos

- **`ERROR`** — algo que el propio proyecto define como inválido (un enlace que no resuelve, un
  estado que no existe en el vocabulario declarado, un recuento que no suma). Merece dictamen.
- **`WARNING`** — algo que podría ser intencional pero normalmente no lo es (una ficha sin
  ningún enlace entrante, un estado `parcial` en un corpus cerrado).
- **`INFO`** — una observación que necesita criterio humano para saber si es un problema (una
  ficha que cita varios vídeos sin `transversal: true` podría ser un enriquecimiento D-76
  legítimo, no un error).
