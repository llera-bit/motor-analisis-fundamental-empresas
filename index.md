# index.md — Catálogo del wiki

> **Al responder una consulta: leer este índice primero**, y después abrir las páginas relevantes.
> Se actualiza en cada ingesta.

---

## Estado real del proyecto

| | |
|---|---|
| **Fichas validadas en el cerebro** | ✅ **28** — **TODAS `completo`.** Ningún `parcial`, ningún `AUSENTE EN EL VÍDEO N`: lo que queda vacío es `AUSENTE EN LA FUENTE` de verdad |
| Vídeos transcritos (`.srt` canónico) | **19 de 19** — ✅ **10, 14 y 16 puntuados a mano** (D-46), **los tres ya ingeridos** |
| Decks disponibles | **12** (vídeos 01–12) + 1 externo |
| 🏁 Vídeos **ingeridos con los moldes vigentes** | ✅ **LOS 19 DE 19.** La ingesta del corpus está **COMPLETA** (2026-07-19) |
| Moldes en firme | **6** (`moldes.md` **v12**, ✅ **RATIFICADO**, D-78) — los seis **validados contra los 19 vídeos**. El molde 5 tiene **sus tres variantes** con material real (`FILTRO` 17 · `SCORING` 18 · `REGLAS` 19) |
| Erratas de la fuente registradas | 🏁 **59** (los 19 vídeos escrutados, **58 dictaminadas** — 11 por evidencia, 19 por criterio del usuario en sesiones previas, 28 verificadas contra el audio en el pase de dictamen final, 2026-07-19). ✅ **Solo `10-E3` sigue sin dictaminar**, por decisión: tensión registrada, no pendiente por descuido |

> 🏁 ⭐ **LA INGESTA DEL CORPUS ESTÁ COMPLETA, Y EL DICTAMEN FINAL DE ERRATAS TAMBIÉN.** Los 19
> vídeos están leídos, fichados y commiteados; de las 33 erratas que seguían `PENDIENTE`, 4 resultaron
> no ser errata (`12-E3`, `07-E4`, `07-E8`, `18-E3` — el recuento bajó de 63 a 59 por depuración, no
> por descuido) y las 29 restantes quedaron dictaminadas verificando cada una contra el audio
> original. **Lo que queda ya no es dictamen de erratas: es mantenimiento normal** — lint periódico
> (`CLAUDE.md` §6.3) y, si el usuario quiere, verificar el `.srt` del vídeo 01 (única fuente nunca
> reverificada, D-46).
>
> 🔴 ⭐ **EL HALLAZGO FINAL DEL MÉTODO — el curso da reglas locales y NUNCA un árbitro entre reglas.**
> Los tres sistemas de decisión ([[multibagger]] `FILTRO` · [[medir_el_riesgo]] `SCORING` ·
> [[cuando_acumular_mantener_vender]] `REGLAS`) tienen **el mismo `[HUECO]`, en el mismo campo**: qué
> prevalece cuando varios criterios apuntan a la vez en direcciones distintas (4-de-5 · fronteras de
> banda · motivos de ramas en conflicto). **Uno sería omisión; tres, en el mismo punto, es un rasgo
> del método** — el experto enseña qué mirar y cómo leer cada señal, y **delega en el juicio del
> inversor la resolución de los conflictos**. ⛔ **No se rellena** (D-60/RD-4): inventar prioridades
> sería diseñar un método más completo que el suyo. Detalle en [[capa_decision]] §3 y `moldes.md`
> §MOLDE 5.

**✅ El bloque de MÉTRICAS (06-09) está COMPLETO**, junto con los ESTADOS FINANCIEROS (02–03–04),
el marco del método (01) y el marco de la fuente documental (05). La ingesta va **de uno en uno**
(`CLAUDE.md` §6.2).

> ✅ **Histórico — la ingesta saltó los tres `.srt` sin puntuar hasta corregirlos.** El diagnóstico de
> puntuación (2026-07-19) encontró que **10, 14 y 16** llegaban prácticamente sin signos (ratio
> 0,09–0,23 por 100 palabras, frente a un suelo de 2,63 en el resto). Los tres se puntuaron a mano
> contra el audio (D-46) y **ya están ingeridos y commiteados** — el 10 reingerido desde su pausa
> inicial. 🏁 **No queda cola: los 19 vídeos están dentro.**

