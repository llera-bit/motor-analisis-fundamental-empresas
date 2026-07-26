# CLAUDE.md — Schema del Cerebro de Análisis Fundamental

> Este archivo es la **capa schema** del patrón LLM Wiki. Define cómo está estructurado
> el wiki, qué convenciones se siguen y qué protocolos se ejecutan.
> Léelo entero al inicio de cada sesión.

---

## 0. Qué es este proyecto

Construimos un **cerebro** (knowledge base incremental, mantenida por LLM) que captura de
forma fiel y auditable la metodología de análisis fundamental de un experto (curso
"Invest Club", módulo 3: Análisis Fundamental de Empresas — 19 vídeos).

**Objetivo del cerebro:** poder razonar sobre una empresa cotizada aplicando la metodología
del experto, con juicio contextualizado y trazabilidad total de cada afirmación.

**Función acordada (D-58): COPILOTO DE CONSULTA INTERPRETATIVA.** El usuario aporta el dato de una
empresa y el cerebro devuelve **lo que el experto diría sobre ese dato** — interpretación
direccional, umbral y su naturaleza, lectura relacional, aplicabilidad, advertencia de uso aislado.
**No es ejecución autónoma:** el recorrido y la decisión son del usuario.

**Lo que este cerebro NO es:**
- No es un screener ni un embudo cuantitativo. (Esa arquitectura está **diferida**: ver D-10.)
- No es una fuente de datos numéricos de empresas.
- No es un resumen del curso. Es una **destilación auditada** de su método.

El usuario (Gerard) conserva siempre la decisión final de inversión.

---

## 1. Reglas duras (no negociables)

**RD-1 — Durante la CONSTRUCCIÓN, el origen es cerrado y la lectura tiene grados.**

**1 · Origen cerrado.** Toda la información que entra al cerebro procede **exclusivamente** del
material de `raw/` facilitado por el usuario: transcripciones, decks, capturas y referencias
externas. **El LLM nunca busca en internet ni aporta datos de su propio conocimiento.** Si algo
falta, es `[HUECO]` (RD-4) — nunca se completa desde fuera.

**2 · No todas las fuentes se leen igual.**
- **Texto legible** —transcripción `.srt`, capa de texto de un deck— es **FUENTE PLENA**: leerlo es
  literal, sin interpretación. **Misma validez que la transcripción.**
- **Imagen que hay que interpretar** —capturas, gráficos y páginas sin capa de texto— es **FUENTE
  CON CAUTELA**: se marca como tal y **ninguna cifra se extrae a ciegas de una imagen**; se eleva
  para verificación humana.
  *(Es el riesgo que motivó descartar Whisper, D-45: un dato mal leído no falla, sale plausible.
  Es invisible y se propaga.)*

**3 · Datos de empresa: definición sí, ilustración no.** Una cifra de una empresa concreta entra al
cerebro **solo si el concepto no se entiende sin ella**. Si únicamente ilustra cómo se aplica el
concepto, va a `wiki/ejemplos/` marcada **PEDAGOGÍA** (D-49) — el cerebro sabe aplicar el método a
cualquier empresa sin guardar el ejemplo.

> **Alcance — esta regla rige la CONSTRUCCIÓN, no el uso.** Las capas de uso (D-59, aparcadas) sí
> podrán consultar fuentes externas cuando llegue su momento. Aquí, y hasta que el cerebro esté
> construido, **el origen es cerrado**.

**RD-2 — Grounding: toda afirmación cita su fuente.**
Cada campo de cada ficha lleva su procedencia. Las afirmaciones del vídeo se citan con
timestamp: `[VÍDEO 06, 14:32]`. Las del PDF, con página: `[PDF 06, p.4]`.
Sin fuente identificable, no entra.

**RD-3 — `curso/` es sagrado.**
El namespace `curso/` refleja lo que el experto enseña. **No se modifica sin aprobación
explícita del usuario en cada cambio.** Cualquier aportación externa va a `complemento/`.
Prueba de fuego: *borrar `complemento/` entero debe devolver el curso íntegro y coherente.*

**RD-4 — Un hueco visible vale más que un relleno plausible.**
Si algo falta y no puede rellenarse honestamente, se marca `[HUECO]` y se deja así.
Nunca se completa en silencio.

---

## 2. Estructura de directorios

