# mapa_tematico.md — Arquitectura del temario (piloto)

> **Qué es.** El sitio de lo que **no es una ficha de concepto pero organiza los conceptos**:
> conceptos paraguas, preguntas rectoras, posición de cada módulo en el conjunto, genealogía de las
> ideas, y el mapa deck ↔ vídeos. Responde **«¿dónde encaja esto en el todo?»**.
>
> **Linaje.** `radiografia.md` §C describe una «**arquitectura temática macro**» que el curso enuncia
> «de forma laxa» — las cinco patas del vídeo 01, el orden de enseñanza. Este archivo es su
> contenedor.
>
> **Frontera con [[capa_decision]]:** aquí va **cómo se organiza el temario**; allí, **qué hacer y en
> qué orden**. Regla práctica: *orden de enseñanza* → aquí; *orden de análisis* → allí.

---

## 1 · Conceptos paraguas (los que ninguna ficha posee)

### ⭐ La RENTABILIDAD — `[VÍDEO 07, 00:09–02:24]` + `[PDF 07, p.1]`

**Este concepto tenía una slide entera y ninguna ficha.** El vídeo 07 se partió en [[roic]] + [[roe]]
(decisión correcta: sus campos bifurcan en sentidos opuestos), pero eso dejó huérfano el nivel
superior. **Vive aquí.**

**Definición.** Las dos capas:

> «La rentabilidad de una Compañía es **el beneficio que se obtiene a través de una inversión**. Es
> decir, las ganancias o pérdidas que se han obtenido a través de una cantidad invertida, **en un
> periodo determinado**» `[PDF 07, p.1]`
>
> «la rentabilidad es el beneficio que obtiene una empresa en relación al capital que invierte,
> **cuánto pone y cuánto saca**» `[VÍDEO 07, 00:25]`

**Por qué es un pilar. Solo-verbal:** «la rentabilidad del capital es **uno de los pilares más
importantes** en este análisis fundamental» `[VÍDEO 07, 00:15]`; «nos dice cuánto beneficio genera una
empresa **en relación a los recursos que necesita para operar**» `[VÍDEO 07, 00:53–01:12]`.

**La bifurcación.** Es de la fuente, está en las dos capas, y es la que explica por qué hay dos fichas:

| | **RENTABILIDAD ECONÓMICA** → [[roic]] | **RENTABILIDAD FINANCIERA** → [[roe]] |
|---|---|---|
| **Deck** `[PDF 07, p.1]` | «el beneficio promedio de la compañía por **el total de las inversiones hechas**, expresada en términos %» | «el beneficio que **los accionistas** de la compañía obtienen por haber invertido en ella, también expresada en términos %» ⚠️ **errata `07-E7`** |
| **Voz** `[VÍDEO 07, 01:51–02:05]` | «mide el beneficio en relación al total de la inversión, que acordad que el total de la inversión es **capital más deuda**» | «mide la ganancia sobre el **equity**, sobre los fondos propios» |

«Ambas métricas están expresadas en porcentaje, y se utilizan para medir la eficiencia y el atractivo
de ese negocio […] pero mirado desde **diferentes perspectivas**» `[VÍDEO 07, 02:05]`. Y: «ambas son
formas de medir **si una empresa realmente crea valor**, pero lo hacen desde ángulos diferentes»
`[VÍDEO 07, 00:41]`.

**Las cuatro métricas del deck** — «**ROIC · ROCE · ROE · ROA**. Diferentes formas de medir la
rentabilidad» `[PDF 07, p.1]`. De las cuatro, el curso desarrolla **dos**: «Nos centramos en 2
indicadores de la rentabilidad: ROIC y ROE» `[PDF 07, p.2]`.

`[HUECO]` ⚠️ **Ninguna capa dice por qué ROA y ROCE quedan fuera.** Se nombran en p.1 y desaparecen en
p.2. *(La frase que hace la selección arrastra la errata `07-E6`.)* **No se rellena.**

---

### 🆕 ⭐ LOS CUATRO GRUPOS DE RATIOS — `[VÍDEO 15, 02:05–04:22]` + las 4 capturas

**Este concepto tenía cuatro capturas y ninguna casa.** `mapa_tematico` §5 lo declaraba `[HUECO]`
—*«material de este archivo. No ingeridos. No se anticipan»*— y **queda cerrado aquí** (ingesta del
vídeo 15, 2026-07-19).