> 🔴 ⭐ **HALLAZGO — una transcripción degradada puede FABRICAR erratas falsas** (reingesta del
> vídeo 10, 2026-07-19). `10-E1` acusaba al experto de un lapsus («activos tangibles» frente al
> «INTANGIBLES» de su propio deck). Al reingerir sobre el `.srt` corregido contra el audio, resulta
> que **el experto siempre dijo «intangibles»**: quien se equivocó fue la máquina de transcribir.
> **Voz y PDF nunca estuvieron en conflicto.** Consecuencias: la tasa de error estaba **inflada por
> una errata inexistente** (es la primera vez que el recuento **baja**), y la ficha **atribuía al
> experto un defecto que no cometió** — lo mismo que RD-2 existe para impedir. **Regla práctica:
> ante una errata T1 en un vídeo con transcripción no verificada, sospechar primero de la
> transcripción.** Detalle en [[erratas]] §Módulo 10.

> ⚖️ **D-73 · Regla afinada: cuándo se ELEVA una errata y cuándo se RESUELVE** (`CLAUDE.md` §5,
> `moldes.md` **v7**). El umbral para elevar **no es «hay una errata»**, es **«hay una errata que no
> puedo resolver sin el usuario»**. Si otra parte del corpus la desambigua **sin margen de duda**,
> el escritor **la corrige** y registra el estado nuevo `DICTAMINADO POR EVIDENCIA`, **citando qué
> evidencia la resuelve**. Se **eleva** cuando depende del criterio del usuario, cuando toca
> **método** y no un ejemplo, o ante **cualquier duda real**. ⛔ **Nunca se corrige con conocimiento
> externo** — eso sigue siendo RD-1. *Lo motivó `12-E1`: la voz decía «Lilly está más barata» y el
> propio deck traía los números que lo desmentían.*

> ✅ **Convención del bloque de múltiplos (12–16) — CERRADA con el vídeo 16 (2026-07-19).** Mientras
> el bloque estuvo abierto, sus fichas nacían `estado: parcial` + `transversal: true`, y usaban
> **`AUSENTE EN EL VÍDEO N`** —no `AUSENTE EN LA FUENTE`— para lo que otro vídeo del bloque podría
> traer. **Con el 16 (el que trae los «dónde NO» y los puntos ciegos que faltaban) las nueve fichas
> pasan a `completo`**: lo que sigue vacío es ya `AUSENTE EN LA FUENTE` de verdad, no una espera. ⭐
> **Hallazgo del cierre:** el EV/FCF es el único de los siete múltiplos con punto ciego **sin
> declarar** en toda la fuente — y es, precisamente, el que el experto declara preferido. Se registra
> como **rasgo del método (y de su sesgo)**, no como hueco de la ficha → [[ev_fcf]] campo 8.

> 🆕 **D-72 · Equivalencia técnica — campo nuevo en los moldes 1, 2, 3 y 4** (`moldes.md` **v6**).
> El cuerpo de cada ficha sigue usando **las palabras del experto**; un bloque aparte y marcado
> registra el **término estándar de la industria** (`[COMPLETADO-EST]`, aportación externa). Motivo:
> el cerebro es copiloto de consulta y **los datos reales llegan en terminología estándar** — sin la
> correspondencia no reconoce el dato que se le trae. **Supersede la retirada total de FCFF/FCFE**
> ordenada al cerrar `09-E1`: no se borra, se ubica donde no puede confundirse con la voz del
> experto. ⚠️ **Es el único contenido externo que vive dentro de `curso/`**, y por eso el bloque es
> extraíble de un corte — ver la nota sobre RD-3 en `moldes.md` §Equivalencia técnica.

> 🔴 **`09-E1` dictaminada — y motivó una regla nueva, D-71.** El FCF **sí resta intereses**; la
> p.2 del deck era la discrepante (contradecía su propia p.3). Esta errata hizo evidente que el
> criterio de arrastre original («¿alguien la cita explícitamente?») no bastaba: nadie cita el FCF
> por su fórmula exacta, y aun así es cimiento del DCF. **`CLAUDE.md` §5 tiene ahora dos criterios**
> — cita explícita (a) o cimiento conceptual (b). Ver el detalle en la nota de fricción del informe
> de esta ingesta.

> 👁️ **Observación abierta del molde 1** (no aplicada): el ROIC trae **dos umbrales con
> propósitos distintos** (10-15% de referencia vs. >15% sostenido = excelencia/moat) que el molde
> no distinguía. Resuelto en la ficha con una nota, no con un cambio de molde — se espera ver si
> reaparece en el bloque de múltiplos antes de tocar el molde 1 o el 4. Ver `moldes.md` §Campo 3.

> ⚠️ **El molde 6 tiene ahora DOS fichas, y no son del mismo nivel.** `marco_analisis_fundamental`
> (01) es el marco **DEL MÉTODO**. `informe_10k` (05) es el marco de **una fuente documental** — el
> documento del que salen los datos que el método analiza, no el método en sí. Mismo molde,
> **nivel distinto**: no las confundas al consultar. Ver la nota de distinción al principio de
> [[informe_10k]].