```
cerebro/
├── CLAUDE.md              # este archivo (schema)
├── index.md              # catálogo del wiki — LEER PRIMERO al responder una consulta
├── log.md                # histórico APPEND-ONLY de decisiones e ingestas
├── decisiones.md         # índice derivado: estado VIGENTE de cada decisión
├── fuentes.md            # inventario del material fuente + su fiabilidad de lectura
├── .gitignore
│
├── raw/                  # FUENTES INMUTABLES — cada subcarpeta declara su FIABILIDAD en su README
│   ├── transcript/       # NN_slug.srt (canónico, D-46) — FUENTE PLENA · los .txt NO son fuente
│   ├── pdf/              # NN_slug.pdf — capa visual del vídeo (01–12, D-64)
│   │                     #   MIXTO: capa de texto = PLENA · gráficos = CON CAUTELA
│   ├── capturas/         # NN_descripcion.jpg — CON CAUTELA (imagen a interpretar). Cubren 14/15/16
│   ├── externo/          # material que el experto AVALA y REPARTE — [EXTERNO-AVALADO] / [ENLACE-DESC]
│   ├── audio/            # .mp3 GITIGNORED (D-47). NO es fuente
│   ├── notas/            # VACÍA POR DECISIÓN (D-24): las notas no son insumo del cerebro
│   └── _inbox/           # VACÍA POR DECISIÓN: la ingesta cero ya se ejecutó
│
├── wiki/
│   ├── _estructura/      # cómo se construye el cerebro — NO es contenido del curso
│   │   ├── moldes.md     #   ⭐ FUENTE ÚNICA de los SEIS moldes (v12, D-63, RATIFICADO D-78)
│   │   └── radiografia.md#   diagnóstico fundacional del temario (D-55)
│   ├── curso/            # EL CEREBRO: el método del experto (RD-3)
│   │   ├── capa_decision.md   #   orden de ANÁLISIS, paradas, reglas (D-61)
│   │   ├── mapa_tematico.md   #   orden de ENSEÑANZA, conceptos paraguas (D-62)
│   │   └── (las 28 fichas de la ingesta — LOS 19 VÍDEOS DEL CORPUS, completa)
│   ├── ejemplos/         # PEDAGOGÍA: los casos del experto, FUERA del método (D-49, D-68)
│   ├── complemento/      # aportaciones externas, contraejemplos, crítica
│   ├── _provisional/     # 8 fichas con molde superado — SE REHACEN en la ingesta
│   ├── _archivo/         # superado, con traza: protocolo_analisis · inventario_atomico ·
│   │                     #   sondeo_procedimental (CONSULTABLE al ingerir 14/15/17) · piloto/
│   ├── erratas.md        # índice de erratas de la fuente (4 tipos, con estado)
│   └── capturas_pendientes.md  # qué falta capturar. VIVO
│
└── _archivo/whisper/     # vía de transcripción retirada (D-45) + el .srt descartado
```

**Convención de nombres:** `NN_slug` donde `NN` es el número de vídeo del usuario
(01–19, con cero a la izquierda). Mismo `NN_slug` para audio, PDF y transcripción,
de modo que se emparejan automáticamente.
Ej.: `06_deuda_y_caja.mp3` / `06_deuda_y_caja.pdf` / `06_deuda_y_caja.srt`
Las capturas usan `NN_descripcion.png` (D-48). El vídeo original NO vive en el proyecto (D-47).

---

## 3. Clases de procedencia

Cada campo de cada ficha lleva **obligatoriamente** una de estas etiquetas:

