# log.md — Histórico del proyecto

> **APPEND-ONLY.** Nunca se edita ni se borra nada de lo ya escrito.
> Las decisiones no se modifican: se supersede con una nueva entrada.
> Para ver el estado vigente de cada decisión, consultar `decisiones.md`.

Formato de entrada: `## [YYYY-MM-DD] tipo | título`

---

## [2026-07-11] traspaso | Consolidación de decisiones D-01 a D-28 desde la fase de diseño en chat

Las decisiones siguientes se tomaron en conversación con Claude (chat) durante la fase de
diseño previa a la existencia de este repositorio. Se consolidan aquí como punto de partida.

---

### D-01 · Metodología antes que arquitectura
**Estado:** RATIFICADA
- **Decisión:** derivar los requisitos de datos del método del experto antes de diseñar arquitectura.
- **Alternativas:** seguir con diseño arquitectónico abstracto en paralelo.
- **Motivos:** no se puede dimensionar una capa de datos sin saber qué se calcula y con qué.
- **Consecuencias:** el catálogo del método es prerrequisito de todo lo demás.

### D-02 · Plantilla de dos capas
**Estado:** RATIFICADA
- **Decisión:** Ficha de Concepto (cualitativa/estructural) + Inventario de Datos Atómicos (plano).
- **Alternativas:** plantilla única de una columna ("dato necesario").
- **Motivos:** el análisis de redundancia exige inputs aplanados.
- **Consecuencias:** dos artefactos a mantener.

### D-03 · Separación Fase A (transcripción) / Fase B (crítica)
**Estado:** RATIFICADA — *matizada por D-04*
- **Decisión:** Fase A cataloga sin podar; Fase B analiza huecos y redundancias.
- **Motivos:** preservar trazabilidad "curso vs. nosotros".
- **Consecuencias:** la poda de métricas se pospone hasta poder testar empíricamente.

### D-04 · Capa de errata y estado epistémico en la ficha
**Estado:** RATIFICADA
- **Decisión:** añadir campos `Errata/Inconsistencias` y `Estado epistémico`.
- **Motivos:** la fuente contiene errores objetivos. Transcribir "fielmente" un error sería
  propagarlo; corregirlo en silencio destruiría la trazabilidad.
- **Consecuencias:** la Fase A deja de ser transcripción pura → **transcripción + auditoría**.

### D-05 · Las notas personales no son insumo del inventario atómico
**Estado:** RATIFICADA — *ampliada por D-24*
- **Motivos:** la compresión manual pierde partidas atómicas e introduce ruido
  (constatado: inversión EV/Market Cap en las notas del módulo 6).

### D-06 · Hallazgo: TIKR es el proveedor de datos del experto
**Estado:** REGISTRO (no requiere decisión)
- Identificado en las capturas de pantalla del PDF del módulo 6.

### D-07 · Adoptar el patrón LLM Wiki (Karpathy) como contenedor
**Estado:** RATIFICADA
- **Decisión:** el cerebro se instancia como wiki de markdown (raw inmutable / páginas
  generadas / schema / index / log), con la Ficha de Concepto como formato de página.
- **Alternativas:** (a) documentos sueltos; (b) RAG puro sobre los PDFs.
- **Motivos:** (a) no escala ni mantiene coherencia entre módulos; (b) el RAG **no acumula** —
  redescubre en cada consulta y no detecta contradicciones entre módulos.
- **Consecuencias:** el Decision Log pasa a ser `log.md`; hace falta `index.md` y un schema.
  El Inventario Atómico queda **fuera** del wiki, como tabla derivada.

### D-08 · Frontera dura cerebro / embudo
**Estado:** RATIFICADA
- **Decisión:** el cerebro almacena metodología, juicio y priors. Los umbrales operativos
  **no se adoptan del cerebro**; se derivan de evidencia. El cerebro registra el *rango
  plausible y su justificación*, no el valor de producción.
- **Motivos:** adoptar por autoridad viola el principio de tres pilares. Un umbral verbalizado
  en un vídeo tiene alta probabilidad de estar sobreajustado a la experiencia del experto.
- **Consecuencias:** **reduce la criticidad de la pasada de vídeo** — deja de ser fuente de
  parámetros y pasa a ser fuente de *priors*.

### D-09 · Clases de procedencia ampliadas
**Estado:** RATIFICADA
- `[PDF]` · `[VÍDEO]` · `[INFERIDO]` · `[CORREGIDO]` · `[COMPLETADO-EST]` · `[JUICIO-CLAUDE]` · `[HUECO]`
- `[COMPLETADO-EST]` exige justificación por tres pilares.

### D-10 · Arquitectura escalonada B → A
**Estado:** RATIFICADA
- **Decisión:** construir primero el **cerebro-copiloto** (analiza una empresa dada aplicando
  la metodología del experto). **Diferir** la decisión sobre el embudo cuantitativo hasta
  tener el Inventario Atómico completo.
- **Alternativas:** (a) ir directo al embudo; (b) quedarse solo en copiloto para siempre.
- **Motivos:** el Inventario Atómico es prerrequisito del embudo y **solo puede derivarse del
  cerebro** → no existe camino a A que no pase por B. Además B entrega valor desde el primer
  módulo, no necesita umbrales duros ni proveedor caro, y no puede sufrir look-ahead bias.
- **Consecuencias:** el **Project Vision v1.0 queda parcialmente en revisión**. Sobreviven las
  dos reglas duras (RD-1, RD-2). El embudo, la watchlist y la frontera del output pasan a
  estado *"pendiente de reevaluación tras la captura"*. La cuestión abierta del alcance
  geográfico **deja de ser bloqueante** (B funciona empresa a empresa).

### D-11 · Separación física curso / complemento
**Estado:** RATIFICADA
- **Decisión:** dos namespaces. `complemento/` enlaza a `curso/` pero nunca lo modifica.
- **Prueba de auditabilidad:** borrar `complemento/` debe devolver el curso íntegro.

### D-12 · Alcance = Módulo 3 completo (19 vídeos), incluido el 19
**Estado:** RATIFICADA
- Trading y módulo 1 (introducción) fuera. Macro fuera **como módulo**, pero los
  condicionantes macro de reglas fundamentales se capturan *in situ* donde aparezcan.
- **Matiz:** el vídeo 19 ("Cuándo acumular, mantener o vender") **no es trading**: es política
  de venta y gestión de posición. Parte del método fundamental. **Dentro del alcance.**

### D-13 · Hallazgo: los vídeos 13–19 carecen de PDF
**Estado:** REGISTRO
- Contienen la **función de decisión** del método (multibagger, riesgo, cuándo vender).
- La hipótesis "el PDF lo contiene todo" queda **refutada por construcción** para esa mitad.

### D-14 · Reformulación de la Regla Dura 1
**Estado:** RATIFICADA → es **RD-1** en `CLAUDE.md`
- **Decisión:** separar capa numérica (fuente estructurada obligatoria: XBRL/proveedor) de
  capa narrativa (LLM lee el documento oficial, con cita). Los filings **sí** son insumo del
  cerebro en ejecución, pero **solo por su narrativa**.
- **Motivos:** los números del 10-K ya existen en XBRL vía EDGAR; no hay razón para arriesgar
  transcripción por LLM (error silencioso). La narrativa solo la puede procesar un LLM.
- **Consecuencias:** la arquitectura de ejecución tiene **dos entradas por empresa**.

### D-15 · Hallazgo: benchmark sectorial (Damodaran) como componente del método
**Estado:** PROPUESTA — **HIPÓTESIS FUERTE, pendiente de confirmar en el vídeo 16**
- El archivo "16" que el usuario catalogó como "enlace de interés" es la página de datos
  sectoriales de Damodaran (NYU Stern), y está junto al vídeo *"La realidad de los múltiplos"*.
  Encaja con la insistencia del experto en comparar con la media del sector (módulo 6).
- **Hipótesis:** el experto **no usa umbrales absolutos, sino benchmarks relativos al sector**.
- **Si se confirma:** el "problema de los umbrales" queda en gran parte disuelto. El umbral es
  una **función**, no una constante. Procedencia = `[CURSO]`, no `[COMPLETADO-EST]`.
- **Limitación conocida:** Damodaran actualiza una vez al año (enero). Sin histórico
  point-in-time → restricción para una eventual Arquitectura A.
- **Primera pregunta a verificar al llegar al vídeo 16.**

### D-16 · Tratamiento de erratas
**Estado:** RATIFICADA
- Cuerpo de la ficha = solo versión correcta. Bloque `## Errata de la fuente` al final.
  `erratas.md` centralizado como índice, cuya función es medir la **tasa de error de la fuente**.

### D-17 · Transcripción Whisper para vídeos 13–19
**Estado:** ⚠️ **SUPERSEDIDA por D-23**

### D-18 · Gobernanza de decisiones tipo ADR
**Estado:** RATIFICADA
- `log.md` append-only e inmutable. Estados: PROPUESTA / RATIFICADA / SUPERSEDIDA / DEROGADA.
- Índice derivado `decisiones.md` con el estado vigente.
- **Motivo:** un log que se reescribe es un log que miente.

### D-19 · Desfase de numeración interna de las diapositivas
**Estado:** PENDIENTE DE VERIFICACIÓN
- La numeración vídeo↔archivo del usuario **es fiable**. Pero la cabecera *dentro* de los PDFs
  muestra otro número: vídeo 6 → slide "4."; vídeo 10 → slide "8." (desfase −2 consistente).
- **Hipótesis (especulativa):** los PDFs proceden de una edición anterior del curso, a la que
  luego se añadieron 2 vídeos al inicio.
- **Implicación:** los PDFs podrían estar **desactualizados respecto a los vídeos**.
  Ante conflicto, **el vídeo manda**. Se confirmará o caerá con la primera transcripción.

### D-20 · La Ficha necesita DOS perfiles, no uno
**Estado:** RATIFICADA
- Perfil *cuantitativo* (deuda, ROIC, FCF, múltiplos) y perfil *cualitativo* (moat, equipo
  directivo, cuándo vender), con campos parcialmente distintos.
- Los **ejemplares son conocimiento de primera clase** en el perfil cualitativo.
- **Alternativa descartada:** plantilla única (aplasta el juicio en campos numéricos vacíos).

### D-21 · Sesgo de supervivencia en los ejemplares — mitigación obligatoria
**Estado:** RATIFICADA
- El curso enseña el moat **solo con ganadores** (ASML, Ferrari, Coca-Cola, Apple, Meta, Zara,
  Salesforce). Ningún caso de moat erosionado.
- **Toda ficha cualitativa debe incluir `Contraejemplos`**, construidos en `complemento/`
  (Nokia, Kodak, Intel, Sears…), con tres pilares.
- **Motivo:** sin casos negativos, el cerebro no puede discriminar. Riesgo de calidad más grave
  detectado hasta la fecha.

### D-22 · Hallazgo: el puente cualitativo→cuantitativo ya está latente en el material
**Estado:** REGISTRO
- El experto define el moat **por su efecto** (*pricing power*, beneficios futuros
  persistentes), no por su forma. Eso tiene **huella financiera medible**: margen bruto
  sostenido, ROIC persistentemente alto que no revierte a la media.
- **Consecuencia:** el Inventario Atómico puede alimentarse **también desde las fichas
  cualitativas**, cosa no prevista inicialmente.

### D-23 · Transcripción Whisper de los 19 vídeos — SUPERSEDE a D-17
**Estado:** RATIFICADA
- **Decisión:** transcribir **los 19**, no solo 13–19. Con **timestamps** (`.srt`).
- **Motivos:** la transcripción domina a las notas manuales en las tres dimensiones
  (completitud, fidelidad, coste humano). El PDF cubre solo lo definicional; el juicio
  operativo está en la voz. Los timestamps extienden RD-2 (grounding) a la fuente-vídeo.
- **Consecuencias:** **reduce** la carga de trabajo humana, no la aumenta.

### D-24 · El documento manual del usuario deja de ser insumo del cerebro
**Estado:** RATIFICADA
- **Decisión:** las fuentes canónicas son **PDF + transcripción**. Las notas del usuario pasan
  a un rol distinto: **dudas, desacuerdos y contradicciones detectadas**, en crudo, archivadas
  en `raw/notas/` y filadas por el LLM en `complemento/`. Nunca en `curso/`.
- **Motivos:** evidencia empírica de pérdida y deformación; y sobre todo **sesgo de selección**
  — un resumen humano descarta comentarios de pasada ("esto en bancos no aplica") que suelen
  ser los de mayor valor metodológico. La transcripción los conserva **porque no decide**.
- **Consecuencias:** el usuario sigue viendo los vídeos **para aprender**, no para transcribir.

### D-25 · Secuencia del piloto: ficha primero, plantilla después
**Estado:** RATIFICADA
- **Decisión:** transcripción del vídeo 06 → **ficha real completa** → **inducir la plantilla**.
  No al revés.
- **Motivos:** una plantilla diseñada contra material incompleto queda mal calibrada, porque no
  sabemos aún qué campos exige el contenido del vídeo. (Corrección de un error de secuencia
  cometido por Claude.)
- **Consecuencias:** la plantilla de `CLAUDE.md` §4 es **PROVISIONAL**.

### D-26 · Claude Code como entorno de construcción y mantenimiento
**Estado:** RATIFICADA
- **Alternativas:** seguir en chat (**inviable**: sin sistema de archivos no hay ingest, lint
  ni persistencia); otros agentes de código.
- **Motivos:** el patrón exige acceso a disco. Además resuelve Whisper y la lectura de PDFs
  en local. `CLAUDE.md` **ES** la capa schema de Karpathy.
- **Consecuencias:** riesgo de corrupción de `curso/` → guardarraíles RD-3 + git.

### D-27 · Obsidian como capa de lectura humana, no como dependencia
**Estado:** RATIFICADA
- El wiki debe seguir siendo markdown portable. Sin plugins que rompan la portabilidad.
- **Hipótesis a explorar:** el Inventario Atómico podría implementarse como **query de
  Dataview** sobre el frontmatter, en lugar de como artefacto mantenido a mano.

### D-28 · Política de modelos
**Estado:** RATIFICADA
- Sonnet para ingesta. Opus (esfuerzo alto) para diseño, lint y `[COMPLETADO-EST]`.
- **Regla: Sonnet para escribir, Opus para pensar y auditar.**

---

## Erratas ya confirmadas en la fuente (antes de la ingesta formal)

Detectadas en el PDF del módulo 06 y del módulo 10. **Deben aparecer en `erratas.md` y en las
fichas correspondientes cuando se ingesten.**

**Módulo 06 — Deuda y Caja**
1. **`EV = Market Cap − Net Debt` es FALSO.** La correcta es `EV = Market Cap + Deuda Neta`
   (+ minoritarios, preferentes). *Evidencia: los propios datos del curso.*
   AMD: 141.426 + (−2.811) = 138.615 ✓ (la fórmula del PDF daría 144.237 ✗).
   Intel: 82.546 + 27.796 ≈ 110.342 vs EV reportado 116.104 → **faltan ~5.762M**, probablemente
   minoritarios/preferentes → *el puente completo del EV es un `[HUECO]` a resolver.*
2. **Definición verbal contradice su propia fórmula:** el texto dice "restarle *a la caja* la
   suma de las deudas" (Caja − Deuda) pero el recuadro dice `Deuda Financiera Total − Caja`.
   La correcta es la del recuadro.
3. Error de rotulación: el panel derecho de la última diapositiva es **Intel**, no AMD.
4. Las cajas de decisión (`MC < EV → tiene deuda`) **son correctas**, pero son lógicamente
   incompatibles con la fórmula errónea del punto 1. *El experto tiene la intuición bien y la
   formalización mal.*

**Módulo 10 — El Moat**
1. La cabecera de la taxonomía dice "ventajas en términos de **aumento de ingresos**" pero
   incluye **BAJOS COSTES**, que es una ventaja de coste. Inconsistencia interna.
2. **"Ser un monopolio" listado como fuente de moat es un error de categoría.** El monopolio
   es el *resultado* de un moat, no su causa.

---

## Huecos ya identificados (pendientes de vídeo o de `complemento/`)

**Módulo 06:**
- Definición operativa de "Deuda Financiera Total" — ¿incluye *operating leases* (IFRS 16 / ASC 842)?
- Perímetro exacto de la Caja — ¿entran *long-term investments*? ¿caja atrapada en filiales?
- Puente completo del EV (minoritarios, preferentes) — **crítico**: si el sistema calcula el EV
  por su cuenta, no coincidirá con el del proveedor. Hay que decidir la fuente canónica.