> 🔧 **La ingesta ya ha corregido el andamiaje una vez** (`moldes.md` **v5**): el campo *Ratios
> derivados* del molde 2 pasó de un desenlace a **tres**, porque los vídeos 02, 03 y 04 se
> comportaron de tres formas distintas y **ninguna** encajaba en la redacción v4.

⚠️ **Las 8 fichas que existen están en `wiki/_provisional/` y NO son válidas**: se escribieron con
moldes superados. Se rehacen en la ingesta. **No se consultan como método.**

---

## `_estructura/` — cómo se construye el cerebro

*No es contenido del curso: es el andamiaje. No le aplica RD-3.*

- **[[moldes]]** — ⭐ **FUENTE ÚNICA de los seis moldes** (**v12**). `CLAUDE.md` §4 remite aquí y no
  copia. Incluye el bloque de erratas de 4 tipos, la spec de frontmatter y las clases de
  procedencia.
- **[[radiografia]]** — diagnóstico fundacional del temario (D-55), inducido de las 19
  transcripciones. Estableció que el método **no es secuencial** y que el material pide varios
  moldes. ⚠️ Su columna *Abs/Sect* es **pre-PDF**.

### Los seis moldes y qué vídeo recibe cada uno

| Molde | Vídeos | Campos | Deck |
|---|---|---|---|
| **1 · Métrica cuantitativa** | 06, 07, 08, 09 | 15 | los 4 |
| **2 · Estado financiero** | 02, 03, 04 | 11 | los 3 |
| **3 · Cualitativo** | 10, 11 | 13 | los 2 |
| **4 · Múltiplo de valoración** | 12, 13, 14, 15, 16 | 16 | solo el 12 |
| **5 · Sistema de decisión** | **17** ✅, **18** ✅, **19** ✅ | 14 · 3 variantes | ninguno |
| **6 · Marco / arquitectura** | 01 (método) · **05** (fuente doc.) · **13** (fase de valoración) · **14** (familia de herramientas) | 12 | 01 y 05 sí; **13 y 14 no** |

> **✅ RESUELTO — el vídeo 05 usa el molde 6, a otro nivel** (dictamen de Gerard, 2026-07-19, con
> la ficha delante — D-01, D-25). No es marco del método: es marco de **la fuente documental** que
> alimenta al método (el 10-K). Se descartaron molde 7 nuevo (N=1, sin segunda instancia posible
> en el resto del corpus) y absorberlo en la ficha del 01 (rompía D-70 o el propio campo
> *Instrumental*, que exige «SIN tutorial»). Ver [[informe_10k]] para la distinción completa.

---

## `curso/` — el método del experto (RD-3)

### Documentos que no son fichas

- **[[capa_decision]]** — orden de **ANÁLISIS**, criterios de parada, reglas condicionales,
  profundidad (D-61). ⚠️ **Contiene poco a propósito**: el protocolo del curso es **mínimo**, y esa
  minimalidad es un **hallazgo**, no un hueco (D-60). 🏁 **CERRADO con el corpus completo**: las tres
  piezas del inventario (P-1, P-2, P-3) están ingeridas y **el vídeo 19 no aportó una P-4** (su
  contenido procedimental es cadencia, no orden). Aloja además **el hallazgo final** sobre la
  ausencia de arbitraje entre reglas (§3).
- **[[mapa_tematico]]** — orden de **ENSEÑANZA**, conceptos paraguas, preguntas rectoras, mapa
  deck ↔ vídeos (D-62).

### Fichas

- **[[marco_analisis_fundamental]]** — vídeo 01, molde 6. `completo`. Define el vocabulario que el
  resto del curso reutiliza (precio≠valor, margen de seguridad, valor intrínseco).
- **[[cuenta_de_resultados]]** — vídeo 02, molde 2. `completo`. Los seis niveles de beneficio
  (Ventas→EPS), el patrón de estado sano y las banderas rojas de la P&L.
- **[[balance_general]]** — vídeo 03, molde 2. `completo`. Activos/pasivos/equity, tres ratios con
  umbral (liquidez corriente, deuda/equity, solvencia) y su demostración sobre el balance real de
  Meta.
- **[[flujo_de_caja]]** — vídeo 04, molde 2. `completo`. Los tres bloques (CFO/CFI/CFF), el patrón
  de estado sano de los tres juntos, y su papel de **«filtro final»** sobre los otros dos estados.
- **[[informe_10k]]** — vídeo 05, molde 6 (⚠️ **marco de una fuente documental, no del método** —
  ver nota arriba). `completo`. Qué es el 10-K, su estructura por *items* (1, 1A, 7, 8), la
  delimitación frente al 10-Q, y la ruta de lectura — que además ingresa como **P-2** en
  [[capa_decision]].