| Etiqueta | Significado | ¿Es fuente? |
|---|---|---|
| `[PDF]` | Lo que el experto **muestra en pantalla**: el deck del vídeo, **no un documento escrito aparte** (D-64) | ✅ Sí — pero **CEDE ante `[VÍDEO]`** cuando chocan |
| `[VÍDEO]` | Verbalizado por el experto (con timestamp) | ✅ Sí |
| `[INFERIDO]` | Deducido de un artefacto del experto (una captura, una tabla, un enlace) | ⚠️ Sí, con reserva — marcar la inferencia |
| `[CORREGIDO]` | ⚠️ **En desuso.** Del modelo viejo, que dictaminaba. El vigente **registra sin resolver** (§5): el cuerpo lleva la voz y el choque va al bloque de erratas. Solo se usa **tras un dictamen humano**, citando cuál | ❌ No |
| `[COMPLETADO-EST]` | Aportación externa (academia / industria) donde el curso no llega. 🆕 **Es también la clase del campo *Equivalencia técnica*** (D-72) — ver nota abajo | ❌ No — **exige tres pilares** |
| `[JUICIO-CLAUDE]` | Opinión razonada sin fuente citable | ❌ No — explícitamente opinión |
| `[HUECO]` | Falta y no se puede completar honestamente | — |
| `[ENLACE-DESC]` | Recurso **enlazado por el experto en la descripción** del vídeo, con URL (D-57) | ⚠️ Sí, con reserva |
| `[EXTERNO-AVALADO]` | Material externo que el experto **AVALA y REPARTE** como propio del curso, sin ser suyo (D-68) | ⚠️ Sí — se cita **como externo**, nunca como método del experto |
| `[ANOTACIÓN-EDITORIAL]` | Texto insertado **por el usuario** dentro del `.srt` | ❌ **NO.** No es del experto |

> **`[EXTERNO-AVALADO]` vs `[ENLACE-DESC]`:** el segundo es una **URL viva** que el experto enlaza;
> el primero, un **fichero que reparte** como material de clase (*«os lo dejaré en descargable»*,
> `[VÍDEO 14, 04:46]`). No es del curso, **pero el experto lo hace suyo al distribuirlo**.

> **`[ANOTACIÓN-EDITORIAL]` — regla dura de atribución.** En `[VÍDEO 06, 09:41]` la transcripción
> dice: *«y en cambio Intel **(en el pdf sale AMD, esto está mal…)** tiene más enterprise value»*.
> **Ese paréntesis es del USUARIO, no del experto.** Sirve como indicio para el bloque de erratas,
> pero **no se cita como afirmación suya**. Sin esta regla, un escritor le atribuiría al experto algo
> que no dijo — **una violación de RD-2 imposible de detectar después**.

### Marcadores de fiabilidad de lectura (RD-1 §2)

La fiabilidad **no es propiedad del fichero, sino de cada cita**: un mismo deck mezcla las dos.

| Marcador | Clase | Qué es |
|---|---|---|
| `[VÍDEO NN, mm:ss]` | **PLENA** | Transcripción `.srt` corregida a mano (D-46) |
| `[PDF NN, p.X]` | **PLENA** | Capa de texto del deck: bullets, rótulos, tablas seleccionables |
| `[PDF NN, p.X · IMAGEN]` | **CAUTELA** | Gráfico o página **sin capa de texto** dentro del deck |
| `[CAPTURA NN_nombre]` | **CAUTELA** | Captura de pantalla (`raw/capturas/`) |

> ⛔ **Ninguna cifra se extrae a ciegas de una fuente marcada CAUTELA.** Se marca y **se eleva para
> verificación humana** (RD-1 §2). *Verificado en `[PDF 07]`: p.1-4 y p.7 son texto (PLENA); p.5 y
> p.6 son gráficos (CAUTELA) — y son justo de donde el experto lee cifras en voz alta.*

> ### 🆕 `Equivalencia técnica` — el único contenido externo dentro de `curso/` (D-72)
>
> El **cuerpo** de cada ficha usa **las palabras del experto**: no se le atribuye ninguna etiqueta
> técnica que él no diga *(lección de `09-E1`: FCFF/FCFE eran jerga del escritor)*. **Además**, un
> bloque aparte —`## Equivalencia técnica`, moldes 1/2/3/4— registra el **término estándar de la
> industria**, marcado `[COMPLETADO-EST]`. **Por qué:** el cerebro es copiloto de consulta (D-58) y
> **los datos reales llegan en terminología estándar** — sin la correspondencia no reconoce el dato
> que se le trae. **Detalle completo en `moldes.md` §Equivalencia técnica.**
>
> ⚠️ **Efecto sobre la prueba de fuego de RD-3**, dicho explícitamente: es la primera vez que hay
> contenido externo **dentro** de `curso/`. La prueba se conserva **reformulada** — *borrar todos
> los bloques `## Equivalencia técnica` debe devolver el curso íntegro y coherente* —, y por eso el
> campo es un bloque delimitado y extraíble de un corte, nunca frases sueltas por los demás campos.