- Umbral / referencia de `Net Debt / EBITDA` — el ratio aparece **resaltado** en las capturas de
  TIKR (AMD −0,52x en verde / Intel 3,58x en rojo) pero **no se menciona en el texto**. Es la
  única heurística cuantitativa recuperable, y solo por inferencia visual. → `[INFERIDO]`
- Ratios de apalancamiento: el PDF los anuncia en plural y **no los enumera**. Ausentes:
  cobertura de intereses, Deuda/Equity, Deuda Neta/FCF, calendario de vencimientos, coste medio
  de la deuda, % a tipo variable.
- Aplicabilidad sectorial: la deuda neta **carece de sentido en bancos y aseguradoras**. No se
  menciona. → regla de exclusión obligatoria.
- Naturaleza temporal: market cap es intradía; deuda neta es foto de balance con hasta 90 días
  de retraso. Mezclarlas sin control genera look-ahead bias.

**Módulo 10:**
- **Procedimiento de detección** — nada sobre *cómo saber* si una empresa tiene moat.
- **Prueba de falsación** — ¿cómo distinguir una marca fuerte de una que *fue* fuerte?
- **Durabilidad / erosión** — no hay "tendencia del moat". Un moat sin durabilidad es una foto.
- **Gradación** — ¿ancho / estrecho / inexistente? Todo es binario en el PDF.
- **Conexión con los números** — cero, pese a que la taxonomía la implica (ver D-22).
- **Contraejemplos** — ninguno. Ver D-21.

---

## [2026-07-12] ingesta-cero | Protocolo 6.0 ejecutado: normalización del material del Módulo 3

Ejecutada la Ingesta cero (protocolo 6.0) sobre los **19 vídeos + 12 PDF de slides** del
Módulo 3, previa propuesta de tabla de correspondencias y **confirmación explícita del
usuario**. Renombrado a la convención `NN_slug`. Tabla completa de nombres originales en
`fuentes.md` (RD-2, preservación de procedencia).

**Dos desviaciones respecto al supuesto de partida (registradas para trazabilidad):**
1. El material **no estaba en `raw/_inbox/`** (vacío): llegó ya repartido en `raw/video/` y
   `raw/pdf/`, con nombres originales. Se renombró *in situ*.
2. Los vídeos son **`.mkv`, no `.mp4`** (como asumían los ejemplos de CLAUDE.md/fuentes.md).
   Se preserva la extensión real: `raw/` es inmutable, no se transcodifica. Corregido el
   ejemplo en `fuentes.md`. *(Pendiente: mismos ejemplos `.mp4` en CLAUDE.md §2/§6.1; CLAUDE.md
   es capa schema y no se toca sin OK explícito.)*

**Dos artefactos que NO son diapositivas → `raw/externo/` (decisión del usuario):**
- `16.txt` (enlace Damodaran) → `raw/externo/16_damodaran_enlace.txt`.
- `14. Multiples_por_Sector_ABREVIADO.pdf` → `raw/externo/14_multiplos_por_sector_abreviado.pdf`
  (**opción b**). Razón del usuario: CLAUDE.md §2 ya define `raw/externo/` como "Damodaran,
  tablas sectoriales, etc.", y esto **es** una tabla sectorial; `raw/pdf/` es para diapositivas
  de vídeo, y esto no lo es. Nombrarlo como slides del vídeo 14 (opción a) mentiría sobre el
  contenido.

**`.gitignore`:** `raw/video/` → `raw/video/*` + excepción `!raw/video/.gitkeep`, para que la
carpeta de vídeos sobreviva a un clon aunque su contenido (`.mkv`) siga ignorado. Verificado:
`.gitkeep` trackeado, cero `.mkv/.mp4` en el índice.

---

### Hallazgo · Refuerzo de D-15 (benchmark sectorial vs. umbral absoluto)