- **[[deuda_financiera]]** — vídeo 06, molde 1. `completo`. Apalancamiento financiero, CP vs. LP,
  el riesgo de liquidez de corto plazo.
- **[[deuda_neta]]** — vídeo 06, molde 1. `completo`. Caja + deuda financiera → deuda neta, con el
  umbral Net Debt/EBITDA < 2.
- **[[enterprise_value]]** — vídeo 06, molde 1. `completo`. EV = Market Cap + Deuda neta, y su
  conexión hacia adelante con EV/EBITDA, EV/FCF, EV/EBIT (molde 4, bloque de múltiplos).
- **[[roic]]** — vídeo 07, molde 1. `completo`. Rehecha del piloto. Umbral 10-15% (dictaminado) +
  umbral secundario >15% sostenido = moat. Punto ciego: no aísla la perspectiva del accionista.
- **[[roe]]** — vídeo 07, molde 1. `completo`. Rehecha del piloto. Punto ciego: no ve la deuda de
  la compañía. Se lee siempre junto al ROIC — tesis comparativa cruzada entre las dos fichas.
- **[[capex]]** — vídeo 08, molde 1. `completo`. Expansión vs. mantenimiento (aproximado por la
  D&A — `08-E1`, dictaminada). Punto ciego: el número no distingue inversión inteligente de
  despilfarro.
- **[[free_cash_flow]]** — vídeo 09, molde 1. `completo`. FCF vs. beneficio neto — la comparación
  más limpia del bloque. `09-E1` dictaminada (el FCF sí resta intereses). Cierra el bloque 06-09.
- **[[moat]]** — vídeo 10, molde 3. `completo`. ⭐ **REINGERIDA** sobre la transcripción puntuada.
  Dos familias, **cinco tipos** (no siete: la fuente limpia lo zanja), cadena causal pricing power →
  márgenes, siete ejemplares dentro de la ficha (D-68) y el «**moat que pasa desapercibido**».
  ⚠️ Su `10-E1` es el caso que demostró que una transcripción mala puede **fabricar** erratas.
- **[[equipo_directivo]]** — vídeo 11, molde 3. `completo`. Skin in the game, los cinco aspectos de
  detección, el **único umbral cualitativo del corpus** (participación de directivos > 5%) y el
  *asset allocation* del FCF. `11-E1` dictaminada (es «Stock **Based** Compensation»).
- **[[per]]** — vídeo 12 + 16, molde 4. `completo`. **Estreno del molde 4.** Banda 16/17x **con su
  caveat pegado** — y la banda operativa real, que es la distribución histórica de la propia
  empresa. El 16 aportó **dónde NO**, **punto ciego** (deuda + caja + contabilidad creativa) y
  **tres trucos de cálculo** con su condición de validez.
- **[[ev_fcf]]** — vídeo 12 + 15 + 16, molde 4. `completo`. El múltiplo que el experto declara
  **«quizás el mejor»** — y el **único de los siete sin punto ciego declarado** en toda la fuente
  (rasgo del método, no hueco de la ficha). El 16 aportó las bandas que le faltaban. Aquí asoma la
  **contradicción del EBITDA** que `CLAUDE.md` §6.3 manda superficiar — y el propio 16 la resuelve
  citando a Buffett.
- **[[marco_valoracion]]** — vídeo 13, molde 6 (⚠️ **tercera instancia, a un nivel propio**: marco de
  **la fase de valoración**). `completo`. ⭐ **Descarta dos métodos de valoración** —valor contable y
  **DCF**— y elige múltiplos por relación esfuerzo/resultado. Trae el **criterio de profundidad más
  concreto del corpus (40-70 %)** y la **declaración de subjetividad** del método: *«si preguntabas a
  20 analistas distintos, obtenías 20 resultados distintos»*. Primer vídeo escrutado **sin deck**.
- **[[p_bv]]** — vídeo 15 + 16, molde 4. `completo`. ⭐ Trae **la primera PROHIBICIÓN explícita del
  corpus**: «no apliquéis este múltiplo en empresas con muchos intangibles». El 16 aportó la escala
  fina, la lectura por sector y **tres limitaciones**.
- **[[p_fcf]]** — vídeo 15, molde 4. `completo`. El escalón previo al EV/FCF, y el **segundo caso**
  del cuarto eje (divergencia múltiplo↔cotización) que motivó D-75.
- **[[ev_ebitda]]** — vídeo 15 + 16, molde 4. `completo`. Tres sectores nombrados (telecomunicación,
  industria, energía) y el reparto de papeles con el EV/FCF: «comparaciones rápidas» frente a
  «visión más realista». El 16 aportó la escala fina, el punto ciego y la advertencia de
  manipulación.