### Principio de justificación por tres pilares
Todo `[COMPLETADO-EST]` debe justificarse por al menos uno de:
- **(a) Fundamento económico/financiero** — por qué tiene sentido.
- **(b) Evidencia empírica** — literatura académica o práctica institucional documentada.
- **(c) Hipótesis explícita pendiente de validación** — se etiqueta como tal y se pre-registra.

**Nunca por autoridad del experto.** El curso es un insumo a validar, no un dogma.

### Umbrales: la regla que evita el sobreajuste
**No inventamos números.** Si el curso no da un umbral, no lo fabricamos.
Se registra el **rango plausible y su justificación**, marcado como hipótesis a testar.
Un umbral concreto (p.ej. "3,0x") **nunca se adopta por autoridad** — se deriva de evidencia.

**CONFIRMADO (D-56, vía el vídeo 16):** el experto **usa umbrales absolutos y los relativiza al
sector**, y lo enuncia como regla: *«comparar ese múltiplo con el múltiplo promedio al que ha estado
la compañía; frente a sus principales competidoras; contra los promedios del sector»*
`[PDF 12, p.1]`. **Ni un solo umbral del corpus se enuncia sin su caveat** — por eso el molde 4 lleva
el caveat como **columna obligatoria**: una banda sin él no es un resumen, es una falsificación.
La referencia sectorial es **fuente viva** (`[EXTERNO-AVALADO]` / `[ENLACE-DESC]`): se guarda el
puntero, **nunca la cifra**.

---

## 4. Formato de ficha → **`wiki/_estructura/moldes.md`** (D-63)

> ⭐ **`moldes.md` es la FUENTE ÚNICA de los seis moldes.** Aquí **no se copian: se remiten**, para
> que no existan dos versiones que se desincronicen.

| Molde | Para qué | Vídeos |
|---|---|---|
| **1 · Métrica cuantitativa** | deuda, ROIC/ROE, capex, FCF | 06–09 |
| **2 · Estado financiero** | cuenta de resultados, balance, flujo de caja | 02–04 |
| **3 · Cualitativo** | moat, equipo directivo | 10–11 |
| **4 · Múltiplo de valoración** | PER, PEG, P/BV, EV/EBITDA, FCF Yield… | 12–16 |
| **5 · Sistema de decisión** | filtro · scoring · reglas condicionales | 17–19 |
| **6 · Marco / arquitectura** | vocabulario, mapa del método, instrumental | 01 |

**Documentos que NO son fichas** (en `wiki/curso/`, bajo RD-3):

| Documento | Qué recoge |
|---|---|
| **`capa_decision.md`** | Orden de **ANÁLISIS**, criterios de parada, reglas condicionales, profundidad (D-61) |
| **`mapa_tematico.md`** | Orden de **ENSEÑANZA**, conceptos paraguas, preguntas rectoras, mapa deck ↔ vídeos (D-62) |

> ✅ **RESUELTO (dictamen del usuario, 2026-07-19):** el vídeo 05 (informe 10-K) usa el **molde 6**,
> a otro nivel — no es marco del método, es marco de **la fuente documental** que alimenta al
> método. Se decidió con la ficha delante, induciendo del material y no diseñando a priori (D-01,
> D-25). Ver `wiki/curso/informe_10k.md` para la distinción completa frente a
> `marco_analisis_fundamental.md`.

**Reglas de escritura, comunes a los seis** *(el detalle vive en `moldes.md`)*:
- Solo **Definición** y **Fuente** son obligatorios de origen.
- **Campo vacío = aspecto no tratado por el experto** → se marca `AUSENTE EN LA FUENTE`. **Nunca se
  rellena por deducción** (RD-4).
- ⭐ **Un campo OPCIONAL nunca significa descartar información.** Si el material trae contenido que
  corresponde a un campo, ese contenido **se añade siempre**. *(Complemento simétrico de RD-4: RD-4
  prohíbe rellenar lo que no hay; esto prohíbe omitir lo que sí hay. D-70.)*
- **REGLA DE ORO (D-51):** si el curso no dice el orden / rol / parada, es `[HUECO]`. **NO se deduce
  la secuencia.**
- Los **ejemplos** van a `wiki/ejemplos/` marcados PEDAGOGÍA; los moldes 1, 2, 4 y 6 los **apuntan**
  desde *Demostración del experto*. **Excepción: el molde 3 conserva sus *Ejemplares* dentro de la
  ficha**, porque ahí la empresa es parte de la definición de la categoría (D-68).