> «hay **cientos de ratios**. Por eso a mí sobre todo me gusta **agruparlos en cuatro grupos** y
> trabajarlos en cuatro grupos, que veréis que os ayudan bastante a la hora de **filtrar, entender o
> sobre todo colocar** ciertas empresas» `[VÍDEO 15, 02:05–02:19]`

| # | Grupo | Qué responde, en sus palabras | Contenido |
|---|---|---|---|
| **1** | **Ratios de VALORACIÓN** | «te dicen si una acción está **cara o barata**» `[02:32–02:41]` | [[per]] · [[p_bv]] · [[p_fcf]] · [[ev_fcf]] · [[ev_ebitda]] · [[peg]] — ⭐ **y tienen su propia sub-taxonomía por numerador** (capitalización · EV · crecimiento), del vídeo 14 → [[marco_multiplos]] §4.1 |
| **2** | **Ratios de RENTABILIDAD** | «cómo la empresa **gana dinero** con sus activos, operaciones, inversiones y recursos propios»… «si la empresa es una **mina de oro** para sus accionistas o **un pozo sin fondo**» `[03:01–03:23]` | ROA · [[roe]] · [[roic]] · ROCE · Márgenes (FCF, EBITDA, neto, operativo) |
| **3** | **Ratios de SALUD FINANCIERA** | «si aquello es un **cadáver** o si la compañía está **más fuerte que el vinagre**» `[03:26–03:33]` | Liquidez (3) · Endeudamiento (4) → [[balance_general]] · [[deuda_neta]] |
| **4** | **Ratios de CUIDAR AL ACCIONISTA** | «qué tal cuida la empresa al accionista, y sobre todo **si esa manera de cuidarlo es sostenible**» `[03:50–04:02]` | Rentabilidad por dividendo · Crecimiento de dividendos · Payout/FCF · Recompra de acciones |

> ⭐ **El grupo 4 lleva su propia advertencia, y es la más afilada de los cuatro:** «**no es lo mismo
> cuidarlos bien a costa de destrozarte tus números**, que hacerlo de una manera **sana y creciente o
> estable o duradera**» `[VÍDEO 15, 04:02–04:13]`.

> ⚠️ **Es una taxonomía, no una secuencia.** «Empezaremos por los ratios de valoración» `[04:39]` es
> orden de **exposición**, no de análisis (D-51/D-62). El propio experto declara el criterio de uso
> como **contextual, no ordenado**: «la complejidad de los ratios financieros radica en entender la
> contabilidad de la empresa y en **saber cuál utilizar en cada contexto**» `[VÍDEO 15, 04:22–04:34]`.

> 🆕 **Cierra parcialmente el otro `[HUECO]` de esta sección**, el de arriba: «ninguna capa dice por
> qué **ROA y ROCE** quedan fuera» en el vídeo 07. **No quedan fuera del corpus** — el vídeo 15 los
> define, brevemente, dentro del grupo 2. ⚠️ **Pero sigue sin decir por qué el 07 los descartó**, que
> era la pregunta. **El hueco se estrecha, no se cierra.**

> 🔴 **CANDIDATO, NO CONFIRMADO — ¿son estos «los cuatro»?** [[capa_decision]] §2.2 arrastra un
> `[HUECO]` desde el piloto: el experto dice «cuatro cositas» (vídeo 03, ×3) y «cuatro cosas» (vídeo
> 13) **sin enumerarlas nunca**. Aquí, por fin, hay **cuatro** algo — y con la misma función
> («filtrar, entender, colocar»). ⛔ **Pero el experto NO dice que sean los mismos cuatro**, y los
> alcances no coinciden (el del 03 era del **balance**). **No se funden** (D-51). Se registra como
> coincidencia llamativa, pendiente de dictamen humano.

---

## 2 · Preguntas rectoras

### ⭐ «¿Está esta empresa creando valor con el capital que gestiona?» — `[VÍDEO 07, 10:20–10:28]`

> «por eso a partir de aquí **todas las métricas que veamos deben responder a esta gran pregunta**:
> ¿está esta empresa creando valor con el capital que gestiona?»