- **[[marco_multiplos]]** — vídeo 14, molde 6 (⚠️ **cuarta instancia**: marco de **una familia de
  herramientas**). `completo`. ⭐ **La TAXONOMÍA POR NUMERADOR** (capitalización · EV · crecimiento)
  que rellenó el campo *Familia* de las seis fichas de múltiplos, **las tres patas** con la función
  de cada una, y **seis factores de infravaloración que NO son múltiplos**. Reparte el PDF sectorial
  como `[EXTERNO-AVALADO]`.
- **[[peg]]** — vídeo 17 + 16, molde 4. `completo`. ⭐ **Caso singular: un múltiplo que llega desde
  un vídeo de decisión.** El PER ajustado por crecimiento — «versión mejorada del PER». Umbral
  `PEG < 1`, **el primer umbral del corpus SIN caveat sectorial**. Es el criterio 2 del filtro de
  multibaggers. El 16 aportó la escala completa, la prohibición y el punto ciego.
- **[[multibagger]]** — vídeo 17, molde 5, variante `FILTRO`. `completo`. ⭐ **ESTRENO DEL MOLDE 5.**
  Radar de 5 criterios para detectar multibaggers. Trae **el primer criterio de parada del corpus**
  («deuda descontrolada → pasa a la siguiente») y la **primera banda con techo** (crecer >25 % es
  alarma, no excelencia). `17-E1` dictaminada (el FCF se compara contra el beneficio neto). Su
  campo 11 (Práctica de registro) se completó con el vídeo 18 (D-76) — ver abajo.
- **[[p_s]]** 🆕 — vídeo 16, molde 4. `completo`. El comodín para empresas sin beneficios. `16-E1`
  (bandas voz↔captura) **dictaminada como GRADIENTE**: extremos sólidos (`<3` barato, `>10` caro) y
  un punto de inflexión personal (6) más exigente que el rango normalizado de mercado (4-9) de la
  captura. Combinación obligatoria con el margen neto.
- **[[ev_ventas]]** 🆕 — vídeo 16, molde 4. `completo`. La «versión mejorada» del P/S — incorpora la
  deuda. Bandas por sector (tech/software/biotech ×10-20 · retail/industria ×1-2). Único múltiplo
  del bloque sin «dónde NO» declarado.
- **[[fcf_yield]]** 🆕 — vídeo 16, molde 4. `completo`. Tensiona la taxonomía por numerador: va
  **invertido** (capitalización en el denominador), es un porcentaje y no un múltiplo tipo «x veces».
  Confirma el dictamen de `09-E1` vía `17-E6` (el «leverage FCF» resta intereses).
- **[[medir_el_riesgo]]** 🆕 — vídeo 18, molde 5, variante `SCORING`. `completo`. ⭐ **Segunda
  variante del molde 5, y la única cuya predicción de diseño se confirmó sin corrección.** Diez
  factores de riesgo binarios, suma simple → bandas 1-3/3-6/6-8/8-10 → peso en cartera (completa
  **P-3** de [[capa_decision]]). ⭐ **El contraste más nítido del corpus entre lo declarado y lo
  entregado** (campo 7): niega usar «una tabla oficial» y diez minutos después la entrega. Completa
  el campo 11 de [[multibagger]] (práctica de registro de las 4-5 razones de entrada).
- **[[cuando_acumular_mantener_vender]]** 🆕 🏁 — vídeo 19, molde 5, variante `REGLAS`. `completo`.
  ⭐ **Cierra el molde 5 y la ingesta del corpus.** Once reglas `situación → acción` repartidas en
  tres ramas: **acumular** (4 motivos), **vender** (5, el último un checklist de 9 puntos) y
  **mantener** (2, con el reencuadre «no moverse es una decisión»). Único sistema del corpus que
  opera sobre una **posición ya abierta**. Completa el campo 9 de [[multibagger]] (cadencia:
  semanal técnica / mensual fundamental) y aloja los antipatrones más explícitos del curso.

🏁 *(**No queda ningún vídeo por ingerir.** Los 19 están dentro.)*

---

## `ejemplos/` — PEDAGOGÍA, no metodología

Los casos concretos del experto (ASML, Meta, Novo Nordisk/Moderna, AMD/Intel…), **separados del
método** para que quien lo consulte no se los encuentre revueltos (D-49, D-68).

- **[[ejemplo_01_margen_seguridad_asml_alibaba]]** — ASML (margen positivo) y Alibaba (margen
  negativo), del vídeo 01.
- **[[ejemplo_02_novo_nordisk_vs_intel]]** — Novo Nordisk (consistente) vs. Intel (errático), del
  vídeo 02. Incluye la mención de Meta/Microsoft.
- **[[ejemplo_03_balance_meta]]** — el balance real de Meta (10-K 2024), con los tres ratios
  aplicados. Cifras leídas de la captura, marcadas como ilustración sin verificar.