---

## 5. Tratamiento de erratas (D-16, ampliado)

La fuente **contiene errores objetivos ya confirmados**. El aparato completo —los cuatro tipos, el
formato de entrada y los precedentes— vive en **`moldes.md`**. Lo esencial:

> ⛔ **SE REGISTRAN, NO SE RESUELVEN — salvo evidencia INEQUÍVOCA del propio corpus (D-73).**
> El escritor **no aporta criterio propio** (RD-1). Pero si **otra parte de la misma fuente**
> desambigua el choque sin margen de duda, resolverlo **no es criterio: es leer la fuente entera**.
> Ver la regla completa abajo, §*Cuándo se eleva y cuándo se resuelve*.

1. **El cuerpo de la ficha lleva la versión que decide la jerarquía** (abajo), no «la correcta».
2. **Bloque `## Errata de la fuente`** al final de toda ficha, **se escriba o no haya nada**
   (`✅ Sin erratas detectadas`) — para que la ausencia sea un dato y no un olvido.
3. **`wiki/erratas.md`** las indexa todas.

### Los cuatro tipos

| Tipo | Qué choca | ¿Jerarquía? |
|---|---|---|
| **T1** · voz ↔ PDF | La voz y el deck se contradicen | ⚠️ Gana la voz **por defecto** — ver abajo |
| **T2** · voz ↔ voz | El experto se contradice a sí mismo | ⛔ No: el cuerpo lleva **los dos** |
| **T3** · PDF ↔ PDF | Inconsistencia interna del deck | ⚠️ Solo si la voz hace de testigo |
| **T4** · ambigüedad de transcripción | El `.srt` no determina qué dijo | ⛔ No: se cita **en crudo** |

> ⚠️ **No todos los tipos son posibles en todos los moldes.** En el **molde 5** (vídeos 17–19, **sin
> deck**) T1 y T3 son **imposibles**: un bloque vacío ahí es lo esperable y no dice nada de la
> fuente. En el molde 6 sí sería informativo. La matriz está en `moldes.md`.

### ⭐ La jerarquía voz > PDF NO es automática

**Gana la voz por defecto** — correcto en 4 de los 5 casos conocidos. **Excepción: lapsus verbal
evidente**, y entonces **el escritor NO dictamina**: marca `CANDIDATO A LAPSUS` y lo eleva.

**Indicios que permiten marcarlo — siempre INTERNOS a la fuente:** el deck lleva el término **como
rótulo escrito** y la voz lo dice de pasada · el experto **usa el término contrario en otro módulo**.
⛔ **Nunca por conocimiento externo** — eso sería RD-1.

*Caso que obliga a la excepción: «activos **tangibles**» (voz, `[10, 01:20]`) vs «ACTIVOS
**INTANGIBLES**» (`[PDF 10, p.2]`). Dictamen humano: **gana el PDF**.*

**Estados:** `PENDIENTE DE REVISIÓN HUMANA` · `CANDIDATO A LAPSUS` · `DICTAMINADO` (con qué se
resolvió, quién y cuándo) · 🆕 `DICTAMINADO POR EVIDENCIA` (D-73 — resuelto por el escritor citando
**qué parte del corpus** lo resuelve). **Una entrada no se borra al dictaminarse:** sigue contando
para la tasa de error.

### 🆕 Cuándo se ELEVA y cuándo se RESUELVE (D-73)

> **El umbral para elevar no es «hay una errata». Es «hay una errata que NO puedo resolver sin el
> usuario».**

| Situación | Qué hace el escritor |
|---|---|
| **Otra capa del corpus la desambigua sin margen de duda** — una cifra del deck contradice la palabra, la coherencia interna del propio ejemplo la fija, el término correcto se usa bien en otro punto de la misma fuente | ✅ **CORRIGE** en el cuerpo y registra `DICTAMINADO POR EVIDENCIA`, **citando qué evidencia lo resuelve**. **NO se eleva** |
| **La resolución depende del CRITERIO del usuario o de algo que solo él tiene** — su escucha del audio, su juicio como inversor, o una contradicción que las fuentes del corpus **no** resuelven | 🔴 **ELEVA** |
| **Duda real** — el deck no zanja · podría ser interpretación y no error · **toca método y no ejemplo** | 🔴 **ELEVA** |