**No es una propiedad del ROIC ni del ROE: es un criterio de lectura que el experto declara sobre
todo lo que viene después.** Solo-verbal.

**Por qué está aquí y no en [[capa_decision]]:** no dice qué hacer ni en qué orden. Dice **con qué
pregunta en la cabeza** hay que leer el resto del temario. Es marco, no procedimiento.

✅ **Alcance verificado — cerrado con el corpus completo (lint, 2026-07-19).** «A partir de aquí»
sitúa la pregunta como rectora **del vídeo 07 en adelante** (módulos 08–19). Barrido de las
transcripciones 08-19 buscando la formulación y sus variantes («crea valor», «crear valor»,
«destroza valor»):

| Vídeo | Aparición | ¿Es la pregunta rectora? |
|---|---|---|
| **08** (capex) | «crear valor **si las inversiones generan retornos**» | ⚠️ Parcial — mismo concepto aplicado al capex, pero no enunciado como pregunta rectora |
| **15** (ratios) | «recompra **que crea valor**» | ❌ No — contexto distinto (recompras) |
| 09-14, 16-19 | Ninguna | ❌ |

**El corpus NO aporta evidencia de que la pregunta se retome como principio rector en ningún módulo
posterior.** Aparece una vez, en el 07, y no vuelve a formularse como tal — ni una sola vez en 12
vídeos. *(Es una lectura del corpus, no un juicio sobre el experto: no dice que "no cumpla" su
propia declaración, dice que el material disponible no muestra que la retome explícitamente.)*
**Queda como principio local del vídeo 07**, no global del curso.

---

## 3 · Posición de los módulos en el conjunto

### Los tres estados financieros

El curso trata los estados como una **serie declarada**, y el balance se sitúa **en medio**:

> «ya conocemos la cuenta de resultados […] ahora vamos a ver el **segundo estado clave** que es el
> balance general» `[VÍDEO 03, 00:08–00:16]`
>
> «la **siguiente clase** veremos el **tercer estado**, que es el flujo de caja, donde ya analizaremos
> si ese beneficio contable realmente se traduce en…» `[VÍDEO 03, 09:10–09:17]`

```
cuenta de resultados (02)  →  BALANCE (03)  →  flujo de caja (04)
```

> ⚠️ **Esto es orden de ENSEÑANZA, no de ANÁLISIS.** El experto dice «la siguiente clase», no «lo
> siguiente que debes analizar». Por eso está aquí y no en [[capa_decision]]. `radiografia.md` §C hace
> la misma distinción y la clasifica como afirmación **operativa**, no metodológica.

**Qué aporta cada estado, según él** — la única frase que los delimita entre sí es solo-verbal y está
en el 03: «aquí **no se habla de rentabilidad**, sino de la **estructura**» `[VÍDEO 03, 00:16]`, y el
balance ve «riesgos que **no aparecen en la cuenta de resultados**» `[VÍDEO 03, 05:58]`.

✅ **Cerrado con el corpus completo (lint, 2026-07-19).** Los módulos 02 y 04 están ingeridos
(`cuenta_de_resultados.md`, `flujo_de_caja.md`); esto es lo que aportan a la serie:

- **02 (cuenta de resultados):** `AUSENTE EN LA FUENTE` como delimitación explícita — el vídeo no
  dice qué NO cubre, a diferencia del 03. Se delimita solo por contraste implícito con lo que sí
  dice el 02 sobre el balance y el flujo de caja `[VÍDEO 02, 01:43–01:58]`.
- **04 (flujo de caja):** **sí delimita explícito**, y es la frase más nítida de las tres: «aquí ya
  **dejaremos atrás el beneficio contable** y nos vamos a centrar en el efectivo real... una cosa es
  ganar dinero en el papel y otra muy distinta es tenerlo en la cuenta» `[VÍDEO 04, 00:28–00:44]`.

**La serie completa, con sus tres delimitaciones (una implícita, dos explícitas):** el 02 no se
autodelimita · el 03 dice «no se habla de rentabilidad, sino de estructura» · el 04 dice «dejamos
atrás el beneficio contable, vamos al efectivo real». Detalle completo en cada ficha.

### Módulo 06 — Deuda y Caja: sus enganches con el temario