- **[[ejemplo_04_flujo_caja_meta]]** — el flujo de caja de Meta (2024) por sus tres bloques, más
  Amazon como mención (CFI negativo sostenido, sin alarma, por tener un CFO potente).
- **[[ejemplo_05_starbucks_10k]]** — navegar la web de Investor Relations de Starbucks hasta sus
  informes anuales. Es navegación, no datos: sin ninguna cifra.
- **[[ejemplo_06_amd_intel]]** — AMD (caja neta) vs. Intel (deuda neta) y su efecto sobre el EV,
  con la corrección del rótulo mal puesto en el deck (errata `06-E4`).
- **[[ejemplo_07_novo_moderna]]** — Novo Nordisk (ROIC/ROE consistentes) vs. Moderna (erráticos
  tras el pico del COVID), la demostración de lectura cruzada citada por `moldes.md` desde su
  propio diseño.
- **[[ejemplo_08_meta_albemarle_alphabet]]** — Meta (asset-light con capex elevado), Albemarle
  (intensiva en activos físicos) y Alphabet (la sorpresa de capex que hizo caer la acción un 8%).
- **[[ejemplo_09_idexx]]** — IDEXX Laboratories, seis periodos de correlación (y desconexión) entre
  el FCF y la cotización. Puramente direccional — sin una sola cifra en juego.
- **[[ejemplo_12_per_palantir_walmart_novo_lilly]]** — el PER aplicado: Palantir (181x, qué
  significa), Walmart (el eje histórico propio) y Novo vs. Lilly (el eje competidoras). Trae tres de
  las erratas del vídeo 12 (`12-E1`, `12-E2`, `12-E3`) — dos corregidas por evidencia y una
  (`12-E3`) verificada y descartada: no era errata.
- **[[ejemplo_12_idexx_ev_fcf]]** — IDEXX otra vez, ahora con el EV/FCF contra la cotización.
  **Segunda aparición de la misma compañía en el corpus**, con gráfico distinto.
- **[[ejemplo_13_tikr_alphabet]]** — dónde viven los múltiplos y el BPA en TIKR e Investing.pro.
  Navegación sin cifras, como el de Starbucks. ⭐ Deja una decisión de método real: **usa el BPA
  normalizado, no el GAAP**.
- **[[ejemplo_17_alphabet]]** — Alphabet como hilo del radar de multibaggers. ⭐ **Demostración por
  contraste**: enseña la herramienta sobre una empresa que declara que **no** es el perfil buscado
  («ya es un monstruo»). Dos cifras en voz (PER 27,56 · net debt/EBITDA −0,44). Inaugura el campo
  *Demostración del experto* del molde 5 (D-77).
- **[[ejemplo_18_riesgos_por_factor]]** 🆕 — seis menciones puntuales, una o dos por factor de
  riesgo (Amper/Apple, ASTS/Pepsi, Tesla-Musk/CSU, Evolution/DMX), **sin una sola cifra de
  scoring**. A diferencia del 17, el vídeo 18 no aplica el sistema completo a una empresa — por eso
  el campo 12 de [[medir_el_riesgo]] queda `AUSENTE` y estas menciones viven aquí, no allí. Trae el
  primer caso del corpus en que un ejemplar (Tesla/Musk) se cita en dos vídeos (11→18).
- **[[ejemplo_19_asts_sofi_teleperformance]]** 🆕 🏁 — ocho menciones del último vídeo. ⭐ **ASTS es
  el único ejemplar del corpus que aparece en TRES vídeos (17, 18, 19)** y, dentro del 19, en **las
  tres ramas del sistema**: acumular cuando confirma contratos → vender parte cuando el peso salta
  del 5 % al 20-25 % → mantener cuando corrige pero sigue liderando. **Demuestra que las tres
  acciones son momentos de una misma tesis en el tiempo**, no categorías de compañías distintas.
  Incluye SoFi (+100 % → vende 50 %), Teleperformance, Nike→Deckers, Bitcoin/Ethereum y Michael
  Burry (usado como **contraejemplo de autoridad**).

> Un dato de empresa entra al **método** solo si **el concepto no se entiende sin él** (RD-1 §3).
> Comprobado sobre el corpus completo: **no hay ninguno definicional** — todos ilustran.

---

## `complemento/` — aportaciones externas

*(vacío por decisión)*

Contraejemplos y `[COMPLETADO-EST]` con tres pilares. **Prueba de fuego (RD-3): borrar esta carpeta
entera debe devolver el curso íntegro y coherente.**

⚠️ **Deuda pendiente aquí:** D-21 exige contraejemplos y el corpus casi no los tiene — en el moat,
**≈11 ejemplares ganadores frente a 1 perdedor** (MySpace), y ese solo está en una slide que el
experto no lee en voz alta.