> ⚖️ **La regla de oro de este apartado: ante la duda, eleva; ante evidencia inequívoca, corrige.**
>
> ⛔ **RD-1 intacta.** «Resolver con evidencia del corpus» **NO es conocimiento externo**: es usar
> otra parte de la propia fuente. **Nunca se corrige con conocimiento del LLM** — si el corpus no lo
> zanja, el escritor no lo zanja.
>
> *Caso que originó la regla (`12-E1`): la voz dice «Lilly está más barata» y el propio deck trae
> los números que lo desmienten (36,62 frente a una media de 29,22 → está **cara**). El corpus se
> desambiguaba solo; elevarlo habría sido trasladar al usuario una lectura que la fuente ya cerraba.*

### 🆕 Regla de arrastre — cuándo una errata se eleva de inmediato (D-71)

**Por defecto, una errata nueva SE ACUMULA** en el bloque de erratas de la ficha y en `erratas.md`,
`PENDIENTE DE REVISIÓN HUMANA`, para un dictamen final conjunto — **no se eleva suelta**. Pero
algunas no pueden esperar: si dejarlas sin resolver **propagaría el error hacia trabajo posterior**,
se marca `🔴 ARRASTRA` y se eleva **de inmediato**, antes de dar la ficha por completa.

**Una errata ARRASTRA si se cumple (a) O (b):**

| Criterio | Qué mira | Ejemplo |
|---|---|---|
| **(a) Cita explícita hacia adelante** | El propio experto liga el concepto a un vídeo o cálculo posterior, en la misma fuente | «entender esta distinción [capex mantenimiento/expansión] permite estimar correctamente el free cash flow ajustado» `[08, 05:08]` → `08-E1` |
| **(b) Cimiento conceptual** | La errata afecta a la **definición** de algo que **otros conceptos del corpus dan por sentado**, aunque nadie lo cite explícitamente. El escritor se pregunta: *«¿esta definición es un cimiento de otros conceptos del corpus?»* | El FCF es «la base del método de valoración más utilizado, el DCF» `[09, 06:00]` — su propia definición (¿resta intereses o no?) es un cimiento, se cite o no cada vez → `09-E1` |

**El criterio (b) exige criterio, no automatismo.** No toda errata sobre una definición arrastra —
solo cuando esa definición sostiene otras piezas del método. Una errata de rótulo o de nombre propio
(ver §5 «qué NO es errata») casi nunca cumple (b). El escritor **registra su razonamiento** al
marcar el `¿Arrastra?`, para que el dictamen humano pueda auditarlo, no solo aceptarlo.

**Lo que NO cambia:** el escritor sigue sin dictaminar — «arrastra» decide **cuándo** se eleva, no
**qué** dice el cuerpo mientras tanto (eso lo sigue decidiendo la jerarquía voz>PDF de más arriba).

### Función epistémica — y su límite

⚠️ **La cuenta mide la fuente Y el método con que se buscó**: con la misma fuente dio 0 → 9 → 17
según el instrumento. Es un **suelo**, no una medida. ✅ **Cubre ya los 19 de 19 vídeos** (corpus
completo, 2026-07-19) — pero **el instrumento no fue homogéneo**: 12 vídeos se contrastaron contra
dos capas (voz + PDF) y 7 solo contra una (sin deck), así que sus cuentas **no son comparables entre
sí**. Su uso legítimo sigue siendo **cualitativo**: qué **tipos** de defecto tiene esta fuente. Ver
`wiki/erratas.md` para el recuento vigente y su aviso de lectura.

---

## 6. Protocolos

### 6.0 — Ingesta cero · ⛔ ARCHIVADA (ejecutada)

**Ya se ejecutó.** El material está repartido y catalogado en `fuentes.md`, con los nombres
originales preservados; `raw/_inbox/` está vacía por decisión. **El protocolo completo queda en el
histórico de git** — se recupera solo si entra material nuevo al proyecto.

### 6.1 — Transcripción (D-46)
- **La fuente canónica es el `.srt` corregido a mano por el usuario en Subtitle Edit, contra el
  vídeo.** Flujo: transcripción base local → el usuario corrige viendo el vídeo → `.srt` corregido =
  canónico. El `.txt` se **exporta DESDE el `.srt`** (nunca se edita a mano). Salida **UTF-8, con
  timestamps** → cumple RD-2. *(Whisper descartado, D-45; ver `_archivo/whisper/`.)*