*(Heredado de `wiki/curso/protocolo_analisis.md` al consolidarlo en [[capa_decision]] — D-61.
**Re-verificados contra `raw/transcript/06_deuda_y_caja.srt`.** Están aquí, y no en [[capa_decision]],
porque los dos llevan marcador explícito de **clase**, no de análisis: son orden de enseñanza.)*

- **Hacia atrás** — la clasificación de la deuda por plazo ([[deuda_financiera]]) se apoya en un
  módulo **anterior**:
  > «corto plazo, con vencimiento menor a un año y largo plazo, con vencimiento mayor a un año
  > (**acordaros que esto ya lo miramos también en los estados financieros**)» `[VÍDEO 06, 01:20–01:28]`

- **Hacia delante** — tras Deuda y Caja vienen los **ratios** ([[roic]] · [[roe]]):
  > «Y **en la siguiente clase** entraremos ya en ratios financieros clave que nos permitirán hacer
  > comparaciones rápidas y detectar fortalezas o debilidades, **con muy pocos números**»
  > `[VÍDEO 06, 10:24–10:39]`
  >
  > ⚠️ **Timestamp corregido:** el archivo antiguo lo citaba en `[06, 10:30]`, que es la línea de
  > continuación; la frase arranca en `10:24`.
  >
  > La cola —«**con muy pocos números**»— **no** es orden de enseñanza: es un **criterio de
  > profundidad**, y encaja con el patrón «son cuatro cosas / un simple vistazo» del vídeo 03. Vive en
  > **[[capa_decision]] §2.2**.

```
estados financieros (02–04)  →  DEUDA Y CAJA (06)  →  ratios (07)
```

> ⚠️ **Esto es orden de ENSEÑANZA.** El archivo antiguo lo anotaba como *«tras Deuda/Caja viene el
> bloque de ratios»* dentro de la capa procedimental — leyendo el orden de las **clases** como orden
> de **análisis**. `radiografia.md` §C clasifica estas frases como **operativas**: *«es logística, no
> interpretación»*. **El experto no dice en ningún momento que al analizar una empresa haya que mirar
> la deuda antes que los ratios.**

### Módulo 12 — Múltiplos de valoración: apertura del bloque

*(Ingerido 2026-07-19. Está aquí, y no en [[capa_decision]], porque el marcador es explícito de
**clase**: «lo que veíamos en la **primera clase**». Es orden de enseñanza — D-62.)*

- **Hacia atrás** — el bloque de múltiplos se abre **reanclándose en el marco del vídeo 01**:
  > «Recordemos primero lo que veíamos en la **primera clase** relativo al concepto del **Margen de
  > Seguridad**» `[PDF 12, p.2]`

  La voz lo desarrolla sin nombrar la clase: la zona donde el múltiplo actual está por debajo de su
  promedio «nos ofrece un margen de seguridad, minimizando así el riesgo y aumentando el potencial
  de revalorización» `[VÍDEO 12, 01:32–01:40]` → [[marco_analisis_fundamental]] §2.

  ⭐ **Es el primer módulo del corpus ingerido que vuelve explícitamente sobre el vocabulario del
  01.** Confirma en la práctica lo que el molde 6 sostenía: «margen de seguridad» se **define** una
  sola vez, en el 01, y se **reutiliza** después.

- **El inventario del bloque** — el deck abre listando los múltiplos que el módulo va a tratar:
  > «PER (Price Earnings Ratio) · P/B (Price to Book) · EV/EBITDA · P/S (Price to Sales) · EV/FCF ·
  > FCF Yield · DIVIDEND YIELD (Rendimiento del Dividendo)» `[PDF 12, p.1]`

  La voz enumera los mismos, en otro orden y añadiendo el criterio de por qué son varios: «cada uno
  de estos nos ofrece una perspectiva diferente del valor relativo de la compañía… **cada múltiplo
  tiene sentido según el tipo de empresa y sector**» `[VÍDEO 12, 01:04–01:18]`.

  ⚠️ **De los siete, el vídeo 12 solo desarrolla DOS**: [[per]] y [[ev_fcf]]. Los otros cinco
  quedan **nombrados, no desarrollados** en el 12 — su desarrollo llegó con los vídeos 13-16, **ya
  ingeridos**: [[p_bv]] (15/16), [[p_s]] (16), [[ev_ebitda]] (15/16), y [[ev_ventas]] (16, que hace
  de «versión mejorada» del P/S). ⚠️ **`FCF Yield` sí tiene ficha** ([[fcf_yield]], vídeo 16), pero
  **`Dividend Yield`, el séptimo nombrado aquí, NUNCA se desarrolla en ningún vídeo del corpus** —
  se queda para siempre en «nombrado, no desarrollado». *(Detectado en el lint del corpus completo,
  2026-07-19: con los 19 vídeos dentro, ya se puede afirmar que no es que su desarrollo "pertenezca"
  a un vídeo futuro — sencillamente no llega.)* **La lista es inventario del temario, no una
  taxonomía**: no lleva ningún marcador de orden ni de familia.