De los **tres** artefactos del Módulo 3 que **no** son diapositivas, **dos** son referencias
sectoriales —la tabla del vídeo 14 y el enlace de Damodaran del vídeo 16— y **ambos caen justo
en los vídeos donde el experto pasa de *definir* múltiplos a *usarlos*** (vídeo 14 "¿Cuándo
Usarlos?", vídeo 16 "La Realidad de los Múltiplos"). Sumado a su insistencia en "comparar con
la media del sector" (módulo 6), la evidencia estructural eleva D-15 de **"hipótesis fuerte"**
a **"hipótesis muy probable"**: el experto usa **benchmarks relativos al sector, no umbrales
absolutos**.

**Estado de D-15: sigue PROPUESTA, pendiente de confirmación en el vídeo 16** (no se cambia el
estado en `decisiones.md`). Lo que cambia es la fuerza del prior, no el veredicto.

---

## [2026-07-12] transcripcion-piloto | Vídeo 06 transcrito; medición y decisión de modelo del lote

Ejecutado el protocolo 6.1 sobre el vídeo 06 (piloto). Objetivo doble: producir la primera
transcripción canónica **y medir** para decidir el tamaño de modelo del lote de 19 — no elegir
por intuición. Se transcribió **dos veces** (medium y large-v3) para comparar.

### Entorno (reproducible)
- Windows 11 · CPU 16 hilos · **sin GPU** (transcripción en CPU).
- Python 3.14.0 en venv aislado `.venv-whisper/` (gitignored). Las wheels de cp314 ya existían;
  no hizo falta el fallback a Python 3.12.
- `faster-whisper` 1.2.1 · `ctranslate2` 4.8.1 · `av` 18.0.0 · `onnxruntime` 1.27.0 · `numpy` 2.5.1.
- `ffmpeg` 8.1.2 (Gyan build, vía `winget install Gyan.FFmpeg`).
- Modelos CTranslate2: `Systran/faster-whisper-medium`, `Systran/faster-whisper-large-v3`.

### Extracción de audio
`ffmpeg -vn -ar 16000 -ac 1 -c:a pcm_s16le` → `06.wav` (16 kHz mono PCM, ~20 MB, 639.2 s).
El `.wav` es intermedio y gitignored; no se versiona.

### Parámetros de transcripción — IDÉNTICOS en ambas pasadas salvo el modelo
- `device="cpu"`, `compute_type="int8"`, `language="es"`, `beam_size=5`
- `vad_filter=True`  (anti-alucinación en silencios; salvaguarda de RD-2)
- `condition_on_previous_text=True`  (no hubo bucles de repetición; el plan B `=False` no fue necesario)

**`initial_prompt` EXACTO usado (parte del linaje de la fuente):**

```
Análisis fundamental de empresas. Estados financieros, balance, cuenta de resultados, flujo de caja. EBITDA, EBIT, ROIC, ROE, ROCE, FCF, capex, EPS, BPA. Deuda financiera, deuda neta, net debt, caja, Enterprise Value, EV, market cap. Múltiplos: PER, EV/EBITDA, EV/FCF, P/B. Moat, foso defensivo, ventaja competitiva, switching costs, efecto red, pricing power. Tickers: $ASML, $TSM, $QCOM, $TXN, AMD, Intel, Nvidia. Fuente: TIKR, Damodaran, 10-K, 10-Q.
```

### Medición (audio = 639.2 s / 10.65 min)

| Modelo | Cómputo | Ratio cómputo:audio | Segmentos | Chars | Bucles |
|---|---|---|---|---|---|
| medium   | 605.5 s (10.09 min) | **0.95x** | 121 | 10 212 | 0 |
| large-v3 | 1201.1 s (20.02 min) | **1.88x** | 358 | 10 123 | 0 |

Carga+descarga del modelo (1ª vez): medium 29.4 s, large-v3 52.1 s (ya cacheados para el lote).

### Fidelidad de la jerga (criterio decisivo)
En un vídeo cuyo tema central es el **Enterprise Value**:
- **`medium` corrompe "EV" → "LV" 5 veces** (p.ej. *"LV partido el free cash flow, o LV partido
  EBITDA, o LV partido EBITDA"* — además duplica el término), y escribe *"net debit"* en vez de
  *"net debt"*.
- **`large-v3`: 0 errores de "EV"**; ratio limpio (*"Como EV partido por EBITDA"*), `net debt`
  correcto, sin errores nuevos donde medium acertaba. Segmentación más fina → timestamps más
  precisos para citar (RD-2).

### Decisiones y artefactos
- **Canónico del vídeo 06 = `large-v3`** → `raw/transcript/06_deuda_y_caja.srt` + `.txt`.
- Las dos variantes del piloto son **regenerables** con los parámetros de arriba; no se versionan
  (viven en el scratchpad de la sesión). Este log es el registro durable de la comparación.

### D-19 (¿PDFs desactualizados vs vídeo?) — sigue PENDIENTE
La transcripción sola no resuelve el desfase de numeración interna de las slides: eso exige cotejar
las cabeceras del PDF contra el contenido del vídeo, tarea de Fase B / ficha, fuera del alcance de
esta sesión. **D-19 sigue PENDIENTE DE VERIFICACIÓN.**

---

### D-29 · Modelo de transcripción del lote de 19 = large-v3 (int8)
**Estado:** PROPUESTA — **recomendación del piloto, pendiente de ratificación del usuario**
- **Decisión propuesta:** transcribir los 19 vídeos con `large-v3`, `compute_type="int8"`, y los
  mismos parámetros del piloto (vad_filter, initial_prompt, language=es, beam=5).
- **Motivos:** la transcripción es la fuente canónica de las 19 fichas; un error de acrónimo
  (EV→LV) se propaga a todo el cerebro (RD-1/RD-2). La fidelidad de large-v3 sobre la jerga es
  netamente superior. El coste (~1.9x tiempo real; ~1 noche desatendida para los 19) es
  irrelevante frente a la fidelidad, criterio fijado por el usuario.
- **Alternativa (medium):** ~2x más rápida (0.95x tiempo real) pero corrompe el acrónimo central
  del dominio. Descartada para la fuente canónica.
- **Consecuencia si se ratifica:** ejecuta D-23 con este modelo. El vídeo 06 ya queda hecho.

---

## [2026-07-12] ratificacion+prompt-v2 | D-29 RATIFICADA; initial_prompt v2 supersede a v1

### D-29 · RATIFICADA
El usuario ratifica **large-v3 (int8)** como modelo de transcripción de los 19 vídeos.
`decisiones.md` → RATIFICADA. Argumento adicional del usuario: el PDF del módulo 06 da la fórmula
del EV **invertida** (`EV = Market Cap − Net Debt`, falsa; correcta = `Market Cap + Deuda Neta`,
ver "Erratas ya confirmadas" arriba). El vídeo es el único árbitro de ese error; con `medium`
(que corrompe "EV"→"LV") habríamos tenido **fuente errónea (PDF) + fuente corrupta (transcripción)**
para el concepto central del módulo. Inaceptable.

### initial_prompt v2 — SUPERSEDE a v1
**v1 (registrada en la entrada `transcripcion-piloto` de esta misma fecha) queda SUPERSEDIDA.**
Estaba sesgada hacia los módulos 6 y 10. La **v2** añade el vocabulario de los vídeos 13–19 —los
que NO tienen PDF de respaldo (D-13)—, que son justo donde no hay red de seguridad si large-v3
corrompe jerga: multibagger, margen de seguridad, recompras/buybacks, payout, goodwill, beta,
volatilidad, drawdown, y más múltiplos (EV/EBIT, PEG). v1 solo se usó en el piloto comparativo del
06 (medium vs large-v3), cuyo canónico se **regenera** con v2. **Los 19 se transcriben con v2**,
parámetros idénticos → linaje consistente.

**Tokens (tokenizer real de large-v3; límite efectivo del prompt = 223 = max_length//2 − 1):**
v1 = 169 · **v2 = 208 → cabe entera, sin recorte.**

**`initial_prompt` v2 EXACTO (verbatim):**

```
Análisis fundamental de empresas cotizadas. Cuenta de resultados, balance, flujo de caja, 10-K. EBITDA, EBIT, ROIC, ROE, ROCE, FCF, free cash flow, capex, EPS, BPA. Deuda financiera, deuda neta, net debt, caja, Enterprise Value, EV, market cap. Múltiplos: PER, EV/EBITDA, EV/FCF, EV/EBIT, P/B, PEG. Moat, foso defensivo, ventaja competitiva, switching costs, efecto red, pricing power. Multibagger, margen de seguridad, recompras, buybacks, payout, goodwill, beta, volatilidad, drawdown. Tickers: $ASML, $TSM, $QCOM, $TXN, AMD, Intel. Fuentes: TIKR, Damodaran.
```

**Parámetros del lote — IDÉNTICOS para los 19:** `large-v3`, `device=cpu`, `compute_type=int8`,
`language=es`, `beam_size=5`, `vad_filter=True`, `condition_on_previous_text=True`,
`initial_prompt` = v2.

### Otros
- **CLAUDE.md §2/§6.1:** corregidos los ejemplos `.mp4` → `.mkv` (extensión real; aprobado por el usuario).
- **D-19** sigue PENDIENTE (se resuelve cotejando slides vs vídeo al redactar la ficha, no ahora).

### Plan de ejecución (esta sesión)
1. Regenerar vídeo 06 con v2 (checkpoint de que v2 no rompe la jerga antes del lote largo).
2. Lote de los 18 restantes, desatendido (~6.8 h estimadas).
3. Verificación obligatoria post-lote: spot-check de jerga en 17/18/19; loops por vídeo (deben ser 0);
   señalar cualquier vídeo con ratio de cómputo disparado (audio problemático).

---

## [2026-07-12] rechazo-v2 + gobernanza | v2 RECHAZADO tras checkpoint; tandas; máquina secundaria

### initial_prompt v2 — PROBADO Y RECHAZADO
initial_prompt v2 probado sobre el vídeo 06 y RECHAZADO. Degrada una transcripción que con v1 era
limpia: EV→LV ×5, EBITDA→'evita', pérdida de puntuación en cascada, repeticiones intra-segmento,
ratio 2.79x vs 1.88x, segmentación 111 vs 358 segmentos. El lote usa initial_prompt v1.

**Corrección de la entrada previa (`ratificacion+prompt-v2`; append-only, no se edita):** lo que
allí decía "v1 SUPERSEDIDA / los 19 se transcriben con v2" queda **revertido**. El prompt canónico
es **v1** (`tools/prompt_v1.txt`). El 06 canónico permanece en su versión v1 (idéntica a git HEAD);
la regeneración v2 se descartó (copia solo en scratchpad efímero, no versionada). `prompt_v2.txt` y
`diag06.py` borrados.

### Herramientas versionadas (`tools/`)
- `transcribe.py` — el que generó el 06 canónico (**sin cambios**).
- `batch_transcribe.py` — el del lote. **Corregido con aviso al usuario:** usaba prompt v2 y rutas
  hardcodeadas al scratchpad de la sesión; ahora lee `tools/prompt_v1.txt` y auto-detecta rutas +
  ffmpeg del PATH, con la llamada a `transcribe()` byte-idéntica en parámetros a `transcribe.py`.
  Verificado: `prompt_v1.txt` == prompt inline de `transcribe.py` (452 chars).
- `prompt_v1.txt` — initial_prompt canónico (452 chars, 169 tokens).
- `requirements.txt` — versiones congeladas (linaje de datos): faster-whisper 1.2.1, ctranslate2
  4.8.1, av 18.0.0, onnxruntime 1.27.0, numpy 2.5.1, tokenizers 0.23.1. Reproducir exige estas
  versiones exactas.

### D-30 · Transcripción del lote en TANDAS de 4–5, no en batch único
**Estado:** RATIFICADA
- El lote se transcribe en tandas de 4–5 vídeos, con verificación y commit entre cada una.
- **Motivo:** aislar fallos, no descubrir un problema 7 horas tarde (lección del checkpoint del 06).

### D-31 · initial_prompt v2 PROBADO y RECHAZADO; el lote usa v1
**Estado:** RATIFICADA — supersede la adopción de v2 de la entrada `ratificacion+prompt-v2`.
- Evidencia arriba. El lote usa `initial_prompt` v1 (`tools/prompt_v1.txt`).

### D-32 · Acciones autónomas largas requieren preguntar antes de lanzarlas
**Estado:** RATIFICADA
- Cualquier acción que Claude Code inicie por iniciativa propia (no pedida explícitamente en el
  turno) y que supere ~10–15 min de cómputo requiere **preguntar antes** de lanzarla.
- **Motivo:** el experimento diag06 de ~100 min, no solicitado.

### D-33 · El lote de los 18 restantes se ejecuta en máquina secundaria, fuera de Claude Code
**Estado:** RATIFICADA
- Máquina: Intel i5-8400 (6 núcleos/6 hilos), 16 GB RAM, con los scripts versionados de `tools/`.
- **Motivo:** aislar el riesgo de fallo de la máquina de trabajo diaria y no gastar cuota del plan
  en horas de cómputo puro.
- **Seguridad:** no depende de que Claude Code observe el cómputo — los parámetros son deterministas,
  la verificación es posterior sobre el `.srt`, y git (en el portátil) es la red de seguridad.

---

## [2026-07-12] hallazgo | batch_transcribe.py estaba con v2 (detectado en TAREA B antes de ejecutar)

HALLAZGO: `batch_transcribe.py` (nunca ejecutado) estaba configurado con `initial_prompt` v2, el
rechazado. Detectado en la auditoría de consistencia (TAREA B) antes de lanzar el lote. De haberse
ejecutado, los 18 vídeos habrían salido corruptos. Corregido a v1. Refuerza el principio: **todo
script que genere fuente canónica debe verificarse contra los parámetros del piloto ANTES de
ejecutarse, no después.**

---

## [2026-07-12] cambio-de-herramienta | Whisper DESCARTADO; transcripción manual + audio + capturas

**Contexto.** Se compararon 4 transcripciones del vídeo 06:
- **Whisper large-v3 (portátil):** INVIERTE la relación EV/Market Cap de AMD (dice "EV superior al
  Market Cap"; es al revés) y omite dos frases metodológicas completas. Su buena puntuación lo hacía
  parecer el mejor: era el PEOR.
- **Whisper large-v3 (otra máquina):** acierta la dirección, pero destroza los acrónimos
  (EBITDA→"evita"/"evi"/"vida") y la puntuación.
- **Qwen3-ASR local:** 3 intentos fallidos de integración. Abandonado.
- **ElevenLabs Scribe:** excelente, pero es nube y coste por créditos.

DECISIÓN: transcripción base local + CORRECCIÓN MANUAL del usuario en Subtitle Edit, contra el
vídeo. El `.srt` corregido a mano es la FUENTE CANÓNICA.

### D-45 · Whisper DESCARTADO como herramienta de transcripción
**Estado:** RATIFICADA — **SUPERSEDE a D-23, D-29, D-30, D-33**
- Evidencia: produce inversiones factuales silenciosas y omite contenido.
- **LECCIÓN CLAVE:** la calidad de la puntuación NO es indicador de fidelidad. Un texto bien puntuado
  con un error direccional es MÁS peligroso que uno feo, porque baja la guardia del revisor.
- Herramientas movidas a `_archivo/whisper/` (evidencia; no reutilizar).

### D-46 · Transcripción con Subtitle Edit + corrección manual del usuario
**Estado:** RATIFICADA
- Flujo: transcripción base → el usuario corrige en Subtitle Edit viendo el vídeo → `.srt` corregido
  = FUENTE CANÓNICA → `.txt` se exporta DESDE el `.srt` (nunca se edita a mano). Salida UTF-8, con
  timestamps → cumple RD-2.
- REGLA: el usuario corrige errores de MÁQUINA (lo que se oyó mal). NUNCA corrige errores del
  EXPERTO — si él dice algo mal, se transcribe tal cual, y el cerebro lo detecta cruzando con el PDF.

### D-47 · raw/video/ se SUSTITUYE por raw/audio/ (.mp3)
**Estado:** RATIFICADA
- Motivo: ninguna IA procesa vídeo hoy; los `.mkv` solo ocupaban espacio. Los vídeos originales están
  íntegros en otra carpeta del usuario, fuera del proyecto — no se pierde nada. Para ver una
  diapositiva, se abre el vídeo original desde allí.
- Acción ejecutada: eliminado `raw/video/` (1.3 GB); creado `raw/audio/` (gitignored, `.gitkeep`);
  actualizados `.gitignore` y `CLAUDE.md §2`.

### D-48 · Capturas de pantalla como TERCERA fuente
**Estado:** RATIFICADA
- HALLAZGO: Claude Code NO ve vídeo ni oye audio; solo lee texto e imágenes estáticas. Los PDFs solo
  cubren 12 de 19 vídeos y son de una edición anterior (D-19). Todo contenido VISUAL que no esté en
  el PDF (tablas, gráficos, pantallazos de TIKR) se perdería para siempre.
- Acción: creado `raw/capturas/` (VERSIONADA en git). El usuario captura, durante la corrección,
  cualquier elemento visual con información NO presente en el PDF. Nombre: `NN_descripcion.png`.
- ⚠️ RECORDATORIO ACTIVO añadido a §6.2: al ingerir un módulo, si la transcripción menciona algo
  visual ("aquí vemos", "en esta tabla", "fijaos en la gráfica") y NO hay ni PDF ni captura que lo
  cubra, DEBO avisar al usuario ANTES de escribir la ficha. No escribirla con el hueco.

### D-49 · Separación estricta EJEMPLOS vs REGLAS
**Estado:** RATIFICADA
- PROBLEMA REAL (módulo 06): el experto muestra AMD (Net Debt/EBITDA = −0,52x) e Intel (3,58x) como
  EJEMPLOS ilustrativos, y en la misma explicación dice "idealmente se suele buscar valores por
  debajo de 2" — que es una REGLA. Ambos son números y conviven en la misma diapositiva. Un LLM puede
  confundirlos, y si lo hace, el umbral del cerebro queda envenenado.
- Acción: la Ficha de Concepto separa OBLIGATORIAMENTE dos campos (CLAUDE.md §4):
  - "Umbral / referencia" → REGLA. Entra en el Inventario Atómico.
  - "Ejemplos ilustrativos" → PEDAGOGÍA. NO entra en el Inventario. Marcados como no-metodológicos.
- Los datos de empresas concretas (AMD, Intel, cifras de TIKR) son SIEMPRE ejemplos, nunca datos
  operativos (coherente con RD-1). Ante duda sobre si un número es regla o ejemplo → PREGUNTAR al
  usuario. No adivinar.

### Consecuencias sobre lo anterior (ejecutadas en esta sesión)
- **D-23, D-29, D-30, D-33 → SUPERSEDIDAS por D-45** en `decisiones.md` (todo el aparato Whisper:
  modelo, tandas, máquina secundaria).
- D-31 (initial_prompt v2 rechazado) y las cuestiones abiertas #6 (causa raíz v2) y #7 (revalidar
  batch_transcribe.py) quedan **sin objeto** al desaparecer Whisper; retiradas de las cuestiones
  vigentes de `decisiones.md`. El histórico permanece aquí (append-only).
- `tools/` → `_archivo/whisper/` con `README.md` explicando el abandono (D-45).
- `raw/transcript/06_deuda_y_caja.srt/.txt` (Whisper) → `06_whisper_DESCARTADO.srt/.txt`, para que el
  nombre no mienta y el usuario coloque su `.srt` corregido con el nombre limpio.
- **Residuos de Whisper que NO se han borrado** (no solicitado): `.venv-whisper/` (290 MB, en el
  proyecto, gitignored) y la caché HF de modelos (~4.4 GB, en `~/.cache/huggingface/`, fuera del
  proyecto).

---

## [2026-07-13] ingesta-06 | Primera ficha del cerebro: módulo 06 (Deuda y Caja) — 4 fichas

Primera ingesta real (protocolo 6.2). De aquí se induce la plantilla definitiva (D-25; TAREA 3
pendiente de OK del usuario). Fuentes: `.srt` corregido a mano (D-46, canónico) + PDF (9 slides).

### Auditoría de fuentes (previa, aprobada)
- **Confirmado "manda el vídeo" (D-19):** el vídeo explica bien la fórmula del EV (Market Cap + Deuda
  Neta) mientras el PDF la tiene invertida. La cabecera del PDF dice "4. La Deuda y la Caja" para el
  vídeo 6 → confirma el desfase −2 (edición anterior del curso).
- Herramienta: instalado `pymupdf` para rasterizar el PDF y leer las cifras dentro de los pantallazos
  de TIKR (imágenes, no texto).

### Decisión de granularidad: 4 fichas atómicas, no una
`deuda_financiera` · `caja` · `deuda_neta` · `enterprise_value`, enlazadas. Motivo: cada una tiene
inputs atómicos, naturaleza temporal y aplicabilidad propios; una sola ficha "Deuda y Caja" fundiría
cuatro unidades atómicas (lo que el Inventario Atómico, D-02, necesita separadas). Cadena:
`Deuda Neta = f(Deuda Financiera, Caja)`; `EV = f(Market Cap, Deuda Neta)`.

### Enterprise Value = ficha ABIERTA (estado: parcial)
El EV es concepto de **valoración**, no de estructura financiera; vuelve en módulos 12–16 (múltiplos).
Se crea con aviso explícito "no cerrar aquí" para evitar dos fichas del EV compitiendo más adelante.

### Primera REGLA operativa del curso: Net Debt/EBITDA < 2  [VÍDEO 06, 09:31]
Registrada en [[deuda_neta]] con estado epistémico **HEURÍSTICA DEL EXPERTO, SIN JUSTIFICAR**. No se
adopta por autoridad (D-08). Enlaza con D-15 (¿umbral absoluto o benchmark sectorial?) → revisar en
vídeo 16.

### Separación regla/ejemplo (D-49)
REGLA: `< 2`. EJEMPLOS (marcados no-metodológicos, NO al Inventario): TIKR AMD/Intel (−0,52x / 3,58x /
141.426 / 82.546 …) y los 100.000€/200.000€ de la analogía.

### Erratas del módulo 06 (4) → wiki/erratas.md
06-E1 fórmula EV invertida (p.5) · 06-E2 def. verbal de deuda neta invertida (p.4) · 06-E3 cajas de
decisión incompatibles con E1 (p.5) · 06-E4 rótulo AMD/Intel (p.9). **3 afirmaciones falsas + 1
incoherencia interna**, todas en la parte de valoración.

### 7 huecos, clasificados por "Resolución esperada"
- **Módulo posterior:** ratios de apalancamiento (→ mód. 07, el experto los remite a "la siguiente
  clase"); justificación/calibración del umbral "2" (→ vídeo 16 / D-15).
- **Complemento/ externo:** leasings (IFRS 16 / ASC 842) en la deuda; perímetro de la caja; exclusión
  sectorial (bancos/aseguradoras).
- **Decisión de arquitectura pendiente:** puente completo del EV (fuente canónica: cálculo propio vs
  proveedor); naturaleza temporal / look-ahead (Market Cap intradía vs balance).

### Pendientes
- **Inventario Atómico** (`wiki/inventario_atomico.md`): NO creado aún. Los inputs atómicos están
  marcados en las fichas; se tabulará tras fijar la plantilla definitiva (TAREA 3).
- **complemento/**: vacío por decisión (nada aún).

---

## [2026-07-13] D-51 + plantilla definitiva | Capa procedimental; 16 campos; retrofit del módulo 06

### D-51 · El cerebro necesita una capa PROCEDIMENTAL
**Estado:** RATIFICADA
- **HALLAZGO:** el patrón LLM Wiki captura conocimiento **declarativo** (qué es cada concepto) pero no
  **procedimental** (en qué orden se aplica, qué se mira primero, qué descarta una empresa). Sin eso,
  el cerebro sabe *definir* pero no *analizar*: ante "analiza Adidas" no sabría por dónde empezar.
- **DÓNDE ESTÁ ese conocimiento:** en los vídeos **13–19** — y no es casualidad que sean los **únicos
  sin PDF**: el juicio no se puede poner en diapositivas. Lo habíamos interpretado como una omisión
  del experto; era una **señal**.
- **DECISIÓN:** se creará `wiki/curso/protocolo_analisis.md`, la secuencia ejecutable del método,
  enlazando a las fichas. **NO se escribe ahora: se deriva de 13–19.** Escribirlo antes sería
  inventarlo (viola D-01).
- **CASO DE USO FINAL:** "analiza esta empresa" → el cerebro **ejecuta** el protocolo. No: "búscame los
  datos y dime tú dónde mirar".

### Plantilla CUANTITATIVO DEFINITIVA (D-25 cerrado para el perfil cuantitativo)
Inducida del módulo 06 y aplicada a `CLAUDE.md §4`. **16 campos** = 13 aprobados + 3 de la capa
procedimental (D-51):
- **13 base:** Definición · Fórmula · Tipo · Inputs atómicos · Normalización · Naturaleza temporal ·
  Umbral (con 4 sub-campos epistémicos) · Aplicabilidad sectorial · Interpretación · Ejemplos
  (no-inventario) · `## Errata` (con ID) · `## Huecos` (con "Resolución esperada") · `## Enlaces`.
- **3 nuevos (D-51):** `## Rol en el análisis` (eliminatorio/condicionante/contextual) · `## Momento de
  evaluación` (qué precede/sigue) · `## Criterio de parada`.
- Frontmatter ampliado: `estado` admite `parcial`; nuevos `transversal` y `enlaces`.
- **REGLA DE ORO (D-51):** si el curso no dice el orden/rol/parada, es `[HUECO]`. **NO se deduce.**
- El **perfil CUALITATIVO sigue PROVISIONAL** (a inducir con el módulo 10 / moat).

### Retrofit de las 4 fichas del módulo 06 con los 3 campos nuevos
Como se preveía, **casi todo `[HUECO]`** — y eso es información: mide cuánto del método NO está en los
módulos declarativos. Resolución esperada dominante: **vídeos 17–19** (función de decisión). Un hueco
señalado como crítico: en [[deuda_neta]], superar `Net Debt/EBITDA > 2` sin razón sectorial ¿descarta
o solo alarma? El experto no lo dice.

### §6.2: extracción activa de secuencia (D-51)
Al ingerir cualquier módulo se extraen **verbatim** las frases de secuencia / criterio de parada
("lo primero que hago…", "si veo esto ya no sigo…", "en la siguiente clase…") → a
`protocolo_analisis.md` (EN CONSTRUCCIÓN). Del módulo 06 ya se capturaron 3 fragmentos (remisión a
estados financieros, a ratios del módulo 07, y al EV en la fase de múltiplos 12–16).

### Artefactos creados
- `wiki/curso/protocolo_analisis.md` — esqueleto vacío + aviso "no rellenar por deducción" + fragmentos
  del 06.
- `wiki/inventario_atomico.md` — construido desde las tablas de "Inputs atómicos": 11 inputs atómicos,
  4 métricas construidas, 1 regla (Net Debt/EBITDA < 2). Ejemplos excluidos (D-49).

### Nota
El `01_*.srt/.txt` es material del usuario y queda versionado (confirmado por él).

---

## [2026-07-13] D-53 + D-54 | Corrección del alcance procedimental; dependencia circular; plan de ingesta

### D-53 · El bloque procedimental es 13–19, NO 17–19  (CORRIGE una suposición previa)
**Estado:** RATIFICADA — corrige el "17–19" usado en el retrofit de D-51.
- Los títulos lo delatan: **"14. ¿Cuándo usarlos?"** es una pregunta de **procedimiento**; **"16. La
  realidad de los múltiplos"** son matices de **uso**. Además el vídeo 16 lleva el **enlace de
  Damodaran** → es donde se resuelve **D-15** (¿benchmarks sectoriales o umbrales absolutos?).
- El supuesto "13–16 = múltiplos = declarativo" era **una suposición sin base**.
- **Acción ejecutada:** corregido "17–19" → "13–19" en las "Resolución esperada" de las 4 fichas del
  módulo 06 (es metadato nuestro, no contenido del experto; RD-3 respetado, con disclosure). El
  `protocolo_analisis.md` ya apuntaba a 13–19.

### D-54 · DEPENDENCIA CIRCULAR identificada (protocolo ↔ fichas)
**Estado:** RATIFICADA
- El protocolo necesita fichas (para enlazar); las fichas necesitan el protocolo (para saber si un
  ratio es ELIMINATORIO o CONTEXTUAL).
- **Resolución:** NO se escribe el protocolo hasta tener el **vocabulario mínimo ingerido**.
- **Corrección de un error propio:** se dijo que "el vocabulario está cubierto" porque los vídeos 01–07
  están TRANSCRITOS. Pero solo el **06 está INGERIDO**. **Transcrito ≠ ingerido.**

### Plan acordado
1. **Ingerir 02, 03, 04, 05, 07** (ya transcritos) → vocabulario base. Necesario en cualquier escenario.
2. En paralelo, el usuario **VE el vídeo 14 ("¿Cuándo usarlos?")** sin transcribirlo. Es un **SONDEO**:
   determina si el protocolo existe en el curso o hay que construirlo en `complemento/`.
3. Con esa respuesta se decide el orden del resto.

### Cuestión abierta CRÍTICA
**¿Existe el protocolo de análisis en el curso, o el experto solo enseña conceptos y el orden lo da
por supuesto?** Si no existe, habrá que construirlo en `complemento/` con **justificación de tres
pilares** — y **eso cambia la naturaleza del proyecto** (de *destilar* un método a *construirlo*).

---

## [2026-07-13] sondeo-procedimental | Ejecutado el sondeo sobre los vídeos 14, 15 y 17

Ejecutado un **sondeo** (no ingesta) para contrastar la hipótesis de si los 3 campos procedimentales
(orden / descarte / momento) están bien diseñados o si el método del experto es de naturaleza
distinta. Se leyeron íntegras las transcripciones canónicas (D-46) de:
- `14_cuando_usarlos.srt` · `15_ratios_fundamentales.srt` · `17_multibagger.srt` (ninguno con PDF).

Se clasificó cada afirmación sobre *cómo se usa* una métrica (no sobre qué es), excluyendo ejemplos
pedagógicos (D-49) y navegación de herramientas, sin deducir orden implícito (D-51/D-53). Resultado
en `wiki/sondeo_procedimental.md` (44 entradas clasificadas en ORDEN / DESCARTE / RELACIÓN / RANGO /
FASE / OTRO, con recuento por tipo y por vídeo).

**SIN CONCLUSIONES** — la interpretación de este recuento (¿existe el protocolo?, ¿hay que rediseñar
los 3 campos?) es **decisión del usuario** y se toma después, contra esta evidencia. El sondeo cubre
solo 3 de los 7 vídeos del bloque 13–19 (faltan 13, 16, 18, 19); **no** es un veredicto del bloque.
D-15 no se toca aquí: en estos 3 vídeos no se nombra a Damodaran (se esperaba en el vídeo 16).

---

## [2026-07-15] cierre-radiografia | Cierre de la fase de radiografía; apertura de etapa post-radiografía

### D-55 · Apertura de etapa post-radiografía
**Estado:** RATIFICADA
- **Decisión:** `wiki/radiografia.md` queda como **documento fundacional** de una etapa nueva del
  proyecto (etapa post-radiografía).
- **Hallazgos que la fundan** (todos con respaldo en `radiografia.md`):
  - El método **NO es secuencial**: no existe un pipeline 1→2→…→N prescrito para analizar una
    empresa completa (Sección C).
  - El curso es un **inventario de conceptos con interpretación, cruzados relacionalmente**, sobre
    una arquitectura temática laxa. Único orden global explícito: negocio→ratios [VÍDEO 15, 00:39].
  - El material pide **VARIOS moldes** (≥5), con corte cuantitativo / cualitativo / capa de decisión
    (Sección D).
  - Se indujeron **14 tipos de afirmación metodológica** (Sección A).
- **Consecuencia declarada:** la ESTRUCTURA del proyecto (plantillas, esquema de campos) se
  **REDEFINIRÁ** desde la radiografía en el próximo paso. Las decisiones ESTRUCTURALES de la etapa
  pre-radiografía (p.ej. la plantilla cuantitativa única y los 3 campos procedimentales) se
  **supersederán UNA A UNA** cuando su reemplazo se diseñe — **NO se anulan en bloque ahora**.
- **Se conservan en vigor, transversales a la etapa nueva:** RD-1, RD-2, la disciplina de fuentes
  (D-46, jerarquía vídeo>PDF), append-only, la regla de no rellenar huecos, y "los ejemplos del curso
  son pedagogía, no metodología".

### D-56 · [CORREGIDO] Resolución de D-15 (benchmark sectorial)
**Estado:** RATIFICADA — corrige y confirma la sustancia de D-15 (la entrada D-15 no se reescribe;
append-only)
- La hipótesis de D-15 (el experto usa **BENCHMARKS SECTORIALES relativos**, no umbrales absolutos)
  queda **CONFIRMADA** por la radiografía: la referencia sectorial es omnipresente, con la coletilla
  recurrente "depende del sector".
- **Fuente externa identificada:** la página *"Revenue Multiples by Sector (US)"* en
  `https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html`, cuyo autor es
  **Aswath Damodaran** (consta en el pie de la propia página).
- El experto **ENLAZA** este recurso en la descripción del **VÍDEO 16** (~20:38: *"una web con
  referencia de los múltiplos precio/venta según el sector"*). **NO pronuncia el nombre "Damodaran"**
  en ninguno de los 19 vídeos — por eso la radiografía (que solo leyó transcripciones `.srt`) reportó
  correctamente que el nombre no aparece. El nombre estaba en el proyecto como inferencia previa;
  queda **CONFIRMADO** como el autor de la página enlazada.
- Los datos de la página son **"a fecha de enero de 2026"**: es una **fuente viva** que se
  actualiza. Tratamiento bajo RD-1: se referencia la URL como fuente estructurada externa; **NO se
  hardcodean cifras sectoriales en las fichas**.
- **Verificación de coherencia:** las afirmaciones sectoriales del experto (p.ej. EV/Ventas x10–x20
  normal en tech/software, vídeo 16) cuadran con las cifras de esta página. La fuente del experto es
  esta.

### D-57 · [HALLAZGO] Nueva clase de fuente: enlaces en descripción
**Estado:** REGISTRO — ítem abierto, no decisión cerrada
- Resolver D-15 destapó que los **recursos enlazados en la descripción de un vídeo** son una clase
  de fuente no contemplada en la jerarquía actual (vídeo > PDF). No son transcripción ni PDF del
  curso: son material externo que el experto avala explícitamente.
- La radiografía no pudo verlos (solo leyó `.srt`). Esta clase vive fuera del transcript.
- **Propuesta preliminar (NO adoptada):** clase `[ENLACE-DESC]` con la URL. La formalización se
  decide durante el diseño de la estructura, no ahora.

**Resumen:** cierre de la fase de radiografía; apertura de etapa post-radiografía (D-55); corrección
de D-15 (D-56); hallazgo de nueva clase de fuente — enlaces en descripción (D-57).

---

## [2026-07-15] cierre-repositorio | Fase de radiografía y consolidación de repositorio COMPLETADA

Fase de radiografía y consolidación de repositorio **COMPLETADA** a esta fecha (`radiografia.md`
commiteado; D-55/D-56/D-57 registradas; estado de D-15 actualizado en el índice; transcripciones y
capturas pendientes de los vídeos 08–19 trackeadas). El proyecto queda **en pausa** a la espera del
diseño de la estructura nueva (moldes, campos, estatus de `protocolo_analisis.md`) — **decisión
pendiente, NO tomada todavía**.

---

## [2026-07-16] funcion+arquitectura | Función del proyecto y arquitectura de tres capas

### D-58 · [DECISIÓN] Función del proyecto: copiloto de consulta interpretativa
**Estado:** RATIFICADA
- **Decisión:** la función del cerebro **NO** es ejecución autónoma (dar el nombre de una empresa y
  que produzca el análisis de principio a fin).
- **Motivo:** la radiografía (Sección C, D-55) estableció que **no existe un pipeline secuencial
  1→2→…→N** en el curso; un modo autónomo obligaría al cerebro a **inventar** un orden que el
  experto nunca dio — violación del espíritu de RD-1/RD-2 aplicada al procedimiento.
- **Función adoptada: COPILOTO DE CONSULTA INTERPRETATIVA.** El usuario (o una fuente estructurada)
  aporta el dato de una empresa concreta, y el cerebro devuelve lo que el experto diría sobre ese
  dato:
  - interpretación direccional (T2)
  - umbral y su naturaleza absoluta/sectorial, con fuente viva si aplica (T3)
  - lectura relacional con otras métricas (T6)
  - aplicabilidad condicionada (T4)
  - advertencia de uso aislado (T5)

  El usuario conserva el recorrido y la decisión de inversión.
- **Encaje:** con la naturaleza del corpus (interpretativo y relacional, no secuencial — Secciones
  C/D de `radiografia.md`) y con lo que el propio usuario describió: *"un listado optimizado de qué
  tener en cuenta, para decidir qué merece seguir excavando."*

### D-59 · [DECISIÓN] Arquitectura de tres capas (construcción vs uso)
**Estado:** RATIFICADA
- **Decisión:** se separan **CONSTRUCCIÓN** y **USO**. El cerebro se construye una vez, cerrado y
  auditable, y solo después se usa desde fuera. Las capas de uso **NO modifican el cerebro**.
- **CAPA 1 — El cerebro (construcción):** método del experto, **SOLO material local del curso**
  (transcripciones, capturas, PDFs como borrador). No busca ni se conecta a nada externo. Es el
  intérprete. **Es la fase actual del proyecto.**
- **CAPA 2 — Datos cuantitativos de la empresa (uso):** los números que se traen a una plantilla
  externa (Excel/Sheets, proyecto hermano, **aún NO diseñado**). Su origen debe respetar **RD-1**
  (fuente estructurada: proveedor/XBRL, **nunca** un LLM leyendo un documento). **Pregunta abierta:**
  proveedor de datos concreto.
- **CAPA 3 — Contexto cualitativo (uso, en paralelo):** Claude buscando en internet **noticias y
  contexto cualitativo** (modelo de negocio, equipo directivo, eventos que afecten a la cotización,
  qué descuenta el mercado). **RD-1 NO aplica aquí** porque no son cifras que entren en un cálculo.
  Es una capa externa, **desechable, por consulta**. **NO entra en el cerebro ni es fuente canónica.**
- **Consecuencia:** las capas 2 y 3 quedan **APARCADAS** hasta que el cerebro esté construido. No se
  diseñan ahora. El cerebro (Capa 1) es lo único en curso.
- **Nota de visión (no decisión cerrada):** este cerebro sería el motor de la "pata" de análisis
  fundamental dentro de un conjunto futuro de cerebros (mentalidad Buffett ya existente; posible
  cerebro cripto/DeFi separado por ser activos de naturaleza distinta). Se registra como **contexto,
  NO se diseña**.

**Resumen:** registradas función del proyecto — copiloto de consulta interpretativa (D-58) — y
arquitectura de tres capas — construcción vs uso (D-59); las capas de uso quedan aparcadas hasta
completar el cerebro.

---

## [2026-07-16] estatus-protocolo | Se destila el protocolo mínimo; consolidación de la capa procedimental

### D-60 · [DECISIÓN] El protocolo se DESTILA tal como aparece; NO se construye
**Estado:** RATIFICADA — **cierra la cuestión abierta CRÍTICA nº7**; supersede la rama «construir» de D-54

- **Decisión:** el proyecto **destila el protocolo mínimo tal como aparece en el curso**. **NO** se
  construye uno más completo en `complemento/`. Si el curso no da más orden que el que da, **se queda
  así**.
- **Base:** `radiografia.md` §C, sobre los 19 vídeos. El protocolo **existe pero es mínimo**:
  - **un orden global** — negocio antes que ratios: *«**Primero** debes conocer el negocio de la
    empresa […] **Posteriormente** ya pasas a someterte a una serie de ratios»* `[VÍDEO 15, 00:37–00:51]`
  - **dos procedimientos locales** — lectura del 10-K (índice → item 1 → 1A → 7 → 8)
    `[VÍDEO 05, 05:41]` y ss.; y riesgo → dimensionamiento en cartera `[VÍDEO 18, ~10:27–10:41]`
  - veredicto literal de §C: *«**No hay** un "paso 1→2→…→N" prescrito para analizar una empresa completa»*
- **Lo que esto cambia:** los `[HUECO]` de **orden**, **rol** y **criterio de parada** dejan de ser una
  **deuda pendiente** y pasan a ser un **HALLAZGO sobre la naturaleza del curso**: el experto enseña
  **qué mirar y cómo interpretarlo**, no **en qué orden ni cuándo parar**. Se dejan visibles (RD-4) y
  **no se rellenan** — tampoco con los 16 módulos que faltan, salvo que el experto lo diga literalmente.
- **Cierra la cuestión nº7** (*«¿existe el protocolo, o el experto solo enseña conceptos y el orden lo
  da por supuesto?»*, D-54): **existe, y es mínimo**. Por tanto **la naturaleza del proyecto NO cambia**:
  sigue siendo **destilar**, no construir. La rama de D-54 —*«si no existe, habrá que construirlo en
  `complemento/` con tres pilares, y eso cambia la naturaleza del proyecto»*— queda **CERRADA sin
  activarse**.
- **Encaje con D-58:** un protocolo mínimo **basta** para un copiloto de consulta interpretativa. Solo
  era un problema bajo la hipótesis de **ejecución autónoma**, que D-58 ya descartó.
- **Sigue rigiendo, y ahora con más fuerza — REGLA DE ORO (D-51):** si el curso no dice el orden, el
  rol o la parada, es `[HUECO]`. **NO se deduce la secuencia.**

**Evidencia adicional recogida al aplicarla** (material ingerido: módulos 03, 06, 07, 10):
- **Cero criterios de parada.** Ni una frase del tipo «si veo esto, ya no sigo». Ni una.
- **Cero roles declarados** (eliminatorio / condicionante / contextual). Concuerda con el retrofit de
  D-51 sobre el módulo 06, que ya dio «casi todo `[HUECO]`».
- **Un solo marcador de orden** en el vídeo 03: *«…cuánta caja tiene, **y después** revisar la parte de
  la deuda, sobre todo a corto plazo»* `[VÍDEO 03, 06:54–07:18]`. El resto de esa frase es enumeración
  («también», «y si»), **no orden**.
- **Patrón transversal de PROFUNDIDAD**, no registrado hasta ahora: el experto insiste en que el
  análisis es superficial a propósito — *«son cuatro cosas del balance»* `[VÍDEO 03, 06:09]`, *«es una
  página, son cuatro datos»* `[VÍDEO 03, 08:35]`, *«controlarlo mirando cuatro cositas»*
  `[VÍDEO 03, 09:05]`, *«ratios […] con muy pocos números»* `[VÍDEO 06, 10:30–10:39]`. **Nunca dice
  cuáles son las cuatro** → `[HUECO]`, no se rellena.

### D-61 · [DECISIÓN] `capa_decision.md` SUPERSEDE a `wiki/curso/protocolo_analisis.md`
**Estado:** RATIFICADA — supersede **solo** la designación de contenedor de D-51, no D-51 entera

- **Decisión:** la capa procedimental tiene **un único contenedor**: `capa_decision.md` (hoy en
  `wiki/piloto/`; su reubicación física es parte de la promoción del piloto, **no hecha**).
  `wiki/curso/protocolo_analisis.md` queda **SUPERSEDIDO**.
- **Motivo:** `protocolo_analisis.md` nació de D-51 bajo la hipótesis de una **secuencia ejecutable**
  concentrada en 13–19. **La radiografía descartó esa hipótesis** (§C) y **D-60** la cierra. Su propio
  subtítulo —*«la secuencia ejecutable del método»*— nombra la hipótesis muerta.
- **Procedimiento (D-55):** las decisiones estructurales pre-radiografía se supersederán **una a una
  cuando su reemplazo se diseñe**. Este es el primer caso: el reemplazo existe, así que se supersede.
- **El antiguo NO se borra** (append-only, D-18): lleva cabecera de superado, con el porqué y el mapa
  de destinos, y **su contenido original se conserva íntegro debajo**. Es la traza de una hipótesis
  falsada. *(Única modificación en `curso/` — RD-3, hecha por instrucción explícita del usuario.)*
- **Nada se ha perdido.** Los **3 fragmentos del módulo 06** que el antiguo tenía y el nuevo no se han
  **re-verificado contra `raw/transcript/06_deuda_y_caja.srt`** y enrutado por tipo:
  - `[06, 01:20–01:28]` «ya lo miramos también en los estados financieros» → **`mapa_tematico.md`**
    (orden de enseñanza)
  - `[06, 10:24–10:39]` «en la siguiente clase entraremos ya en ratios» → **`mapa_tematico.md`**
    (orden de enseñanza); su cola «con muy pocos números» → **`capa_decision.md` §2.2** (profundidad)
  - `[06, 08:18–08:34]` «cuando vayamos a valorar… múltiplos que emplean el EV» →
    **`capa_decision.md` §2.4** (fase del análisis)

**Hipótesis heredadas que se marcan MUERTAS al consolidar:**
- ⛔ *«Caso de uso final: "analiza esta empresa" → el cerebro **EJECUTA** este protocolo»* —
  **contradice de frente a D-58** (copiloto, no ejecución autónoma). **No se traslada.**
- ⚠️ *«El conocimiento procedimental está en 13–19 […] no es casualidad que sean los únicos sin PDF:
  el juicio no cabe en diapositivas»* — **parcialmente falsada**: hay material procedimental en **03,
  05, 06, 07 y 10**, todos fuera de 13–19 y cuatro de ellos **con** PDF. **No es un bloque: está
  disperso y es fino.** *(D-53 acertó al corregir 17-19 → 13-19, pero el marco de «bloque» no se
  sostiene. D-53 no se anula: se matiza aquí.)*

### [ERRATA DE NUESTRO PROPIO MATERIAL] Cita mal ubicada en `protocolo_analisis.md`
Detectada al re-verificar contra el `.srt` canónico. **No es una errata del curso: es nuestra.**
- **Decía:** `[VÍDEO 06, 08:44]` para *«cuando vayamos a valorar si una empresa está cara o barata…»*.
- **Está en:** `[VÍDEO 06, 08:18–08:34]`. A los **08:44** el experto habla de la **caja neta de AMD**,
  otro tema. La cita apuntaba a un sitio donde no está lo citado — defecto de **RD-2**.
- **Acción:** corregida en `capa_decision.md` §2.4. En `protocolo_analisis.md` **se deja como estaba**
  (no se reescribe historia; el archivo está superado).
- **Lección para el escalado:** una cita con timestamp equivocado **es indetectable sin volver a la
  fuente**. Es el mismo modo de fallo silencioso que RD-1 previene para los números, aplicado a RD-2.

### Conflicto destapado, NO resuelto (decisión humana)
`CLAUDE.md` §6.2 manda literalmente enviar las frases *«en la siguiente clase…»* a
`protocolo_analisis.md`. Pero `radiografia.md` §C clasifica esas frases como **operativas**
—*«es logística, no interpretación»*— y **no** como método. **El schema instruye a hacer lo que la
radiografía desaconseja**, y seguirlo inflaría la capa procedimental con orden de temario, haciendo
que el protocolo **parezca secuencial** — justo lo que D-60 niega. **Registrado, no tocado**:
`CLAUDE.md` es la capa schema y su actualización no se decide aquí.

**Resumen:** cerrado el estatus del protocolo — se **destila el mínimo** tal como aparece, y su
minimalidad es un **hallazgo**, no un hueco (D-60; cierra la cuestión abierta nº7 sin cambiar la
naturaleza del proyecto). Consolidada la capa procedimental en **un único contenedor**:
`capa_decision.md` supersede a `protocolo_analisis.md`, que se marca como superado conservando su
traza íntegra (D-61). Los 3 fragmentos del módulo 06 se re-verificaron y enrutaron; **se encontró y
corrigió una cita nuestra mal ubicada** `[06, 08:44]` → `[06, 08:18–08:34]`.

---

## [2026-07-16] sync-schema | `CLAUDE.md` sincronizado con las decisiones vigentes (§6.2, moldes, fuentes)

**Contexto:** `CLAUDE.md` es la **capa schema** y se lee entera al arrancar cada sesión. Contradecía
decisiones ya tomadas en tres puntos. Se alinean **solo esos tres**; el resto del esquema no se toca.
**Alinear ≠ ampliar:** no se ha inventado contenido de esquema nuevo.

### D-62 · [DECISIÓN] El orden de ENSEÑANZA va a `mapa_tematico.md`, NO a la capa procedimental
**Estado:** RATIFICADA — **cierra la cuestión abierta nº8**; corrige `CLAUDE.md` §6.2

- **Problema:** §6.2 instruía enviar **«en la siguiente clase…»** —junto a las frases de secuencia
  real— a la capa procedimental. **El schema mandaba hacer lo que `radiografia.md` §C desaconseja**:
  §C clasifica los punteros entre clases como afirmaciones **operativas**, *«es logística, no
  interpretación»*, y **no** como método.
- **Decisión:** al ingerir se separan dos cosas que suenan igual y no lo son:
  - *«lo primero que hago es…»* · *«si veo esto ya no sigo…»* · *«esto solo lo miro cuando…»* ·
    *«aquí depende de si es una empresa de…»* → **orden de ANÁLISIS** → `capa_decision.md`, verbatim.
  - *«en la siguiente clase…»* · *«ya lo miramos en…»* · *«el segundo estado clave»* → **orden de
    ENSEÑANZA**, logística de temario → `mapa_tematico.md`.
- **Motivo, que queda escrito en el schema:** mezclarlos **infla la capa procedimental con orden de
  temario y hace que el protocolo parezca secuencial** — exactamente lo que **D-60** niega (el
  protocolo del curso es **mínimo**, y su minimalidad es un **hallazgo**, no un hueco).
- **No es hipotético: ya pasó.** El antiguo `protocolo_analisis.md` anotaba *«tras Deuda/Caja viene el
  bloque de ratios (módulo 07)»* a partir de un *«en la siguiente clase»* — leyendo orden de clases
  como orden de análisis. Corregido al aplicar D-61.
- **Se refuerza la regla de oro (D-51)** con la lección del piloto: **numerar una enumeración es
  ordenarla**. Sin marcador explícito («primero», «después», «posteriormente»), **no es secuencia**.
  Y: si un módulo no aporta nada procedimental —lo esperable bajo D-60— **no se anota nada**.

### D-63 · [DECISIÓN] `moldes.md` es la FUENTE ÚNICA de los moldes; `CLAUDE.md` §4 remite
**Estado:** RATIFICADA — supersede la generación anterior de moldes (D-20, D-25 y los 16 campos de D-51)

- **Problema:** `CLAUDE.md` §4 contenía el molde cuantitativo de **16 campos** (D-25 + D-51) y el
  cualitativo **provisional**, mientras los moldes reales viven en `moldes.md`. **Dos fuentes de
  verdad sobre qué es un molde** — el mecanismo exacto por el que `curso/` se corrompe en silencio
  (riesgo nº3 de §9).
- **Decisión:** §4 **remite** a `wiki/piloto/moldes.md` y **no copia nada**. Moldes vigentes:
  **1 · métrica cuantitativa** · **2 · estado financiero** · **3 · cualitativo**. Más dos documentos
  **no-ficha**: `capa_decision.md` (orden de análisis) y `mapa_tematico.md` (orden de enseñanza).
- **Ratificación:** los tres se pilotaron contra los vídeos **07, 03 y 10**, con dos pasadas de
  fricción documentadas en `piloto_friccion.md`.
- **Superseden:** D-20 (dos perfiles cuantitativo/cualitativo) · D-25 en su parte de plantilla
  definitiva · los 16 campos de D-51. **La regla de oro de D-51 sigue vigente.**
- **Ubicación:** `moldes.md` vive en `wiki/piloto/` porque el piloto **no se ha promovido**.
  Reubicarlo es parte de la promoción.

### D-64 · [DECISIÓN] Modelo de fuente: el PDF es la CAPA VISUAL del vídeo, no un documento aparte
**Estado:** RATIFICADA — supersede D-48 en su parte de «capturas como tercera fuente»

- **Decisión:** el PDF de un vídeo **no es un documento aparte ni un borrador desactualizado**: es el
  **deck que se ve en pantalla** mientras el experto habla. **Transcripción + PDF = las dos mitades
  del mismo momento**, y se leen juntas. **Vídeos con PDF: 01–12.**
- **`raw/capturas/` deja de ser una tercera fuente por defecto.** Solo hace falta captura **donde el
  deck no cubre lo operativo**: cuando el experto **se sale del deck** a otra pantalla o **dibuja
  encima** de la slide.
- **Un hueco de cobertura NO bloquea la ficha** (corrige el «No la escribas con ese hueco» de §6.2).
  Se escribe, se marca en el campo *Fuente*, y se anota en `capturas_pendientes.md`. **No se inventa
  lo que no se ve** (RD-4).
- **Jerarquía INTACTA: voz > PDF.** Las discrepancias se **registran** en `## Errata de la fuente`
  (4 tipos, `moldes.md`); **no se resuelven por criterio propio** (RD-1).
- **Evidencia del piloto:** el deck cubre el vídeo 07 casi entero; en el **03** cubre ≈3,5 de 9:17 y
  **los tres ratios con umbral se calculan sobre el balance de Meta, ausente del PDF** → única
  captura de prioridad alta. En el **07**, la fórmula del ROIC se **dibuja a mano** sobre la slide →
  tercera capa visual que el PDF no captura.

**Nota sobre D-19** (`PENDIENTE DE VERIFICACIÓN`): **no se toca aquí.** `mapa_tematico.md` §4 deja la
evidencia de que el desfase de numeración se explica porque **el deck es un único documento con 10
secciones repartido en 12 vídeos** (02+03 comparten la sección 2; 04+05, la 3) — no por una edición
anterior. Resolver D-19 es decisión humana, y §9 de `CLAUDE.md` (*«los PDFs pueden estar
desactualizados»*) **se ha dejado intacto** por depender de ella.

**Resumen:** `CLAUDE.md` sincronizado con las decisiones vigentes en tres puntos: el orden de enseñanza
se enruta a `mapa_tematico.md` y no a la capa procedimental (D-62; cierra la cuestión abierta nº8);
§4 pasa a **remitir** a `moldes.md` como fuente única, superseder la generación anterior de moldes
(D-63); y el modelo de fuente se alinea — el PDF es la capa visual del vídeo y la captura solo cubre
lo que el deck no alcanza, con la jerarquía voz > PDF intacta (D-64). Ningún otro punto del esquema
tocado.

---

## [2026-07-16] cierre-D19 | Resolución de D-19; alineación de §9 y §3 con D-64

### D-65 · [CORREGIDO] Resolución de D-19: el desfase NO indica PDFs desactualizados
**Estado:** RATIFICADA — **cierra D-19**, que quedaba `PENDIENTE DE VERIFICACIÓN` desde el principio.
*(La entrada D-19 **no se reescribe** — append-only, D-18. Se marca resuelta con puntero a aquí.)*

- **Lo que D-19 observó, y era correcto:** la cabecera *dentro* de los PDFs muestra otro número que el
  del vídeo — *«vídeo 6 → slide "4."; vídeo 10 → slide "8." (desfase −2 consistente)»*.
- **Lo que D-19 hipotetizó, y es FALSO:** *«los PDFs proceden de una edición anterior del curso, a la
  que luego se añadieron 2 vídeos al inicio»* → implicación: *«los PDFs podrían estar desactualizados
  respecto a los vídeos»*. **La hipótesis era explícitamente especulativa; queda falsada.**

**Evidencia — la numeración de sección de los 12 decks, extraída de la página 1 de cada uno:**

| Vídeo | Sección | Desfase | | Vídeo | Sección | Desfase |
|---|---|---|---|---|---|---|
| 01 | *(sin numerar)* | — | | 07 | 5. LA RENTABILIDAD | −2 |
| 02 | 2. LOS 3 ESTADOS FINANCIEROS | **0** | | 08 | 6. EL CAPEX | −2 |
| 03 | 2. EL BALANCE | **−1** | | 09 | 7. EL FREE CASH FLOW | −2 |
| 04 | 3. LOS ESTADOS DE FLUJOS DE CAJA | **−1** | | 10 | 8. EL MOAT | −2 |
| 05 | 3. EL INFORME FINACIERO 10Q | −2 | | 11 | 9. EL EQUIPO DIRECTIVO | −2 |
| 06 | 4. LA DEUDA Y LA CAJA | −2 | | 12 | 10. MÚLTIPLOS DE VALORACIÓN | −2 |

**Dos hallazgos que cierran el asunto:**

1. **El desfase NO es constante: es 0, −1, −1, −2, −2, −2… Crece y luego se estabiliza.** D-19 lo
   llamó *«−2 consistente»* porque muestreó **solo los vídeos 6 y 10** — **ambos en la cola plana**.
   Dos muestras del tramo llano de una función escalonada.
2. **La hipótesis de los «2 vídeos añadidos al inicio» predice un desfase −2 CONSTANTE**, es decir
   vídeo 02 → sección 0, vídeo 03 → sección 1, vídeo 04 → sección 2. **La realidad es 2, 2 y 3.**
   **La hipótesis falla en los vídeos 02, 03 y 04**; solo acierta del 05 al 12, que es justamente
   donde el escalón ya se ha estabilizado.

**Explicación real, y es benigna:** **el deck es UN ÚNICO documento con 10 secciones numeradas,
repartido en 12 vídeos.** Dos secciones abarcan dos vídeos cada una:
- **02 + 03 comparten la sección 2** (los 3 estados financieros / el balance) → primer escalón
- **04 + 05 comparten la sección 3** (flujos de caja / el informe 10Q) → segundo escalón

Los dos escalones acumulan −2, y de ahí en adelante el desfase se congela. **El corte en vídeos no
coincide con el corte en secciones. Eso es todo.**

**Corroboración independiente:** `[PDF 07, p.7]` trae series de precio de Novo Nordisk y Moderna con
datos hasta **~mediados de 2025** — el deck está **al día del vídeo**, no es material antiguo.

**Consecuencias:**
- **Los PDFs NO están desactualizados.** El desfase no era evidencia de nada. **Refuerza D-64**: el
  PDF es la capa visual del mismo momento, no un borrador de otra época.
- ⚠️ **La jerarquía voz > PDF NO cambia.** Que el PDF esté al día **no lo eleva por encima de la
  voz**: cuando chocan, **sigue ganando la voz**, y la discrepancia se registra sin resolverla
  (RD-1). El piloto encontró **17 erratas en 3 vídeos** — las capas chocan, y mucho.

**Alineación de `CLAUDE.md` (solo los dos puntos que descansaban en D-19):**
- **§9 (riesgos vivos):** retirado *«Los PDFs pueden estar desactualizados respecto a los vídeos
  (D-19: …sugiere edición anterior del curso)»*. En su lugar, el riesgo **real** que sí queda vivo:
  las dos capas **chocan**, y cuando chocan manda la voz y la discrepancia se **registra**.
- **§3 (clases de procedencia):** `[PDF]` dejaba de encajar como *«Aparece en el material escrito»*.
  Ahora: *«Lo que el experto **muestra en pantalla**: el deck del vídeo, no un documento escrito
  aparte (D-64)»*, con **«CEDE ante `[VÍDEO]` cuando chocan»** explícito en la columna de fuente.

*Incidencia menor anotada, no accionada:* el deck del vídeo 05 se titula «EL INFORME **FINACIERO
10Q**» (errata «FINACIERO») mientras el slug del proyecto es `05_informe_10k`. **10Q ≠ 10K.** Para la
ingesta del módulo 05.

### Cuestiones abiertas registradas (aparcadas por decisión del usuario — NO se tocan)
- **nº9 · Los 3 campos procedimentales de D-51 no tienen casa por-ficha.** *Rol en el análisis* ·
  *Momento de evaluación* · *Criterio de parada* no existen en los moldes nuevos (D-63). El material
  procedimental tiene destino (`capa_decision.md`, D-61), pero es **un documento único y el rol es
  por-ficha**: un `[HUECO]` como *«¿el ROIC >15% es eliminatorio o condicionante?»* no tiene dónde
  vivir. Consecuencia conocida de que el procedimiento salió de las fichas. **NO se resuelve ahora.**
- **nº10 · La «tasa de error de la fuente» no calibra la autoridad del curso.** §5 la quiere como
  *«evidencia dura para calibrar cuánta autoridad merece el curso»*. Pero **mide la fuente Y el
  método**: con la misma fuente dio **0 → 9 → 17** según el instrumento (v1 sin PDF · v2 con PDF y 1
  tipo de errata · v3 con 4 tipos), y **no hay clase de comparación** — ningún otro curso medido con
  este instrumento. Un número sin comparación no calibra autoridad; lo que sí hace es decir **qué
  tipos de defecto** tiene esta fuente. **Corrección conceptual válida pero no bloquea. §5 NO se
  reformula en esta sesión.**

**Resumen:** cerrada **D-19** (D-65): el desfase de numeración **no** indica PDFs desactualizados —
el deck es un único documento de 10 secciones repartido en 12 vídeos, y los vídeos 02+03 y 04+05
comparten sección, lo que produce un escalón acumulado de −2 a partir del vídeo 05. La hipótesis
original («2 vídeos añadidos al inicio») **falla en los vídeos 02, 03 y 04**; parecía correcta porque
D-19 solo muestreó el 6 y el 10, ambos en la cola plana. Alineados los dos puntos de `CLAUDE.md` que
descansaban en D-19 — **§9** y **§3** — con la jerarquía **voz > PDF intacta**. Registradas, sin
tocar, las cuestiones abiertas **nº9** (campos procedimentales sin casa por-ficha) y **nº10** (la tasa
de error mide fuente+método).

---

## [2026-07-17] rd1 | Reescritura de la REDACCIÓN de RD-1 (no de su intención)

### D-67 · [CORREGIDO] RD-1 reescrita — origen cerrado y fiabilidad por tipo de fuente
**Estado:** RATIFICADA — supersede la **REDACCIÓN** de RD-1 y de D-14. **NO su intención.**

- **Problema:** la letra de RD-1 prohibía lo que el propio piloto hace. Decía *«Ningún valor numérico
  … puede originarse en un LLM leyendo **un PDF**»*, pero las fichas toman el umbral `13-15 %` de
  `[PDF 07, p.3]` — y eso es correcto. **D-14**, que reformuló RD-1, acota a **filings** (*«los
  números del 10-K ya existen en XBRL vía EDGAR»*): es una regla sobre **datos de empresa**, no sobre
  el deck del curso. La distinción que el piloto aplica de facto **no estaba escrita en ninguna
  parte**.
- **Urgencia:** los módulos **13-16 son los más densos en umbrales de deck**. Un escritor que
  obedeciera la letra vieja **se negaría a tomarlos**. Era el punto con más riesgo del escalado.

**La redacción nueva dice tres cosas:**
1. **Origen cerrado** — toda la información procede **exclusivamente** de `raw/`. El LLM **nunca
   busca en internet ni aporta datos de su propio conocimiento**. Si falta, es `[HUECO]`.
2. **La lectura tiene grados** — **texto legible** (`.srt`, capa de texto de un deck) es **FUENTE
   PLENA**, misma validez que la transcripción; **imagen que hay que interpretar** (capturas,
   gráficos, páginas sin capa de texto) es **FUENTE CON CAUTELA**: ninguna cifra a ciegas, se eleva
   para verificación humana.
3. **Datos de empresa** — entran **solo si el concepto no se entiende sin ellos**. Si solo ilustran,
   van a `wiki/ejemplos/` marcados PEDAGOGÍA (D-49).

**Alcance declarado:** rige la **CONSTRUCCIÓN**, no el uso. Las capas de uso (D-59, aparcadas) sí
podrán consultar fuentes externas en su momento.

**Qué relaja, qué aprieta y qué conserva — dicho explícitamente por tratarse de una regla dura:**
- **RELAJA:** permite extraer cifras de la **capa de texto** de un PDF. Justificado: extraer de texto
  digital **no es transcribir**; el modo de fallo silencioso que RD-1 teme es de la **visión**.
- **APRIETA:** añade dos prohibiciones que la letra vieja **no decía** — (a) nunca buscar en internet
  ni aportar conocimiento propio, que no estaba escrito en ninguna parte; (b) ninguna cifra a ciegas
  desde una imagen, con elevación obligatoria.
- **CONSERVA:** la intención original intacta — que ningún número entre al cerebro por una vía en la
  que el error sea **invisible**.

**Traza:** el texto anterior de RD-1 queda en el histórico de git y citado en esta entrada. **D-14 no
se anula:** su distinción numérico/narrativo sigue vigente y ahora está **escrita en la propia regla**
en vez de vivir solo en el log.

**Resumen:** reescrita la redacción de RD-1 (D-67) para que diga lo que la regla siempre quiso decir:
origen cerrado durante la construcción, texto legible como fuente plena, imagen con cautela y
elevación, y datos de empresa solo si son definicionales. Intención intacta.

---

## [2026-07-17] descontaminacion | Descontaminación aplicada, revalidada contra el corpus completo

### D-69 · [DECISIÓN] Descontaminación: se archiva lo que el corpus completo confirma innecesario
**Estado:** RATIFICADA — supersede **D-02** (2ª capa), **D-03** y **D-05**

- **Contexto:** `auditoria_descontaminacion.pdf` propuso archivar seis piezas, pero se escribió con
  **3 decks leídos**. **Cada propuesta se ha revalidado contra los 13**, y **ninguna resultó
  necesaria** a la luz del corpus completo.

| Pieza | Revalidación con los 13 decks | Acción |
|---|---|---|
| `inventario_atomico.md` | **Huérfano**: dice derivarse del campo «Inputs atómicos», y los moldes v4 **no tienen ese campo** (`grep -ci "atómic"` = **0**). Nada lo alimenta. Su destino —el embudo— está **diferido** (D-10) y **aparcado** (D-59) | → `wiki/_archivo/`, **congelado**. Se descongela si la Capa 2 se activa |
| `sondeo_procedimental.md` | Cubría 14/15/17 **parcialmente**; la lectura virgen los cubre **enteros**; **D-60 cerró la pregunta** que sondeaba | → `wiki/_archivo/`, marcado ⚠️ **CONSULTABLE al ingerir 14/15/17**: su clasificación ORDEN/DESCARTE/RELACIÓN/RANGO/FASE es materia prima aprovechable. **No muerto** |
| **§6.0** ingesta cero | Ejecutada; `fuentes.md` cataloga `raw/externo/` correctamente | → **ARCHIVADA** en `CLAUDE.md`; el protocolo queda en el histórico de git |

**Decisiones supersedidas — con traza, nunca borradas:**

- **D-02 · Plantilla de dos capas (Ficha + Inventario Atómico)** → ⚠️ **su SEGUNDA capa queda sin
  objeto.** La primera (la ficha) sigue viva y es hoy el sistema de seis moldes. El Inventario
  Atómico no lo alimenta nada.
- **D-03 · Separación Fase A (transcripción) / Fase B (crítica)** → ⛔ **VOCABULARIO MUERTO.** «Fase
  A/B» no aparece en `CLAUDE.md`, ni en ningún molde v4, ni en ninguna ficha. **D-04 ya la disolvió**
  al declarar que «la Fase A deja de ser transcripción pura → transcripción + auditoría».
- **D-05 · Las notas personales no son insumo del inventario** → 🔀 **FUSIONADA en D-24**, que la
  superó en alcance: las notas dejan de ser insumo **del cerebro**, no solo del inventario. Dos
  decisiones vivas para lo mismo.

**Nada se borra.** Los tres documentos siguen en `wiki/_archivo/` con su README explicando qué los
superó, y las tres decisiones conservan su entrada original en este log.

**Resumen:** aplicada la descontaminación (D-69) tras **revalidarla contra el corpus completo**:
`inventario_atomico.md` congelado, `sondeo_procedimental.md` archivado pero **consultable**, §6.0
archivada. Supersedidas D-02 (2ª capa), D-03 y D-05, con traza. **Ninguna de las seis piezas resultó
necesaria a la luz de los 13 decks** — la auditoría original se sostiene entera.

---

## [2026-07-17] reorganizacion | Reorganización del repositorio, separación método/ejemplo y cláusula de campos opcionales

### D-66 · [DECISIÓN] Reorganización del repositorio en clases + fiabilidad de lectura de las fuentes
**Estado:** RATIFICADA — supersede la **cláusula de ubicación** de D-63 (su contenido sigue vigente)

- **Problema:** la ubicación de un fichero **no decía qué era**. Los moldes definitivos vivían en
  `wiki/piloto/`, las fichas provisionales en `wiki/curso/`, y documentos superados convivían con
  documentos vivos en la raíz de `wiki/`.
- **Decisión — cuatro clases, cuatro sitios:**
  - **`wiki/_estructura/`** — cómo se construye el cerebro (`moldes.md`, `radiografia.md`). No es
    contenido del curso: **no le aplica RD-3**.
  - **`wiki/curso/`** — el método del experto, **bajo RD-3**. Recibe `capa_decision.md` y
    `mapa_tematico.md`, que son contenido suyo. **Sin ninguna ficha**: es la verdad.
  - **`wiki/ejemplos/`** — PEDAGOGÍA, separada del método (ver D-68).
  - **`wiki/_provisional/`** — las 8 fichas con molde superado, con un README que detalla **una por
    una** qué las invalida.
  - **`wiki/_archivo/`** — superado con traza.
- **21 movimientos, todos `git mv`**, detectados como `R100` (renombrado puro): **el historial de
  cada fichero se conserva**. **No se ha renombrado nada** — los wikilinks se resuelven por nombre de
  archivo, así que mover es seguro y renombrar los habría roto.

**Fiabilidad de lectura (RD-1 §2) — declarada en tres sitios:**
1. Un `README.md` en **cada subcarpeta de `raw/`** con su clase.
2. Una sección nueva en **`fuentes.md`** con la tabla completa y sus marcadores.
3. Los **marcadores de cita** en `CLAUDE.md` §3.

> **Hallazgo que obligó al diseño en dos capas: los decks son MIXTOS.** La fiabilidad **no es
> propiedad del fichero sino de cada cita**. Verificado sobre `[PDF 07]`: p.1-4 y p.7 tienen 423-843
> caracteres de texto (**PLENA**); **p.5 y p.6 tienen 41** — son gráficos (**CAUTELA**) — y son
> **justo de donde el experto lee cifras en voz alta**. Por eso mover carpetas no bastaba.

**Además:** `06_whisper_DESCARTADO.srt/.txt` sale de `raw/transcript/` a `_archivo/whisper/`. Era el
producto de una **herramienta rechazada** (D-45) conviviendo con las fuentes canónicas, donde un
escritor podría leerlo como fuente.

### D-68 · [DECISIÓN] Separación método / ejemplo: `wiki/ejemplos/`
**Estado:** RATIFICADA — amplía D-49, que declaraba la separación pero **no la ubicaba**

- Los casos concretos del experto viven **fuera del método**. Quien consulte el método **no se los
  encuentra revueltos**.
- **Los moldes 1, 2, 4 y 6** apuntan desde *Demostración del experto* con un **puntero + una línea de
  resumen**.
- ⚠️ **Excepción — MOLDE 3:** su campo *Ejemplares* **se queda DENTRO de la ficha**. Ahí la empresa
  **es parte de la definición de la categoría** (ASML define qué es un moat-monopolio, Ferrari qué es
  exclusividad de lujo). Sacarlos rompería la taxonomía: **el tipo no se entiende sin su ejemplar**.
- **Criterio de entrada al método (RD-1 §3):** un dato de empresa entra **solo si el concepto no se
  entiende sin él**.

> **Comprobación sobre el corpus completo: NO hay ni un solo dato de empresa que sea definicional.**
> ASML 780 $, Meta 182/276, Novo/Moderna, AMD/Intel, IDEXX — **todos ilustran** conceptos ya
> definidos sin ellos. Lo único cercano son las **analogías inventadas** (la hipoteca, la casa con
> caja fuerte, `[VÍDEO 06]`), que **no son datos de empresa** y se quedan en la ficha.
> **La regla es limpia de aplicar: el método queda sin una sola cifra de compañía.**

### D-70 · [DECISIÓN] Un campo OPCIONAL nunca significa descartar información
**Estado:** RATIFICADA — complemento simétrico de RD-4

- **Si el material trae contenido que corresponde a un campo —obligatorio u opcional—, ese contenido
  SE AÑADE SIEMPRE.**
- «Opcional» significa que **la casilla no se fuerza vacía** cuando el vídeo no trata el aspecto.
  **No** significa que la información se omita.

| Regla | Qué prohíbe | Contra qué protege |
|---|---|---|
| **RD-4** | **Rellenar** lo que no hay | La invención |
| **D-70** | **Omitir** lo que sí hay | La pérdida |

**Motivo:** sin ella, «opcional» se lee como «prescindible», y un escritor con prisa deja fuera
material que el vídeo sí trae. **Las dos juntas cierran el círculo: ni se inventa ni se pierde.**

**Resumen:** reorganizado el repositorio en cuatro clases con la fiabilidad de lectura declarada en
`raw/`, `fuentes.md` y `CLAUDE.md` (D-66); separados los ejemplos del método en `wiki/ejemplos/`, con
punteros desde los moldes 1/2/4/6 y la excepción razonada del molde 3 (D-68); y añadida la cláusula
de campos opcionales como complemento simétrico de RD-4 (D-70).

## [2026-07-19] arrastre | Regla de arrastre para erratas, formalizada y afinada (D-71)

**Estado:** RATIFICADA

**Contexto.** Desde `08-E1` (2026-07-19) veníamos aplicando un criterio informal —"si algo
futuro depende explícitamente de esta errata, se eleva de inmediato en vez de acumularse"— pero
nunca se escribió como regla en `CLAUDE.md`. Al cerrar `09-E1` (el FCF define si resta intereses
o no; el deck se contradice entre su p.2 y su p.3) se detectó que el criterio original —"¿alguien
la cita explícitamente hacia adelante?"— no bastaba: nadie cita `09-E1` por su nombre, y sin
embargo el FCF es la base explícita del DCF (`[09, 06:00]`). Hacía falta un segundo criterio.

**Decisión — dos criterios, no uno.** Una errata `ARRASTRA` si se cumple (a) el experto la cita
explícitamente hacia adelante (caso `08-E1`, capex→FCF ajustado), **o** (b) la errata afecta a la
definición conceptual de algo que otros conceptos del corpus dan por sentado, aunque nadie la cite
explícitamente (caso `09-E1`, el FCF como cimiento del DCF). El escritor evalúa (b) con la
pregunta: *«¿esta definición es un cimiento de otros conceptos del corpus?»*. Registrada en
`CLAUDE.md` §5, junto a la jerarquía voz>PDF.

**Por qué no es automatismo.** El criterio (b) exige juicio, no una lista de casillas — no toda
errata sobre una definición arrastra, solo cuando esa definición sostiene otras piezas del método.
El escritor deja el razonamiento por escrito al marcar `¿Arrastra?`, para que el dictamen humano
pueda auditarlo.

**Lo que NO cambia.** El escritor sigue sin dictaminar qué versión es correcta — la regla decide
**cuándo** se eleva una errata, no **qué** dice el cuerpo mientras tanto (eso lo sigue decidiendo
la jerarquía voz>PDF ya existente).

**Deuda reconocida, no resuelta aquí.** Esta regla —y su antecesora informal, y la «regla
permanente de cifras» (método vs. ejemplo, 2026-07-18)— llevaban operando varias sesiones sin
quedar registradas como decisión. Este `log.md` no tiene entradas entre el `2026-07-17` (D-70) y
esta, a pesar de que en ese tramo se ingirieron y cerraron los vídeos 01 a 09 con numerosos
dictámenes del usuario. **No se han registrado retroactivamente** — sería una tarea aparte, no
pedida — pero queda anotado aquí para que la próxima sesión sepa que el hueco existe.

## [2026-07-19] equivalencias | Campo *Equivalencia técnica*: el término estándar, marcado como externo (D-72)

**Estado:** RATIFICADA

**Contexto.** Al cerrar `09-E1` (2026-07-19) se ordenó **retirar del cuerpo** de
`free_cash_flow.md` los términos `FCFF`/`FCFE`: eran jerga del escritor, el experto **nunca** los
dice, y atribuírselos violaba RD-2. La retirada fue correcta **en cuanto a la atribución** — pero
se ejecutó como **borrado total**, y eso tuvo un coste que se hizo visible después: el cerebro es
un **copiloto de consulta** (D-58), el usuario le trae datos de empresas reales, y **esos datos
llegan en terminología estándar**. Un screener dice «Total Debt»; un 10-K dice «Share-based
compensation»; la literatura dice «FCFE». Sin esa correspondencia registrada en alguna parte, el
cerebro **no reconoce el dato que le están enseñando**.

**Decisión — separar ATRIBUCIÓN de CORRESPONDENCIA.** Son dos cosas distintas y el borrado total
las confundió:

| | Regla |
|---|---|
| **El cuerpo de la ficha** | Usa **las palabras del experto**. No se le atribuye ninguna etiqueta técnica que él no diga. **Esto no cambia** — es lo que `09-E1` acertó |
| **Un bloque nuevo y aparte** | `## Equivalencia técnica` registra el **término estándar de la industria**, marcado `[COMPLETADO-EST]` (pilar b: práctica institucional documentada), **explícitamente NO palabra del experto** |

**Dónde va.** Campo nuevo en los moldes **1 (métrica), 2 (estado), 3 (cualitativo) y 4
(múltiplo)** — `moldes.md` **v6**. **NO** en el molde 5 (sistemas de decisión personales del
experto: no hay término estándar que emparejar, y añadir la casilla invitaría a inventarlo) **ni**
en el molde 6 (el marco ya define su vocabulario en su campo 2, y el 10-K ya usa nomenclatura
estándar). **Opcional en los cuatro**: `AUSENTE` cuando no hay equivalencia, o cuando el experto
**ya usa** el término estándar — que entonces no es equivalencia, es su palabra.

**Las tres prohibiciones** (en `moldes.md` §Equivalencia técnica): no se atribuye jamás al experto ·
no se registra una equivalencia dudosa (`AUSENTE` es la respuesta correcta) · no sustituye al
método, solo dice cómo se llama fuera.

**Qué le hace a las reglas duras — dicho, no escondido.** **RD-1 queda intacta en su intención**:
esto no mete conocimiento externo *como método del experto*, y usa el canal que el proyecto ya
tenía abierto para lo externo (`[COMPLETADO-EST]`, `CLAUDE.md` §3) en vez de abrir uno nuevo.
**Pero sí toca la prueba de fuego de RD-3** —*«borrar `complemento/` entero debe devolver el curso
íntegro»*—, porque por primera vez hay contenido externo **dentro de `curso/`**. La prueba se
conserva reformulada: **borrar todos los bloques `## Equivalencia técnica` debe devolver el curso
íntegro y coherente**. Por eso el campo es un bloque delimitado y extraíble de un corte, y no
frases externas repartidas por los demás campos.

**Supersede** la parte de la instrucción de cierre de `09-E1` que ordenaba retirar FCFF/FCFE **del
todo**. No se borra esa instrucción ni se reescribe su entrada: se registra que **su parte de
atribución sigue vigente** y **su parte de borrado total queda superada** por la ubicación
correcta. La equivalencia FCF→FCFE/FCFF vuelve, en el campo nuevo, marcada como externa.

**Aplicado en esta sesión a 5 fichas** (no una pasada exhaustiva — decisión del usuario: solo
donde sea obvia y de alto valor; el resto se completa al ingerir): `free_cash_flow` (FCFE/FCFF) ·
`equipo_directivo` (insider ownership · SBC · ⭐ *capital* allocation) · `balance_general` (Current
Ratio, D/E, y una equivalencia **rechazada** por dudosa) · `deuda_financiera` (Total Debt ≠ Total
Liabilities) · `cuenta_de_resultados` (la cascada, y que **EBITDA no es una línea del 10-K**).

**Resumen:** cerrado el vídeo 11 con el dictamen de `11-E1` (es «Stock **Based** Compensation»;
«Basic» es lapsus compartido por voz y deck, desempatado por la propia voz 16 segundos antes), y
formalizado el campo *Equivalencia técnica* como D-72, con `moldes.md` en v6 y las cinco fichas de
alto valor ya rellenas.

## [2026-07-19] erratas | Regla afinada: cuándo se ELEVA y cuándo se RESUELVE (D-73)

**Estado:** RATIFICADA

**Contexto.** Hasta aquí el schema decía, sin matiz: *«SE REGISTRAN, NO SE RESUELVEN. El escritor
no dictamina en ningún tipo»* (`CLAUDE.md` §5, `moldes.md`). La razón era buena —evitar que el
escritor colara criterio propio, RD-1— pero producía un efecto no buscado: **elevar al usuario
erratas que la propia fuente ya resolvía**. El caso que lo hizo evidente fue `12-E1`: la
transcripción dice «Novo parece más barata, mientras que **Lilly está más barata**» —las dos no
pueden serlo— y **el propio deck traía los números que lo desmentían** (Lilly 36,62 frente a una
media de 29,22: está **cara**). No hacía falta el criterio de nadie; hacía falta leer la fuente
entera.

**Decisión — el umbral de elevación cambia.** No es «hay una errata», es **«hay una errata que NO
puedo resolver sin el usuario»**:

| Situación | Qué hace el escritor |
|---|---|
| Otra parte del corpus la desambigua **sin margen de duda** | ✅ **CORRIGE** + estado `DICTAMINADO POR EVIDENCIA`, **citando qué evidencia lo resuelve** |
| Depende del **criterio** del usuario o de algo que solo él tiene (su escucha del audio, su juicio como inversor, una contradicción que el corpus no cierra) | 🔴 **ELEVA** |
| **Duda real**: el deck no zanja · podría ser interpretación y no error · **toca método y no ejemplo** | 🔴 **ELEVA** |

⚖️ **Regla de oro: ante la duda, eleva; ante evidencia inequívoca, corrige.**

**Por qué NO viola RD-1.** «Resolver con evidencia del corpus» **no es conocimiento externo**: es
usar otra parte de la propia fuente. La prohibición que sigue intacta es la de **corregir con
conocimiento del LLM** — si el corpus no lo zanja, el escritor no lo zanja. El estado nuevo obliga
a **citar el localizador de la evidencia**: sin eso, el dictamen no vale y la entrada vuelve a
`PENDIENTE`.

**Efecto sobre el recuento.** La columna «Dictaminadas» de `erratas.md` deja de ser homogénea:
mezcla `DICTAMINADO` (lo resolvió el usuario) y `DICTAMINADO POR EVIDENCIA` (lo resolvió el
escritor citando el corpus). Queda anotado en la propia tabla para que nadie lea las dos cosas como
una sola.

**Aplicado el mismo día al módulo 12, su primer banco de pruebas:** de cuatro erratas, **tres se
corrigieron por evidencia** (`12-E1` Lilly cara · `12-E2` el rótulo «NVO» que era LLY · `12-E4`
Idex→IDEXX) y **una quedó sin dictamen** (`12-E3`, el 22,9 vs 22,29 de Walmart) precisamente porque
su polo B **se lee de una imagen** (`CAUTELA`) y por tanto la evidencia **no es inequívoca**.
**Ninguna se elevó.** Ese `12-E3` es la demostración de que el límite de la regla muerde: la regla
no es «corrige lo que puedas», es «corrige lo que la fuente cierra sin duda».

**Resumen:** cerrado el vídeo 12 —estreno del molde 4, dos fichas (`per`, `ev_fcf`) nacidas
`parcial` + `transversal` por la convención del bloque de múltiplos—, y formalizada como D-73 la
regla afinada de elevación de erratas, con `CLAUDE.md` §5 y `moldes.md` (v7) actualizados y el
estado nuevo `DICTAMINADO POR EVIDENCIA` en uso.

## [2026-07-19] moldes | Campo *Grado de formalización declarado* en el molde 6 (D-74)

**Estado:** RATIFICADA

**Contexto.** El vídeo 13 trae el pasaje epistémicamente más importante del corpus hasta ahora: el
experto declara que **su propia disciplina es tan subjetiva como el trading** —*«si preguntabas a 20
analistas distintos, obtenías 20 resultados distintos… es igual de subjetivo»* `[13, 01:59–02:29]`—
y **el molde 6 no tenía dónde alojarlo**. Se aparcó como parche dentro del campo 1 (Definición del
marco), que no es su sitio: eso no define qué es el marco, define **cuánta autoridad se le
atribuye**.

**Lo llamativo es que el campo ya existía… en otro molde.** El molde 5 lo lleva como campo 7
(*Grado de formalización declarado*), y `moldes.md` **ya citaba esta misma frase del vídeo 13** al
justificarlo. El diseño lo había visto y lo había puesto en un solo sitio.

**Decisión.** Se añade **campo 10 · Grado de formalización declarado** al molde 6, opcional,
`AUSENTE` cuando el vídeo no declara estatuto epistémico. `moldes.md` → **v8**.

**Criterio de a qué moldes les toca** *(y por qué no a todos)*: lo llevan **los dos moldes que
describen «el continente» —5 (sistemas de decisión) y 6 (marco)—** y no los que describen un objeto
concreto (1-4). Un ratio no tiene estatuto epistémico; un método sí.

**Ubicación — se sigue el precedente de D-72.** Va como **última casilla de contenido, antes del
bloque de erratas**, igual que se hizo con *Equivalencia técnica*. Motivo práctico: **no renumerar
campos ya referenciados** por otras fichas (`marco_analisis_fundamental` campo 7, `informe_10k`
campo 8…). Es menos elegante semánticamente que ponerlo junto al campo 7 y **se acepta a
conciencia**: romper referencias cruzadas cuesta más que un orden imperfecto.

**Por qué importa y no es cosmético.** Sin este campo el cerebro presentaría el método **con más
autoridad de la que su propio autor le atribuye**. Es exactamente el mismo problema que el molde 5
resolvía para el vídeo 18 (que niega usar una tabla formal y diez minutos después entrega una).

**En la misma sesión: `13-E1` dictaminada.** Las tres cuantificaciones del alcance (30-40 %,
40-70 %, 20/80) **no eran una contradicción sino un gradiente compatible** — la misma idea dicha de
tres formas. **Estándar operativo fijado por el usuario: 40-70 %.** ⚖️ La errata se había elevado
bajo D-73 (tocaba método, sin deck que desambiguara, podía ser interpretación) y el dictamen
**confirma que elevarla fue lo correcto**: corregirla por cuenta propia habría inventado una
contradicción que no existía. `marco_analisis_fundamental` campo 7 y `capa_decision` §2.2 quedan
corregidos para registrar las tres como gradiente, no solo el 40-70 % como si fuera la única.

**Resumen:** cerrado el vídeo 13 (molde 6, tercera instancia — marco de la fase de valoración,
primer vídeo escrutado sin deck), dictaminada `13-E1` como gradiente con estándar operativo 40-70 %,
y añadido el campo *Grado de formalización declarado* al molde 6 (D-74, `moldes.md` v8).

## [2026-07-19] moldes | Cuarto eje de comparación (D-75) y política de enriquecimiento (D-76)

**Estado:** RATIFICADAS

### D-75 · El cuarto eje de comparación, formalizado con N=2

`moldes.md` campo 5 del molde 4 tenía **tres ejes**, todos del deck `[PDF 12, p.1]`: contra el
histórico propio, contra competidoras, contra el sector. **Los tres son de corte transversal.** Al
ingerir el vídeo 12 apareció un cuarto, **solo en voz y de naturaleza distinta —longitudinal—**:
comparar la trayectoria del múltiplo con la del precio y **leer la divergencia como oportunidad**.
Se dejó como **observación, no como cambio de molde**, por ser N=1.

**Al ingerir el vídeo 15 reapareció**, con otro múltiplo y las mismas palabras de fondo:

| Vídeo | Múltiplo | Cita |
|---|---|---|
| 12 | EV/FCF | «observas **divergencias entre el múltiplo y la cotización** porque eso nos puede mostrar que existen oportunidades» `[12, 06:24]` |
| 15 | P/FCF | «cuando los números dicen una cosa y **el precio todavía no se ha enterado**» `[15, 07:35]` |

**Con N=2 se incorpora al molde** (`moldes.md` **v9**). ⚠️ **Solo se aplica donde el experto lo
enuncia** —`ev_fcf` y `p_fcf`—, **no** en `per`, `p_bv` ni `ev_ebitda`. Se marca **aporte
solo-verbal**: ningún deck lo recoge.

> ⚖️ **La disciplina de esperar a N=2 es el punto.** Es la misma que sigue aplicándose a «dos
> umbrales» del ROIC, que **continúa en N=1** y por tanto **sin tocar el molde** — el vídeo 15 trajo
> una escala graduada del PER (<10/10-20/>20), que **no es la misma forma** y no cuenta como segundo
> caso.

### D-76 · Política de enriquecimiento de fichas `completo`

**El problema.** El corpus **no reparte un concepto por un solo vídeo**. El PER vive en el 12, el 15
y el 16; los ratios del balance en el 03 y el 15; el FCF en el 09, el 12 y el 15. Con la lectura
rígida de `completo` —«cerrada»—, el aporte de un vídeo posterior **no tenía dónde entrar**. Y la
alternativa (dejarlo todo `parcial` hasta el vídeo 19) **vaciaría el estado de significado**.

**Decisión.** Una ficha `completo` lo está **respecto a los vídeos ingeridos hasta ese momento**,
no para siempre.

| Cuándo | Qué se hace |
|---|---|
| Un vídeo posterior **aporta** | ✅ **SE AÑADE**, citando `[VÍDEO NN]` y dejando visible que es incorporación posterior |
| Un vídeo posterior **contradice** | ⛔ **NO se sobrescribe**: es errata **T2 entre vídeos** → su cauce (D-73) |

**Es sumar, no reescribir** — y la cita del vídeo aportante es obligatoria: sin ella la ficha pierde
procedencia (RD-2). ⚠️ **No relaja RD-3**: enriquecer una ficha de `curso/` sigue necesitando la
aprobación del usuario.

⭐ **Efecto colateral valioso:** con D-76, declarar `completo` deja de ser una apuesta arriesgada.
Por eso `ev_fcf` y `p_fcf` pasan a `completo` en esta misma sesión pese a quedar dos vídeos del
bloque sin leer — si aportan, se añaden.

**Aplicada el mismo día a tres fichas que llevaban tiempo en `completo`**, con lo que el vídeo 15
les traía: `cuenta_de_resultados` campo 4 (**cuatro márgenes con fórmula** — el campo pasa del
desenlace **b** al **a**) · `balance_general` campo 4 (**test ácido** y **ratio de caja**, «el test
más definitivo») · `deuda_neta` campo 3 (**EBIT/intereses** como ratio de cobertura hermano).

### Criterio de ficha propia — confirmado, no ampliado

Los **~13 ratios menores** del vídeo 15 (ROA, ROCE, los cuatro márgenes, los siete de
liquidez/endeudamiento) **quedan en la taxonomía de `mapa_tematico` §1, sin ficha propia**, hasta
que un vídeo los desarrolle con definición **más** al menos un campo sustantivo. **Motivo:** 16
campos × 20 ratios daría fichas con 13 casillas `AUSENTE` — **más andamiaje que contenido**.
⚠️ **El ROA se registra con la fórmula que da el experto** (`EBIT / Activos totales medios`), **sin
marcar errata**: el corpus no la contradice en ninguna parte, y señalarla exigiría conocimiento
externo (RD-1, y el límite de D-73).

**Resumen:** cerrado el vídeo 15 —vídeo de **amplitud**, repartido entre la taxonomía de los cuatro
grupos, tres fichas nuevas (`p_bv`, `ev_ebitda`, `p_fcf`), el completado de `per` y `ev_fcf`, y tres
enriquecimientos— y formalizados el cuarto eje de comparación (D-75) y la política de
enriquecimiento (D-76), con `moldes.md` en **v9**. Se corrigió además que la cabecera de `moldes.md`
seguía en v7 pese a haberse aplicado D-74: **la v8 quedó sin entrada en el historial y se ha añadido
en retrospectiva**.

## [2026-07-19] pausa | Punto de parada del proyecto — límite de uso de sesión

**Estado:** REGISTRO (no es una decisión de método; es una fotografía del punto exacto en que se
interrumpe el trabajo)

**Por qué esta entrada.** La sesión se pausa por límite de uso, no por haber cerrado un vídeo. Para
que la siguiente sesión no tenga que reconstruir el estado leyendo el `git log` y adivinando qué
quedó a medias, se deja aquí la fotografía exacta.

### Commiteado y completo — hasta el vídeo 15

Cola cerrada: **01–09, 11, 12, 13, 15** (el bloque de métricas 06-09 completo desde antes; D-72
equivalencias técnicas; D-73 regla afinada de erratas; D-74 grado de formalización en el molde 6;
D-75 cuarto eje de comparación; D-76 política de enriquecimiento — las cinco aplicadas y
commiteadas). Último commit: `92c20d78211d9c8731200f27221aa9e64a9a8567` («Cierra el vídeo 15…»).

### Vídeo 17 — INGERIDO, SIN COMMITEAR

**En el working tree, tal cual, sin tocar en esta entrada:**
- Nuevos, sin trackear: `wiki/curso/multibagger.md` (molde 5, variante `FILTRO` — **estreno del
  molde 5**) · `wiki/curso/peg.md` (molde 4, `parcial`) · `wiki/ejemplos/ejemplo_17_alphabet.md`.
- Modificados (enriquecimiento D-76, sin commitear): `wiki/curso/capa_decision.md` (§3 — primer
  criterio de parada del corpus) · `wiki/curso/free_cash_flow.md` (campo 13) ·
  `wiki/curso/mapa_tematico.md` (§Genealogía — Peter Lynch).

**Lo que falta antes de cerrar el 17, en orden:**
1. **Dictamen de `17-E1`** — el criterio 3 (free cash flow) del filtro trae un umbral sin referente
   enunciado: «si el FCF es mayor, genial, pero si no llega ni a la mitad…» — ¿mayor/mitad **de
   qué**? Elevada porque toca método y no hay deck que desambigüe. Hoy el criterio queda operable
   solo en su parte direccional (creciente / decreciente).
2. **Decisión sobre la predicción «Conjunción» de `moldes.md`** para la variante `FILTRO` del molde
   5 — la lectura completa del vídeo 17 no encontró una conjunción limpia de los 5 criterios, sino 4
   encadenados + 1 condicional, con la deuda como veto unilateral. Sin decidir si se corrige la
   tabla de variantes.
3. **Decisión sobre añadir el campo *Demostración del experto* al molde 5** — hoy no lo tiene, y el
   recorrido por Alphabet quedó enlazado desde el campo 3 (Entrada requerida), que no es su sitio.

### En pausa por puntuación manual pendiente del usuario

**Vídeo 10** (moat) — ya ingerido y con ficha escrita (`wiki/curso/moat.md`, sin trackear), pendiente
de **reingesta completa** sobre el `.srt` puntuado a mano. **Vídeos 14 y 16** — no ingeridos todavía,
bloqueados por la misma razón (transcripción sin puntuar). Ninguno de los tres se ha tocado en esta
sesión.

### Sin ingerir — cola limpia

**Vídeos 18 y 19.** Cierran el bloque del molde 5 (variantes `SCORING` y `REGLAS`).

**Resumen para la próxima sesión: el siguiente paso es dictaminar `17-E1` y cerrar el vídeo 17.**

## [2026-07-19] cierre 17 | Estreno del molde 5; dictamen de 17-E1; dos ajustes al molde (D-77)

**Estado:** RATIFICADA

**Contexto.** Se retoma tras la pausa del checkpoint anterior. Se cierra el vídeo 17 con las tres
decisiones del usuario.

**17-E1 · DICTAMINADA — el referente es el BENEFICIO NETO.** El criterio 3 del filtro (free cash
flow) comparaba el FCF contra un sujeto que la transcripción no enunciaba: «si el FCF es mayor,
genial, pero si no llega ni a la mitad…». El usuario lo resuelve **contra el audio** (D-46): FCF >
beneficio neto → buena señal; FCF < ½ del beneficio neto → problema. **El criterio 3 pasa de
operable-solo-en-dirección a plenamente operable.** ⚖️ **Es el reverso exacto de `12-E1`**: aquélla
se corrigió *por evidencia* (el deck la desambiguaba sola); ésta *se elevó* porque nada en el texto
la desambiguaba y su resolución dependía de la escucha del audio, que solo tiene el usuario. Las dos
son T4; el tratamiento distinto **es lo que D-73 prescribe**. Coherente con la tesis del vídeo 09
(el FCF como beneficio más fiable que el contable): el criterio se convierte en un **test de
conversión** beneficio→caja.

**Molde 5, ajuste (a) · corrección de la predicción de agregación.** La tabla de variantes de
`moldes.md` anticipaba «**Conjunción**» para la variante `FILTRO`. La lectura completa del vídeo 17
lo **desmiente**: el experto **nunca enuncia una regla de agregación**. Lo que hay es **4 criterios
encadenados + 1 condicional** (dividendos, solo empresas maduras) **+ 1 con veto unilateral** (deuda
alta → «no lo dudes, pasa a la siguiente»). Se corrige la predicción para que describa **lo
observado, no lo previsto en diseño**, y se mantiene el `[HUECO]` explícito de «¿qué pasa si cumple
4 de 5?» — el experto no lo dice y **no se deduce**. Las filas del 18 y el 19 siguen marcadas como
predicción, sin ingerir.

**Molde 5, ajuste (b) · D-77 · campo *Demostración del experto*.** El molde 5 era **el único de los
seis sin casilla para un caso concreto** (los 1/2/4/6 tienen *Demostración*; el 3, *Ejemplares*; el
5, nada). El recorrido por Alphabet del vídeo 17 —con dos cifras reales— quedaba colgado del campo 3
(Entrada requerida), que no es su sitio. Se añade como **campo 12** (puntero a `ejemplos/`,
opcional), y `ejemplo_17_alphabet` se reubica ahí. `moldes.md` → **v10**.

> ⭐ **El estreno del molde 5 dejó dos hallazgos de método más, ya en las fichas:** (1) **el primer
> criterio de parada del corpus** —«deuda descontrolada → pasa a la siguiente»—, que **enriquece
> `capa_decision` §3** (D-76) y hace caer la afirmación absoluta «ni una parada, ni una», **sin
> tocar** la minimalidad del protocolo (D-60); (2) **la primera banda con techo** —crecer >25 % del
> BPA es señal de alarma, no de excelencia—, forma distinta del patrón «dos umbrales», que **sigue
> en N=1** y sin tocar el molde.

**Enriquecimientos aplicados en esta ingesta (D-76):** `capa_decision` §3 (criterio de parada) ·
`free_cash_flow` campo 13 (la métrica *apalancada* que el experto usa en TIKR, coherente con
`09-E1`) · `mapa_tematico` §Genealogía (Peter Lynch, tercera atribución externa del corpus, y como
las otras dos, a un inversor y no a literatura académica).

**Resumen:** cerrado el vídeo 17 —estreno del molde 5, variante `FILTRO`, dos fichas nuevas
(`multibagger`, `peg`) y un ejemplo—, dictaminada `17-E1` (referente = beneficio neto), corregida la
predicción de agregación del FILTRO y añadido el campo *Demostración del experto* (D-77). `moldes.md`
en **v10**. **Los seis moldes tienen ya al menos una ficha real.**

## [2026-07-19] fuentes | Transcripciones puntuadas a mano (10, 14, 16) — resuelto el defecto diagnosticado

**Estado:** REGISTRO (corrección de fuente, no de método)

**Contexto.** El diagnóstico de puntuación (2026-07-19) encontró **tres transcripciones degradadas**,
prácticamente sin signos: **10** (ratio 0,087/100 palabras), **16** (0,110) y **14** (0,233), frente
a un suelo de 2,63 en el resto del corpus. Se decidió **no ingerirlas así** (el 10 quedó en pausa
tras su ingesta piloto; 14 y 16 se saltaron en la cola).

**Qué pasó.** El usuario ha **corregido las tres a mano contra el audio** en Subtitle Edit (flujo
canónico D-46) y ha sustituido los `.srt` (y sus `.txt` derivados) en `raw/transcript/`. La
puntuación de prosa sube en los tres —10: +50 marcas · 14: +78 · 16: +432— y las correcciones
incluyen arreglos que casan con dictámenes ya registrados (p. ej. «activos **tangibles**» →
«**intangibles**» en el vídeo 10, que es la errata `10-E1`).

**Commit de estas fuentes:** *(hash en el informe de la sesión — commit separado del cierre del
vídeo 17, para no mezclar corrección de fuente con ingesta).*

**Qué habilita — y qué NO se ha hecho todavía:**
- ✅ **Vídeo 10** — la **reingesta** completa sobre el `.srt` puntuado ya es posible. La ficha
  piloto actual (`wiki/curso/moat.md`, sin commitear) se rehará sobre esta versión. **No se ha
  reingerido en esta sesión.**
- ✅ **Vídeos 14 y 16** — desbloqueados para **ingesta** (molde 4, bloque de múltiplos). El 16 es
  especialmente relevante: `moldes.md` lo declara la pieza que cierra las fichas `parcial` de
  múltiplos (`per`, `p_bv`, `ev_ebitda`, `peg`) con sus «dónde NO» y puntos ciegos. **No se han
  ingerido en esta sesión.**

**Efecto sobre el diagnóstico de puntuación:** las tres franjas degradadas quedan resueltas. El
corpus ya no tiene ninguna transcripción por debajo del suelo de calidad — salvo revisión futura del
vídeo **01** (2,63), que el diagnóstico marcó como caso intermedio, no crítico.

## [2026-07-19] cierre 14 | Marco de los múltiplos; taxonomía por numerador; T2 entre vídeos

**Estado:** RATIFICADA

**Vídeo 14 = MOLDE 6, cuarta instancia.** No es molde 4: no desarrolla ningún múltiplo (sin
numerador propio, sin banda propia, sin punto ciego). **Lo que hace es dar la estructura que las
fichas de molde 4 usan.** Las cuatro instancias del molde 6 quedan escalonadas por nivel: **01**
marco del método · **05** marco de una fuente documental · **13** marco de la fase de valoración
(qué método se elige) · **14** marco de una familia de herramientas (elegido el método, cómo se
organizan y cuándo se usa cada uno).

**⭐ La aportación estructural: la TAXONOMÍA POR NUMERADOR.** Rellena el campo *Familia por
numerador* que estaba `AUSENTE` en **las seis** fichas de múltiplos: **capitalización bursátil**
(per, p_bv, p_fcf — «los más conocidos pero también los más volátiles») · **valor de empresa**
(ev_fcf, ev_ebitda — «ya jugamos en otra liga: incluyen deuda y efectivo») · **crecimiento** (peg —
familia propia, pese a llevar el PER dentro).

> ⭐ **Un cierre limpio de RD-4.** Al ingerir el vídeo 12 se anotó que el experto justificaba la
> superioridad del EV/FCF **solo por el denominador**, y que la conexión con el numerador «estaba
> disponible y **no se hacía**» por no atribuírsela. **El vídeo 14 la enuncia él mismo.** La
> inferencia que no se hizo resultó ser suya — y se registra **cuando la dice, no antes**. RD-4 no
> costó información: solo la retrasó hasta que hubo fuente.

**Umbrales de imagen, verificados y ya incorporados.** La tabla de referencia del 14 trae seis
valores; **cuatro los pronuncia la voz** (PER<15, ROE>10%, Deuda/Patrimonio<1, FCF Yield>5%) y
coincidían. **Dos vivían solo en la captura** —`P/B < 1,5` y `EV/EBITDA < 10`—, se elevaron en la
ingesta en vez de escribirse a ciegas (RD-1 §2), **el usuario los verificó**, y ahora entran como
método en `p_bv` y `ev_ebitda`.

### 🆕 T2 ENTRE VÍDEOS — sub-tipo nuevo, y su criterio de resolución

`14-E1` y `14-E2` estrenan un patrón: **umbrales del mismo ratio dados en módulos distintos**. Hasta
aquí, todas las T2 eran contradicciones **dentro de un mismo vídeo**. Este choque **no existe hasta
que el corpus está lo bastante ingerido para cruzarlos** — y por tanto **aparecerá más**.

**Los dos se dictaminaron como COMPATIBLES**, y eso fija el criterio:

| Errata | Choque | Dictamen |
|---|---|---|
| `14-E1` | Deuda/Patrimonio `<1` (v.14) vs `<1,5` (v.03) | **GRADIENTE**: ideal `<1` · aceptable `<1,5`. ⭐ La propia voz del 14 lo enuncia: «menor a uno **es lo ideal**, aunque **tampoco es malo ligeramente por encima**» |
| `14-E2` | PER `<15`=barato (v.14) vs escala `<10`/`10-20`/`>20` (v.15) | **ATAJO vs. ESCALA**: el `<15` es un atajo orientativo **que el propio experto declara como tal**; la escala del 15 es la **referencia principal** |

> ⚖️ **Criterio fijado por el usuario:** cuando dos cifras del mismo criterio encajan como
> **gradiente** (ideal/aceptable) o como **atajo vs. escala fina**, se registran así, **no como
> contradicción**. **Se eleva solo lo que no encaje en ese patrón**: una contradicción real, no una
> diferencia de grano. *Aplicable de inmediato al vídeo 16, que redesarrolla múltiplos ya fichados.*

**Cita reutilizada del vídeo 01, VERIFICADA.** «Las tres patas» `[14, 07:00]` estaba marcada
*«reutilizada, no releída»* en `marco_analisis_fundamental` §4.3, pendiente en la lista de
verificación humana (punto 4). **Timestamp correcto y contenido coincidente** — ⭐ y aporta más de lo
registrado: **cada pata viene con su función declarada** (macro→ciclo/narrativa/sector ·
fundamental→margen de seguridad · técnico→gestión de posiciones). **El punto 4 queda cerrado.**

**Corrección de dato en `moldes.md`:** su campo 12 afirmaba que el gráfico «según Morgan Stanley»
**no estaba en el repositorio**. **Sí está** (`raw/capturas/14_multiplos_mas_usados_morgan_stanley.jpg`).
Corregido, marcando que es `CAUTELA` y que **no se transcribe ninguna cifra** — lo que es método es
su uso: advertir que **popularidad ≠ calidad**.

**Resumen:** cerrado el vídeo 14 (molde 6, cuarta instancia), incorporados los dos umbrales
verificados, dictaminadas `14-E1` y `14-E2` como compatibles —fijando el criterio para las T2 entre
vídeos—, verificada la cita del vídeo 01 y corregido el dato del gráfico de Morgan Stanley.

## [2026-07-19] moldes | Ratificación de moldes.md — D-78

**Estado:** RATIFICADA

**Contexto.** Desde su creación (D-63, v4), `moldes.md` llevaba la cabecera *«ESTADO: PILOTO, SIN
RATIFICAR»*. Con los 19 vídeos del corpus ingeridos y commiteados, el usuario decide ratificarlo en
la sesión de lint del corpus completo.

**Motivo declarado:** los **seis moldes** tienen ya al menos una ficha real, y el molde 5 —el que
más tarde en probarse, con sus **tres variantes** (`FILTRO` 17 · `SCORING` 18 · `REGLAS` 19)— quedó
completo sin que **ninguna de las tres** obligara a añadir un campo nuevo al cerrar su vídeo (v11 y
v12 solo confirmaron predicciones o registraron hallazgos, no ampliaron el esqueleto). El histórico
de versiones (v1→v12) muestra ajustes reales —tres de ellos «inducidos por la ingesta» (v5, v7,
v9)— pero **ninguno posterior al v10** tocó la forma de los campos; los últimos dos (v11, v12) son
verificación, no diseño.

**Qué cambia en la práctica:** el estado pasa de `PILOTO, SIN RATIFICAR` a `RATIFICADO` en la
cabecera de `moldes.md`. **D-63 sigue vigente sin cambios** (moldes.md como fuente única); esta
decisión ratifica el *contenido*, no la *arquitectura* del documento. `moldes.md` sigue siendo un
documento vivo — nuevo material (p. ej. si algún día se ingiere contenido fuera del curso, o el
propio experto publica un vídeo nuevo del módulo) podría seguir motivando una v13, igual que
cualquier otra pieza del cerebro.

**Resumen:** `moldes.md` pasa de piloto a ratificado (D-78), con el corpus completo como evidencia
y sin abrir ningún campo nuevo en el proceso.

## [2026-07-19] registro | Nota retrospectiva — cuatro rondas sin entrada individual en el log

**Estado:** RATIFICADA

**Qué pasó.** El cierre del vídeo 16, el cierre del vídeo 18, el cierre del vídeo 19 (con el que
terminó la ingesta de los 19 vídeos) y la sesión de lint del corpus completo **no generaron entrada
propia en este archivo** — el paso «añadir entrada a `log.md`» (`CLAUDE.md` §6.2, punto 7) se saltó
en las cuatro rondas seguidas. Se detectó al escribir la entrada de D-78 (arriba) y comprobar que el
log terminaba justo después de «cierre 14».

**No se reconstruyen esas cuatro entradas con el detalle de las demás** — hacerlo bien exigiría
revisar cada ronda con la misma profundidad que en su momento, y esta nota no es el sitio para eso.
Lo que sí queda es el puntero a **dónde está cada cambio**, para que el histórico no tenga un
agujero mudo:

| Ronda | Qué hizo | Commit |
|---|---|---|
| Cierre del vídeo 16 | Bloque de múltiplos (12–16) cerrado; `16-E1` dictaminada como gradiente; nueve fichas `completo` | `c0f1cf4` |
| Cierre del vídeo 18 | Molde 5 `SCORING`; P-3 ingerido; cadencia y práctica de registro completadas en `multibagger` | `32e19a5` |
| Cierre del vídeo 19 | Molde 5 `REGLAS`; **fin de la ingesta de los 19 vídeos**; hallazgo del vacío de arbitraje entre reglas, común a las tres variantes del molde 5 | `4537a1c` |
| Lint del corpus completo | Detección de contradicciones, enlaces, huecos y stale sobre las 28 fichas + documentos base | *(sin commit propio — informe entregado sin tocar ficheros)* |
| Corrección del lint | A1-A4, F (equivalencias técnicas ×6), D11, G3 (D-78), stale de `CLAUDE.md`/`index.md`/`mapa_tematico.md`, E1-E2, enlaces C, G1 | `9afe23d` |

**El registro continúa con normalidad desde esta entrada.** No se cambia ningún contenido de las
rondas afectadas — esto es una nota de proceso, no una revisión de sustancia.