- **El usuario corrige errores de MÁQUINA** (lo que se oyó mal). **NUNCA corrige errores del
  EXPERTO:** si el experto dice algo objetivamente falso, se transcribe **tal cual** y el cerebro lo
  detecta cruzando con el PDF (ver §5, erratas).
- **Verificación de calidad (tool-agnóstica, obligatoria) — leyendo texto real:**
  (a) **direcciones y relaciones** — p.ej. "EV > Market Cap" vs "<": una **inversión silenciosa** es
  el fallo más grave; (b) **acrónimos y jerga** (EV, EBITDA, tickers); (c) **números y contenido
  completo** (que no falten frases).
  **Lección D-45: la buena puntuación NO es indicador de fidelidad** — un texto bien puntuado con un
  error direccional es más peligroso que uno feo, porque baja la guardia del revisor.

### 6.2 — Ingesta de un módulo
**De uno en uno. Nunca en lote sin revisión del usuario.**

> **Modelo de fuente y capturas (D-64, supersede D-48 en su parte de "tercera fuente"):**
> **El PDF NO es un documento aparte: es el deck que se ve en pantalla mientras el experto habla.**
> Transcripción (lo que dice) + PDF (lo que muestra) son **las dos mitades del mismo momento**, y se
> leen juntas. **Vídeos con PDF: 01–12.**
> - **`raw/capturas/` NO es una tercera fuente por defecto.** Solo hace falta captura **donde el deck
>   no cubre lo operativo**, es decir, cuando el experto **se sale del deck** a otra pantalla (un
>   balance real, un proveedor de datos) o **dibuja encima** de la slide. *Caso del piloto: en el
>   vídeo 03 los tres ratios con umbral se calculan sobre el balance de Meta, que no está en el PDF.*
> - **Un hueco de cobertura NO bloquea la ficha.** Se escribe, se marca con precisión en el campo
>   *Fuente*, y se anota en `wiki/capturas_pendientes.md`. **No se inventa lo que no se ve** (RD-4).
> - ⭐ **La captura es FUENTE CON CAUTELA** (RD-1 §2), igual que un gráfico dentro del deck. Se cita
>   `[CAPTURA NN_nombre]` o `[PDF NN, p.X · IMAGEN]`, y **ninguna cifra se extrae a ciegas de ella**:
>   se marca y se eleva para verificación humana.
> - **Jerarquía: voz > PDF POR DEFECTO — salvo lapsus verbal evidente.** Las discrepancias se
>   **registran** en `## Errata de la fuente` (los 4 tipos, ver `moldes.md`); **no se resuelven por
>   criterio propio** (RD-1). Ante indicio de lapsus, el escritor marca `CANDIDATO A LAPSUS` y
>   **eleva**: el dictamen es humano (§5).