---

## Artefactos vivos

- **[[erratas]]** — índice de erratas de la fuente. 🏁 **59 entradas, 58 dictaminadas** (11 de ellas
  **por evidencia**, D-73; 28 **verificadas contra el audio** en el pase de dictamen final,
  2026-07-19), en **los 19 vídeos** — cobertura completa. ✅ **Solo `10-E3` sigue sin dictaminar**,
  por decisión explícita del usuario de dejarla como tensión registrada. El recuento **bajó de 63 a
  59** por depuración (4 entradas resultaron no ser errata), no por descuido. ⚠️ Los vídeos **13, 15, 16, 17, 18 y 19 no tienen deck**: sus
  erratas salen de una sola capa contra el deck (T1/T3 imposibles), aunque el 16 sí trae T1 contra
  su **capa de capturas**. El 15, el vídeo más largo escrutado (22 min), solo dio 3 — **y eso mide
  el instrumento, no la fuente**. El 18, el mejor puntuado de todo el corpus, dio solo 3, todas T4
  triviales. Cuatro tipos (voz↔PDF · voz↔voz · PDF↔PDF · ambigüedad de transcripción) con su estado.
  🆕 `16-E1` es el primer caso de **gradiente dictaminado contra una capa de capturas**, no solo
  entre vídeos. 🆕 El 18 aporta el primer caso del corpus de **ambigüedad de contenido registrada a
  propósito FUERA de la tabla de erratas** (fronteras de banda, «puntito más») — no encaja en los
  4 tipos y se deja como `[HUECO]` en la ficha, sin forzar la taxonomía.
  ⚠️ **Lleva su propio aviso de cómo NO leer el recuento**: mide la fuente **y el método**. Ahora
  también lleva la **regla de arrastre (D-71)**: cuándo una errata se eleva de inmediato.
- **[[capturas_pendientes]]** — qué falta capturar. ✅ **El balance de Meta del vídeo 03 (la más
  importante) ya está resuelta.** Quedan las de prioridad media/baja (vídeos 10 y 07).

---

## `_provisional/` — no consultar como método

Las **8 fichas** escritas con moldes superados: `deuda_financiera` · `caja` · `deuda_neta` ·
`enterprise_value` (módulo 06) y `roic` · `roe` · `balance_general` · `moat` (piloto).

✅ **Las 8 están ya `⛔ SUPERSEDIDAS`** con marcador y traza hacia su ficha nueva: las cuatro del
módulo 06, `balance_general`, `roic`/`roe`, y **ahora `moat`** — que además está **doblemente
superada** (su rehechura se reingirió sobre la transcripción puntuada). **La carpeta queda cerrada:
ninguna ficha piloto sigue viva.**

**Su README detalla, una por una, qué las invalida y su estado actual.** Conservan sus citas
verificadas y el trabajo de contraste voz↔deck, pero **se rehacen desde cero** en la ingesta.

---

## `_archivo/` — superado, con traza

| Documento | Estado |
|---|---|
| `protocolo_analisis.md` | ⛔ **SUPERSEDIDO** por `capa_decision.md` (D-61). Nació de una hipótesis que la radiografía descartó. Se conserva como lápida |
| `inventario_atomico.md` | ❄️ **CONGELADO** (D-69). Huérfano: los moldes v4 no tienen campo «inputs atómicos» |
| `sondeo_procedimental.md` | 📖 **CONSULTABLE** — ⚠️ **al ingerir 14, 15 y 17**: su clasificación es materia prima aprovechable |
| `piloto/` | 📦 Los artefactos del piloto de moldes (fricción, erratas, registro de organización) |

*(`_archivo/whisper/` vive en la **raíz** del repositorio: es herramienta, no wiki — D-45.)*

---

## Las fuentes y su fiabilidad de lectura (RD-1 §2)

**Cada subcarpeta de `raw/` declara su clase en su propio README.**

| Fuente | Clase | Cita |
|---|---|---|
| Transcripción `.srt` | **PLENA** | `[VÍDEO NN, mm:ss]` |
| Capa de texto de un deck | **PLENA** | `[PDF NN, p.X]` |
| Gráfico dentro de un deck | ⚠️ **CAUTELA** | `[PDF NN, p.X · IMAGEN]` |
| Captura de pantalla | ⚠️ **CAUTELA** | `[CAPTURA NN_nombre]` |

> ⛔ **Ninguna cifra se extrae a ciegas de una fuente CAUTELA**: se marca y se eleva.
> ⚠️ **Muerde ya en el bloque de múltiplos**: las capturas cubren **14, 15 y 16**, que **no tienen
> deck** — ahí la única capa visual es la de cautela.