```
marco / margen de seguridad (01)  →  …  →  MÚLTIPLOS: apertura + PER + EV/FCF (12)  →  13–16
```

> ⚠️ **Esto es orden de ENSEÑANZA.** El experto no dice en ningún momento que al analizar una
> empresa haya que mirar los múltiplos en este punto ni en este orden.

### Módulo 13 — el «jefe final»: apertura del tramo práctico

*(Ingerido 2026-07-19. Desarrollo completo en [[marco_valoracion]]; aquí solo la posición en el
temario.)*

- **Hacia atrás** — el 13 declara cerrado el tramo conceptual y abre el práctico:
  > «después de dar a estas primeras pinceladas y **temario necesario** para que entendamos dónde nos
  > estamos metiendo… ahora ya pasamos al **final boss, al jefe final de este módulo**, ya que es
  > toda esta parte ya más enfocada a la valoración, a los ratios, a la aplicación, a plataformas…
  > pero ya desde una parte **más práctica**» `[VÍDEO 13, 00:09–00:40]`

  ⭐ **Es la única frase del corpus que parte el módulo en dos mitades declaradas** — una conceptual
  (01–12) y una práctica (13–19). No es orden de análisis: es estructura del temario.

- **Hacia delante** — anuncia el 14:
  > «a partir de aquí, **en la siguiente clase**, ya entraremos de lleno en la parte más potente y
  > práctica de **cómo usar estos múltiplos, cuándo usarlos**, ratios fundamentales, etcétera»
  > `[VÍDEO 13, 13:54–14:03]`

  ✅ Encaja con el slug del vídeo 14 (`14_cuando_usarlos`), **hoy bloqueado por transcripción sin
  puntuar**.

```
conceptual (01–12)  →  JEFE FINAL / práctica: valoración (13)  →  cuándo usarlos (14)  →  15–19
```

> ⚠️ **Esto es orden de ENSEÑANZA.** «En la siguiente clase» y «temario necesario» son marcadores de
> clase, no de análisis (D-62).

### Genealogía de las ideas

- **Moat ← Warren Buffett.** «esta idea fue popularizada por Warren Buffett, quien buscaba empresas
  con un moat amplio y duradero» `[VÍDEO 10, 00:58]`. Solo-verbal: el deck no lo menciona
  `[PDF 10, p.1]`. **Única atribución externa del piloto.**
- 🆕 **Multibagger ← Peter Lynch** *(ingesta del vídeo 17, 2026-07-19)*. «este término viene de
  **Peter Lynch**, uno de los mejores gestores de la historia, el cual usaba la palabra ***bagger***
  para describir cuánto te había multiplicado una acción: un *two bagger* es un por dos, un *cinco
  bagger* es un por cinco» `[VÍDEO 17, 01:05–01:24]`. Solo-verbal (el 17 no tiene deck) →
  [[multibagger]].
  ⭐ **Es la tercera atribución externa del corpus**, tras Graham/Buffett (margen de seguridad,
  vídeo 01) y Buffett (moat, vídeo 10). **Las tres son a inversores, ninguna a literatura
  académica** — un rasgo consistente de esta fuente.
- **Herramientas externas recomendadas** (moat): «análisis **Porter**», «enfoque de **economic moat de
  Morningstar**» `[VÍDEO 10, 04:06]`. Nombradas, no explicadas. → [[moat]] §4.

---

## 4 · Mapa deck ↔ vídeos

**El deck es UN solo documento con 10 secciones numeradas, repartido en 12 vídeos.** No hay un PDF por
vídeo: hay un temario continuo del que cada vídeo toma un trozo.