> **Recordatorio activo de secuencia (D-62):** al ingerir hay que separar **dos cosas que suenan
> igual y no lo son**:
>
> | Qué se oye | Qué es | Dónde va |
> |---|---|---|
> | *"lo primero que hago es…"* · *"si veo esto ya no sigo…"* · *"esto solo lo miro cuando…"* · *"aquí depende de si es una empresa de…"* | **Orden de ANÁLISIS** / criterio de parada → **método** | **`capa_decision.md`**, verbatim |
> | *"en la siguiente clase…"* · *"ya lo miramos en…"* · *"el segundo estado clave"* | **Orden de ENSEÑANZA** → **logística de temario, NO método** | **`mapa_tematico.md`** |
>
> **Por qué importa, y no es cosmético:** `radiografia.md` §C clasifica los punteros entre clases como
> afirmaciones **operativas** — *"es logística, no interpretación"*. Meterlos en la capa procedimental
> **la infla con orden de temario y hace que el protocolo parezca secuencial** — que es exactamente lo
> que **D-60** niega: el protocolo del curso es **mínimo**, y esa minimalidad es un **hallazgo**, no un
> hueco. *(Ya ocurrió: el antiguo `protocolo_analisis.md` anotaba "en la siguiente clase entraremos en
> ratios" como si fuera orden de análisis.)*
>
> **NO deducir el orden** (regla de oro, D-51). **Numerar una enumeración es ordenarla:** si la frase
> no lleva marcador explícito ("primero", "después", "posteriormente"), **no es una secuencia**.
> **Si un módulo no aporta nada procedimental —lo esperable bajo D-60— no se anota nada y no pasa nada.**

1. Leer PDF + transcripción `.srt` del módulo.
2. Discutir los hallazgos clave **con el usuario** antes de escribir.
3. Escribir la ficha en `wiki/curso/` **con el molde que le corresponda** (§4), con procedencia por campo y timestamps. Los **ejemplos** van a `wiki/ejemplos/` (D-68).
4. Registrar erratas (en la ficha + en `erratas.md`).
5. Marcar `[HUECO]` sin rellenar.
6. Actualizar `index.md` y las cross-references. *(El inventario atómico está **archivado**: los moldes v4 no tienen campo «inputs atómicos» — D-69.)*
7. Añadir entrada a `log.md`.
8. **Solo entonces**, y por separado, proponer `complemento/` (contraejemplos, `[COMPLETADO-EST]`).

### 6.3 — Lint (periódico)
Buscar: contradicciones entre fichas · claims obsoletos · páginas huérfanas · conceptos
mencionados sin ficha propia · cross-references ausentes · huecos que podrían cerrarse.
**Contradicción de máximo interés:** el experto usa EBITDA como métrica central; otras
escuelas (Buffett) lo desprecian. Cuando aparezca, se superficia, no se esconde.

---

## 7. Gobernanza de decisiones (ADR — D-18)

- **`log.md` es APPEND-ONLY. Nunca se edita ni se borra nada de lo ya escrito.**
- Las decisiones no se modifican: se **supersede**.
- Estados: `PROPUESTA` · `RATIFICADA` · `SUPERSEDIDA por D-XX` · `DEROGADA`
- **`decisiones.md`** es el índice derivado: solo el estado vigente.

*Motivo: un log que se reescribe es un log que miente. Dentro de seis meses hay que poder
responder "¿por qué decidimos X y luego lo cambiamos?".*

---

## 8. Política de modelos (D-28)

| Tarea | Modelo |
|---|---|
| Ingesta de un módulo (mecánica, voluminosa) | **Sonnet** |
| Diseño, arquitectura, auditoría crítica | **Opus, esfuerzo alto** |
| Lint (detectar contradicciones entre fichas) | **Opus, esfuerzo medio** |
| Aportaciones `[COMPLETADO-EST]` | **Opus, esfuerzo alto** — máximo riesgo de inventar con confianza |

**Regla: Sonnet para escribir, Opus para pensar y auditar.**

---

## 9. Riesgos vivos — recordarlos, no olvidarlos

- **Sesgo de automatización (riesgo nº 1).** Este cerebro es eficaz, y esa eficacia puede
  hacer que el usuario deje de leer lo que produce. **Ingesta de una en una, con revisión.**
  La lentitud aquí es una característica, no un defecto.
- **Sesgo de supervivencia en los ejemplares.** El curso enseña con ganadores (ASML, Ferrari,
  Coca-Cola, Apple, Meta). Sin casos negativos, el cerebro no discrimina. **Contraejemplos
  obligatorios.**
- **Corrupción silenciosa de `curso/`.** Guardarraíl: RD-3 + git.
- **Discrepancias voz ↔ PDF.** El PDF **NO** está desactualizado: es la **capa visual del mismo
  momento** (D-64; D-19 cerrada por D-65). Pero las dos capas **sí chocan a menudo**, y cuando chocan
  **manda la voz — por defecto**. La discrepancia **se registra** en `## Errata de la fuente` (4
  tipos, ver `moldes.md`); **nunca se resuelve por criterio propio** — eso sería RD-1. ⚠️ Ante
  **lapsus verbal evidente** el escritor **no dictamina**: marca `CANDIDATO A LAPSUS` y eleva (§5).
- ⭐ **Lectura de imágenes (riesgo nuevo, RD-1 §2).** Las capturas y los gráficos dentro de un deck
  son **fuente CON CAUTELA**: un dato mal leído de una imagen **no falla, sale plausible**. Es el
  mismo modo de fallo invisible que motivó descartar Whisper (D-45). **Ninguna cifra a ciegas desde
  una imagen** — se marca y se eleva. ⚠️ **Muerde ya en el bloque de múltiplos**: las capturas
  cubren 14/15/16, que **no tienen deck**, así que ahí la única capa visual es la de cautela.