---

## Por dónde sigue

**Ingesta secuencial, de uno en uno** (`CLAUDE.md` §6.2): 01–09 cerrados — marco del método, marco
de la fuente documental, trilogía de estados financieros, y el **molde 1 completo** (06-09: deuda
en cadena, ROIC/ROE bifurcados, capex y FCF de ficha única cada uno). **Más el 11**, que estrena de
hecho el molde 3 en el corpus commiteado.

**El 12 cierra el estreno del molde 4** — y con él, **los seis moldes han recibido ya material
real**. *(En este punto de la ingesta el 10 estaba en pausa, pendiente de reingesta sobre el `.srt`
puntuado — ✅ ya reingerido y commiteado, ver más abajo.)*

**El 13 demostró que un vídeo del «bloque múltiplos» puede no ser un múltiplo** (resultó ser marco) y
**el 15 que puede no caber en un molde solo** (es un vídeo de **amplitud**: ~20 ratios repartidos
entre la taxonomía de [[mapa_tematico]] §1, tres fichas nuevas y tres enriquecimientos). **No se
asume el molde por el bloque temático.**

**El 17 estrenó el molde 5** (variante `FILTRO`) — con él, **los seis moldes tienen ya al menos una
ficha real**. Trajo el **primer criterio de parada** del corpus y **corrigió una predicción de
diseño** (la agregación del FILTRO no era «conjunción»).

✅ **El bloque de múltiplos (12–16) queda CERRADO con el vídeo 16.** Las nueve fichas son
`completo`. El 16 fue el tramo más largo escrutado (38,5 min) y el que más umbrales trajo de un
solo vídeo; su única errata, `16-E1` (bandas del P/S, voz↔captura), quedó **dictaminada como
gradiente**, no como contradicción. Es también donde el campo de **equivalencia técnica** (D-72) más
trabajó: el usuario trae los múltiplos desde un screener, con su nombre estándar (`PER`→**P/E**,
`PER Forward`→**Forward P/E**).

✅ **El 18 estrenó `SCORING`, la segunda variante del molde 5** — y esta vez la predicción de diseño
**se confirmó tal cual**, sin corrección (al contrario que el FILTRO en el 17): 10 factores
binarios, suma con bandas, salida número → peso en cartera. Completó **P-3**, la última pieza que le
faltaba a [[capa_decision]] — el inventario procedimental del curso queda cerrado. También completó
la práctica de registro de [[multibagger]] (D-76).

🏁 **El 19 cerró `REGLAS`, la ingesta y el corpus.** Su predicción también se confirmó (disyunción),
completó la **cadencia** de [[multibagger]] (D-76) y destapó, al poder ya comparar las tres
variantes, **el hallazgo final sobre la ausencia de arbitraje** (arriba). **De las tres predicciones
de agregación del molde 5, dos acertaron y una falló** — y la que falló (el FILTRO) lo hizo por
atribuir al experto una regla que nunca dijo.

---

## 🏁 Y ahora qué — la ingesta terminó, el trabajo no

**No queda ni un vídeo por leer.** Lo que sigue es de otra naturaleza:

| Qué | Estado |
|---|---|
| **Dictamen final conjunto de erratas** | 🏁 ✅ **HECHO (2026-07-19).** De 33 `PENDIENTE`, 4 no eran errata (recuento 63→59) y 29 quedaron dictaminadas verificando cada una contra el audio original. **Solo `10-E3` sigue sin dictaminar**, por decisión — ver [[erratas]] |
| **Ratificar `moldes.md`** | ✅ **HECHO (D-78, 2026-07-19).** Validado contra los 19 vídeos sin necesitar ni un campo nuevo en su última versión |
| **Pasada de lint del corpus completo** | ✅ **HECHO (2026-07-19)** y sus hallazgos ya corregidos: sincronización de umbrales, seis equivalencias técnicas rellenadas, enlaces cerrados, stale corregido en `CLAUDE.md`/`mapa_tematico.md`. Queda como **rutina periódica** (`CLAUDE.md` §6.3), no como pendiente puntual |
| **Verificar el `.srt` del vídeo 01** | 🔴 Puntuación intermedia (2,63), **nunca reverificado contra el audio** — el único cabo suelto de fiabilidad de fuente que queda en todo el corpus (D-46) |
| **Deuda D-21: contraejemplos** | `complemento/` sigue vacío por decisión. El corpus enseña con ganadores: ~11 ejemplares positivos frente a 1 negativo en el moat |
| **Capas de uso (D-59)** | Aparcadas por decisión. El cerebro está construido; **cómo se consulta es otra fase** |

*Protocolo de ingesta: `CLAUDE.md` §6.2. **De uno en uno, nunca en lote sin revisión.** — cumplido
en los 19.*