| Vídeo | Sección del deck | Págs. | | Vídeo | Sección del deck | Págs. |
|---|---|---|---|---|---|---|
| 01 | *(sin numerar)* | 8 | | 07 | **5.** LA RENTABILIDAD | 7 |
| 02 | **2.** LOS 3 ESTADOS FINANCIEROS | 8 | | 08 | **6.** EL CAPEX | 10 |
| 03 | **2.** EL BALANCE | 4 | | 09 | **7.** EL FREE CASH FLOW | 4 |
| 04 | **3.** LOS ESTADOS DE FLUJOS DE CAJA | 4 | | 10 | **8.** EL MOAT | 5 |
| 05 | **3.** EL INFORME FINACIERO 10Q | 5 | | 11 | **9.** EL EQUIPO DIRECTIVO | 5 |
| 06 | **4.** LA DEUDA Y LA CAJA | 9 | | 12 | **10.** MÚLTIPLOS DE VALORACIÓN | 8 |

**Los vídeos 02+03 comparten la sección 2. Los vídeos 04+05 comparten la sección 3.** Por eso el
desfase vídeo↔sección **no es constante** (03→2, 07→5, 10→8).

> ⚠️ **Esto toca D-19**, que está `PENDIENTE DE VERIFICACIÓN` y **hipotetiza** que el desfase «sugiere
> **edición anterior del curso**». **La explicación es más simple y benigna:** el corte en vídeos no
> coincide con el corte en secciones. **No es evidencia de PDFs desactualizados.**
>
> Evidencia adicional: `[PDF 07, p.7]` trae series de precio con datos hasta **~mediados de 2025** —
> el deck está al día del vídeo. Y el modelo de fuente nuevo (el PDF **es** lo que se ve en pantalla)
> queda reforzado.
>
> **No he tocado `decisiones.md`.** Es decisión humana si esto resuelve D-19.

**Vídeos 13–19: sin PDF** (D-13). El deck termina en la sección 10 / vídeo 12.

- *Incidencia menor, para la ingesta del 05:* el deck se titula «EL INFORME **FINACIERO 10Q**» (con
  la errata «FINACIERO») mientras el slug del proyecto es `05_informe_10k`. **10Q ≠ 10K.** No he
  actuado — fuera del piloto.

---

## 5 · El marco que falta

✅ ~~`[HUECO]` **Las «cinco patas»**~~ → **RESUELTO** (lint del corpus completo, 2026-07-19; el vídeo
01 llevaba ya ingerido desde el inicio de la ingesta — este archivo solo no se había actualizado).
`radiografia.md` §C localiza en `[VÍDEO 01, 09:49]` la arquitectura que el curso enuncia: *estados
financieros → ratios → cualitativo → valoración → comparables*, con el matiz de que el vídeo 01 las
llama «unos pasos que deberemos trabajar» **pero no impone el orden**.

**El esqueleto ya está desarrollado — en [[marco_analisis_fundamental]] campo 4.1, «Las 5 patas —
nativa del vídeo 01»** `[VÍDEO 01, 09:44–10:22]`, con su cita completa y su función declarada por
pata. Lo de arriba (§§1-4 de este archivo) son las piezas de cada módulo; la pata que las cuelga a
todas vive en la ficha del 01, no aquí — este archivo registra **enseñanza**, no la arquitectura del
método (eso es [[marco_analisis_fundamental]]).

✅ ~~`[HUECO]` **Los cuatro grupos de ratios**~~ → **RESUELTO** (ingesta del vídeo 15, 2026-07-19).
Están desarrollados en **§1 · Conceptos paraguas**, con sus cuatro capturas como capa visual.

✅ ~~**El 20/80** `[VÍDEO 13, 02:47]`~~ → **RESUELTO** (ingesta del vídeo 13). Vive en
[[marco_valoracion]] campo 7, dentro del gradiente 30-40 / **40-70** / 20-80 dictaminado en `13-E1`.
⚠️ **Corrección de cita:** este archivo lo situaba en `[VÍDEO 13, 02:47]`, pero ahí empieza la frase
del **30-40 %**; el 20/80 está en **`[VÍDEO 13, 03:41–03:53]`**. Defecto de RD-2 de este archivo, no
de la fuente — corregido al verificarlo contra el `.srt`.
