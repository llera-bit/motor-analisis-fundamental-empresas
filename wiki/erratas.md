# erratas.md — Índice de erratas de la fuente

> **Índice derivado.** El detalle y la evidencia de cada errata viven **en la ficha donde se usa el
> concepto** (`CLAUDE.md` §5): *la corrección vive donde se usa, no archivada lejos.* Aquí solo el
> recuento, para poder medir.
>
> ⛔ **Las erratas se REGISTRAN, no se resuelven.** El escritor **no dictamina** cuál versión es
> correcta — sería aportar criterio propio (RD-1). El dictamen es **humano**.

## Los cuatro tipos

| Tipo | Qué choca | ¿Hay jerarquía que decida? |
|---|---|---|
| **T1** · voz ↔ PDF | La voz y el deck se contradicen | ⚠️ **Sí, pero NO automática**: gana la voz **por defecto**, salvo `CANDIDATO A LAPSUS` → dictamen humano |
| **T2** · voz ↔ voz | El experto se contradice a sí mismo | ⛔ **No.** Los dos polos son voz: el cuerpo lleva los dos |
| **T3** · PDF ↔ PDF | Inconsistencia interna del deck | ⚠️ Solo si la voz hace de testigo de uno |
| **T4** · ambigüedad de transcripción | El `.srt` no determina qué dijo | ⛔ **No.** Se cita en crudo con las lecturas posibles |

**Estados:** `PENDIENTE DE REVISIÓN HUMANA` · `CANDIDATO A LAPSUS` · `DICTAMINADO` ·
`DICTAMINADO POR EVIDENCIA` · 🏁 `DICTAMINADO — VERIFICADO CONTRA EL AUDIO` (el usuario volvió al
vídeo original a comprobarlo; la evidencia más fuerte del proyecto) · 🏁 `SIN DICTAMEN — TENSIÓN
REGISTRADA` (decisión explícita de no elegir ganador entre dos lecturas, distinta de dejarla
pendiente por no haberla mirado) · ⛔ `NO ES ERRATA` (verificada y descartada; sale del recuento,
la fila no se borra). Una entrada **no se borra al dictaminarse**: sigue contando para la
tasa de error, salvo que pase a `NO ES ERRATA`.

> ⚖️ **Regla afinada de elevación (D-73, `CLAUDE.md` §5):** el umbral para elevar **no es «hay una
> errata»**, es **«hay una errata que no puedo resolver sin el usuario»**. Si otra parte del corpus
> la desambigua **sin margen de duda**, el escritor **la corrige** y registra `DICTAMINADO POR
> EVIDENCIA`, citando qué evidencia la resuelve. **Se eleva** cuando depende del criterio del
> usuario o de su escucha del audio, cuando toca **método** y no un ejemplo, o ante **cualquier duda
> real**. ⛔ **Nunca se corrige con conocimiento externo al corpus** — eso sigue siendo RD-1.

> 🔴 **Regla de arrastre (D-71, `CLAUDE.md` §5):** por defecto, una errata nueva se acumula aquí
> `PENDIENTE`. **Se eleva de inmediato**, antes de cerrar la ficha, si (a) el experto la cita
> explícitamente hacia adelante, o (b) afecta a una definición que otros conceptos del corpus dan
> por cimiento — aunque nadie la cite. Marcada `¿Arrastra?` en cada tabla de módulo.

---

## Módulo 06 — La Deuda y la Caja

*Detectadas en la primera ingesta. **Las cuatro dictaminadas**: deck erróneo, voz correcta.*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **06-E1** | T1 | Fórmula del EV: el deck imprime `EV = MARKET CAP – NET DEBT` `[PDF 06, p.5]`; la voz dice «market cap **más** la deuda neta» `[VÍDEO 06, 06:21]` | ✅ **DICTAMINADO** — gana la voz |
| **06-E2** | T1 | Definición de deuda neta: la **prosa** del deck dice «restarle **a la caja** la suma de todas las deudas» `[PDF 06, p.4]`, invertida respecto a su **propio recuadro** en la misma página | ✅ **DICTAMINADO** — gana el recuadro / la voz |
| **06-E3** | T1 | Las dos cajas de decisión MC/EV de `[PDF 06, p.5]` son incompatibles con la fórmula errónea de E1 | ✅ **DICTAMINADO** — las cajas son correctas; la incoherencia es interna |
| **06-E4** | T1 | `[PDF 06, p.9]` rotula **los dos paneles «AMD»**; el derecho es **Intel**. La voz lo corrige en directo `[VÍDEO 06, 08:50]` | ✅ **DICTAMINADO** — es Intel |

> ⚠️ El paréntesis de `[VÍDEO 06, 09:41]` —*«(en el pdf sale AMD, esto está mal…)»*— es una
> **`[ANOTACIÓN-EDITORIAL]` del usuario**, no una frase del experto. Sirve de indicio; **no se cita
> como afirmación suya**.

---

## Módulo 07 — ROIC vs ROE

*🏁 **Pase de dictamen final (2026-07-19), verificado contra el audio.** Detalle completo en
[[roic]] y [[roe]] (repartidas entre las dos, ver nota de cada ficha). **Dos dejan de ser
errata**: `07-E4` (criterio de inclusión de muestra, no umbral) y `07-E8` (límite del vídeo
original, no de la transcripción) — sacadas del recuento.*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **07-E1** | T1 | «empresas» (voz `07:00`) vs «**Industrias**» (título del gráfico, `[PDF 07, p.5]`) | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — COMPATIBLE**: generalización coloquial, no error conceptual → [[roic]] |
| **07-E2** | T1 | «filtro para **detectar empresas de calidad**» (voz `03:08`) vs «filtro para **al menos descartar empresas mediocres**» (`[PDF 07, p.2]`) | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — COMPATIBLE**: dos formulaciones de la misma acción, registradas las dos (patrón `01-E2`) → [[roe]] |
| **07-E3** | T1 | **Postura sobre el ROE**: el deck lo llama «una métrica muy buena» `[PDF 07, p.2]`; la voz dice «**no me gusta el ROE**» `[05:43]` | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — GANA LA VOZ**: el deck es plantilla genérica → [[roe]] |
| **07-E4** | ~~T1~~ | El gráfico de ROE está filtrado a «**ROE > 15 %**» `[PDF 07, p.6]` y la voz nunca enuncia ese umbral | ⛔ **NO ES ERRATA — VERIFICADO CONTRA EL AUDIO.** Es el criterio de inclusión de la muestra del gráfico, no un umbral recomendado — aporte de una sola capa. **Sacada del recuento** → [[roe]] |
| **07-E5** | **T2** | ⭐ «promedio de mercado» = **13-15 %** `[03:49]` vs **8-10 %** `[07:28]` | ✅ **DICTAMINADO** — consolidado en **10-15 %** |
| **07-E6** | T2 | «estas dos primeras» `[02:18]` no son las dos primeras de su propia enumeración | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — trivial, sin impacto** → [[roic]] |
| **07-E7** | T3 | El deck define la rentabilidad financiera y la reformula con la fórmula de la **económica** `[PDF 07, p.1]` | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — ERROR DE DECK** (rótulo/fórmula intercambiados, patrón `02-E1`) → [[roe]] |
| **07-E8** | ~~T4~~ 🔧 **Límite de fuente** *(reclasificada; se registró como T4)* | «consistencia en el tiempo» — el vídeo se corta a mitad de frase | ⛔ **NO ES ERRATA — VERIFICADO CONTRA EL AUDIO.** El vídeo original se corta a mitad de palabra; el `.srt` era fiel a ese corte. **Sacada del recuento** → [[roe]] |
| **07-E9** | T4 | «el **WAC**» ×2 `[07:12]`, `[10:54]` — sin ancla en el deck | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** Es **WACC**. `.srt` canónico corregido (D-46) → [[roic]] |

---

## Módulo 03 — Balance general

*🏁 **Pase de dictamen final (2026-07-19), verificado contra el audio.** Detalle en
[[balance_general]].*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **03-E1** | T1+T3 | Activos no corrientes: «más de un año» (voz `01:11`) vs «MÁS DE 1 AÑO **MENOS DE 12 MESES**» (`[PDF 03, p.1]`, **contradictoria consigo misma**) | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — GANA LA VOZ.** El PDF es internamente imposible; resto de copy-paste de la definición de activos corrientes |
| **03-E2** | T3 | `[PDF 03, p.1]` nombra un conjunto de partidas de activos; `[PDF 03, p.3]` (con «Entre otros») nombra un conjunto parcialmente distinto | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — COMPATIBLE + ENRIQUECIDA.** El «Entre otros» declara la lista no exhaustiva. Todas las partidas nombradas entre p.1 y p.3 se consolidaron en el campo 3 de [[balance_general]], citando su página |

---

## Módulo 10 — El Moat

*⚠️ **Registro revisado tras la REINGESTA sobre la transcripción puntuada** (2026-07-19). Las
entradas originales se detectaron sobre un `.srt` **sin ni una coma**; el usuario lo corrigió a mano
contra el audio (D-46) y la ficha se rehízo. **Dos entradas cambian de estado y una cambia de
tipo.** Detalle completo en [[moat]].*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **10-E1** | 🔧 **T4** *(reclasificada; se registró como T1)* | ⭐ La transcripción de **máquina** ponía «activos **tangibles**»; la **corregida contra audio** dice «activos **intangibles**» `[01:20]`, que **coincide con** `[PDF 10, p.2]` | ✅ **DICTAMINADO POR EVIDENCIA** — 🔴 **NO era un lapsus del experto: era un error de máquina.** Voz y PDF **siempre coincidieron**. Ver el aviso de abajo |
| **10-E2** | **T4** | ⭐ Sin puntuación, «dos familias» vs «lista de efectos» no era decidible `[01:10]` | ✅ **DICTAMINADO** — **sí hay dos familias**. **Confirmado** por la puntuación de la fuente corregida (`en aquellas que: …, también …`) |
| **10-E3** | T1 | ASML: «**toda la producción** de máquinas de litografía» (voz `04:19`) vs «**la máquina más importante**, la EUV» (`[PDF 10, p.3]`) | ⚖️ **SIN DICTAMEN — TENSIÓN REGISTRADA (decisión del usuario, 2026-07-19), verificado contra el audio.** Se registran las dos lecturas, sin elegir ganador — es ejemplo, no método: importa el concepto, no la situación exacta de esta compañía → [[moat]] |
| **10-E4** | T3 | «SECTOR LUJO» se desarrolla (`p.3`) y **no está en la taxonomía** (`p.2`); «PATENTES/LICENCIAS» está en la taxonomía y **no se desarrolla** | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — constatación, sin dictamen de fondo.** Deck incompleto en ambas direcciones |
| **10-E5** | T3 | La cabecera «AUMENTO DE INGRESOS» (`p.2`) **no cubre** «BAJOS COSTES» ni «ALTOS COSTES DE SUSTITUCIÓN», que contiene | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — trivial, sin impacto** |
| **10-E6** | T4 | «mejores retornos **a jugadores**» `[06:25]` — cierre corrupto | ✅ **DICTAMINADO POR EVIDENCIA** — **el corrupto no existía**: la fuente limpia cierra «suelen generar mejores retornos.» |
| **10-E7** 🆕 | T4 | «**Salesforce**» ×2 `[02:08 · 05:08]` | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido en las dos apariciones (D-46) |

> ### 🔴 ⭐ APRENDIZAJE — una transcripción degradada no solo OCULTA: puede FABRICAR erratas falsas
>
> **`10-E1` acusaba al experto de un defecto que no cometió.** Se registró como *lapsus verbal* —el
> experto habría dicho «tangibles» donde su propio deck decía «intangibles»— y así se dictaminó. La
> fuente corregida contra el audio demuestra que **el experto siempre dijo «intangibles»**: quien se
> equivocó fue **la máquina de transcribir**.
>
> **Consecuencias, y ninguna es menor:**
>
> 1. **La tasa de error de la fuente estaba INFLADA por una errata inexistente.** El proyecto mide
>    «cuántos defectos tiene el corpus»; ésta no era del corpus, era del instrumento. `erratas.md`
>    ya avisaba de que *la cuenta mide la fuente **Y** el método con que se buscó* — **este es el
>    primer caso demostrado de esa contaminación**, y en la dirección más incómoda: **sobre**contar.
> 2. **Atribuyó al experto un error que no era suyo**, que es justo lo que RD-2 y la regla de
>    `[ANOTACIÓN-EDITORIAL]` existen para impedir. El mecanismo aquí fue distinto (no una anotación
>    del usuario, sino ruido de máquina), pero **el daño es el mismo: una afirmación falsa sobre lo
>    que el experto dijo, indetectable después**.
> 3. **La jerarquía voz > PDF se aplicó sobre un polo que no existía.** El dictamen «gana el PDF»
>    fue correcto en su resultado, pero por la razón equivocada: no había conflicto que arbitrar.
>
> **Regla práctica que deja:** ⚠️ **ante una errata T1 en un vídeo cuya transcripción no esté
> verificada contra el audio, sospechar primero de la transcripción y solo después del experto.**
> Un `[VÍDEO NN, mm:ss]` procedente de un `.srt` degradado **no es fuente PLENA de facto**, aunque
> el marcador lo diga.

---

## Módulo 01 — Marco del análisis fundamental

*Detectadas en la ingesta del vídeo 01 (2026-07-18). **Las tres dictaminadas por Gerard el mismo
día.** Detalle completo, con las citas, en [[marco_analisis_fundamental]].*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **01-E1** | T1 | Definición de «valor»: la voz lo ancla a «capacidad de poder generar beneficios futuros» `[VÍDEO 01, 05:01]`; el PDF lo describe como «lo que estamos dispuestos a pagar» `[PDF 01, p.5]`, que se confunde con *precio* | ✅ **DICTAMINADO** — gana la voz; el PDF queda como formulación secundaria, más débil |
| **01-E2** | T2 | Margen de seguridad de Alibaba: 46% se calcula sobre el precio de compra `[VÍDEO 01, 08:49]`, mientras el resto del vídeo lo calcula sobre el valor real (ASML ×2, Alibaba segundo caso) | ✅ **DICTAMINADO** — son dos formulaciones equivalentes e intencionales (margen sobre valor / rendimiento sobre lo pagado), no un desliz |
| **01-E3** | T4 | El `.srt` transcribe «Katy Wood» `[VÍDEO 01, 04:30]`; no corresponde a ninguna gestora conocida | ✅ **DICTAMINADO** — es **Cathie Wood**, verificado contra el audio |

---

## Módulo 02 — Cuenta de resultados

*Detectada en la ingesta del vídeo 02 (2026-07-18). **Dictaminada por Gerard el mismo día.**
Detalle completo, con las citas, en [[cuenta_de_resultados]].*

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **02-E1** | T3 | EBIT y Beneficio Neto se rotulan «Income» (cantidad absoluta) en `[PDF 02, p.3]` y `[PDF 02, p.4]`, y «Margin» (%) en `[PDF 02, p.5]` — misma slide casi duplicada | ✅ **DICTAMINADO** — error de rotulación en la p.5, no una equivalencia. Gana «Income»; la voz lo confirma |

---

## Módulo 04 — Estado de flujos de caja

*Detectadas en la ingesta del vídeo 04 (2026-07-18). **Las dos son `NO ARRASTRA`** (regla
permanente de erratas): quedan acumuladas para el dictamen final conjunto, no se elevan sueltas.
Detalle completo, con las citas, en [[flujo_de_caja]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **04-E1** | 🔧 **T2** *(reclasificada; se registró como T4)* | «Meta ha recomprado más de 30 mil millones de **acciones**» `[VÍDEO 04, 07:04]` | **NO** — cifra de ejemplo, no toca ninguna definición ni umbral | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** 🔴 **NO era transcripción: es lapsus del experto.** Dice literalmente «acciones», refiriéndose a 30 mil millones de **dólares**. El `.srt` es fiel, no se toca. **Cuenta para la tasa de error** (a diferencia de una errata de transcripción) → [[flujo_de_caja]] |
| **04-E2** | T4 | «que voy a subir para aquí porque no veis con el logo de **CIC**» `[VÍDEO 04, 07:56]` — «CIC» no aparece en el resto del corpus | **NO** — solo identifica el origen de una cifra ya dicha completa en voz | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — irresoluble, sin impacto.** Sigue sin identificarse; se cierra así, no queda `PENDIENTE` indefinidamente (el corpus está completo) |

---

## Módulo 05 — El informe 10-K

*Detectadas en la ingesta del vídeo 05 (2026-07-19). Detalle completo, con las citas, en
[[informe_10k]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **05-E1** | T1 | «el 10K es un resultado trimestral y el 10Q son los resultados anuales» `[VÍDEO 05, 02:40]` — invertido respecto al deck `[PDF 05, p.4]` y al resto de la propia voz (`[02:47]`, `[03:06]`) | **SÍ arrastraba** — resuelto antes de escribir la ficha | ✅ **DICTAMINADO** — es lapsus verbal. 10-K = anual, 10-Q = trimestral. *Resuelto por Gerard, 2026-07-19* |
| **05-E2** | T3 | Las 5 páginas del deck llevan la cabecera «EL INFORME FINACIERO **10Q**» siendo el contenido del **10K** | **NO** — rótulo de cabecera, no afecta ninguna definición | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — ERROR DE PLANTILLA.** Mismo patrón que `05-E1`. Gana el contenido (10-K) |

---

## Módulo 08 — CAPEX

*Detectadas en la ingesta del vídeo 08 (2026-07-19). `08-E1` dictaminada el mismo día; las otras
cinco, `NO ARRASTRA`, acumuladas para el dictamen final conjunto. Detalle completo, con las
citas, en [[capex]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **08-E1** | T1 | El deck iguala sin reserva «CapEx de mantenimiento **(D&A)**» `[PDF 08, p.8]`; la voz matiza: «una aproximación **más o menos**» `[VÍDEO 08, 04:58]` | **SÍ, arrastraba** hacia el vídeo 09 (FCF ajustado) | ✅ **DICTAMINADO** — gana la voz: aproximación, no igualdad |
| **08-E2** | T3 | `[PDF 08, p.6]` rotula «5. EL CAPEX» — el resto del deck dice «6.» | **NO** | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — trivial**, error de numeración de sección |
| **08-E3** | T4 | «el WACC» `[VÍDEO 08, 08:53]` — tercera aparición del término (dos en el 07, `07-E9`) | **NO** | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido (D-46) |
| **08-E4** | 🔧 **T2** *(reclasificada; se registró como T4)* | «el de Meta... el de Meta» al comparar 588M con 15.500M `[VÍDEO 08, 07:12]` | **NO** — cifra de ejemplo | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** 🔴 **Lapsus de voz, no de máquina:** dice «Meta» las dos veces; la primera cifra (588M) es de **Albemarle**, la segunda (15.500M) de Meta. `.srt` fiel, no se toca. **Cuenta para la tasa de error** → [[ejemplo_08_meta_albemarle_alphabet]] |
| **08-E5** | T4 | «Meta, **Adobe**, Microsoft o Visa» `[VÍDEO 08, 04:04]` | **NO** | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido (D-46) |
| **08-E6** | T4 | «capex... de 75 billones... 58 billones» `[VÍDEO 08, 07:58]` — «billón» español = 10¹² | **NO** — cifra de ejemplo | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — lapsus del experto, cifra NO se corrige.** Quiso decir «mil millones» (billions americanos) |

---

## Módulo 09 — Free Cash Flow

*Detectada en la ingesta del vídeo 09 (2026-07-19), dictaminada el mismo día. Cierra el bloque de
métricas (06-09). Detalle completo, con las citas, en [[free_cash_flow]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **09-E1** | T1+T3 | `[PDF 09, p.2]` define el FCF «sin deuda» y sin restar intereses; la voz y `[PDF 09, p.3]` (el mismo deck) sí restan intereses — el deck se contradice entre sus propias páginas | 🔴 **SÍ, criterio (b)** — el FCF es cimiento explícito del DCF `[09, 06:00]` | ✅ **DICTAMINADO** — gana la voz + p.3. El FCF sí resta intereses; p.2 queda como formulación discrepante del deck |

---

## Módulo 11 — El Equipo Directivo

*Detectada en la ingesta del vídeo 11 (2026-07-19), dictaminada el mismo día. Cierra el bloque
cualitativo por la parte del 11 (el **10 queda pendiente de reingesta** tras puntuar su `.srt`).
Detalle completo, con las citas, en [[equipo_directivo]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **11-E1** | T1+T4 | «stock **based** compensation» `[VÍDEO 11, 03:09]` vs «Stock **Basic** Compensation» `[VÍDEO 11, 03:25]` — 16 segundos después, mismo hablante; `[PDF 11, p.4]` refuerza la **segunda** forma | **NO** — disputa léxica sobre una palabra; la definición sustantiva de SBC es correcta en las dos capas | ✅ **DICTAMINADO** — es **«Stock BASED Compensation»**. *Resuelto por Gerard, 2026-07-19* |

> ⭐ **Caso poco habitual: las DOS capas repiten el mismo desliz.** Aquí la jerarquía voz > PDF no
> podía desempatar (el deck coincide con la voz errónea). El testigo que decide es **la propia voz
> 16 segundos antes**, más el uso ya asentado en [[flujo_de_caja]]. Es el primer precedente del
> corpus en que **el desempate viene de otro punto de la misma voz**, no de la otra capa.

---

## Módulo 12 — Múltiplos de valoración

*Detectadas en la ingesta del vídeo 12 (2026-07-19), **estreno del molde 4**. ⚖️ **Primer módulo
tratado bajo la regla afinada D-73**: tres se resolvieron con evidencia del propio corpus y **están
corregidas en el cuerpo**; una queda sin dictamen. **Ninguna se elevó.** Detalle completo, con las
citas y la evidencia de cada dictamen, en [[per]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **12-E1** | T4 | El `.srt` transcribía «Novo Nordisk parece más barata, mientras que **Lilly está más barata**» `[VÍDEO 12, 04:28]` — las dos no pueden serlo | **NO** — lectura de un ejemplo | ✅ **DICTAMINADO POR EVIDENCIA** — es «Lilly está **cara**». Lo resuelven los propios números leídos en voz (36,62 vs. media 29,22) y el rótulo `[PDF 12, p.7]`. ⭐ **Corregida además EN LA FUENTE** por Gerard contra el audio (D-46): el `.srt` canónico ya dice «cara» |
| **12-E2** | T3 | `[PDF 12, p.7]` rotula «**NVO**» en los **dos** rótulos del gráfico | **NO** — rótulo de un ejemplo | ✅ **DICTAMINADO POR EVIDENCIA** — el superior es **LLY** (línea negra a ~36x, coincidente con `LLY Last: 36,62x`). Precedente `06-E4` |
| **12-E3** | ~~T1~~ | PER medio de Walmart: «**22,9x**» (voz + rótulo) vs. «**Mean: 22,29x**» (captura TIKR, `[PDF 12, p.6 · IMAGEN]`) | **NO** — cifra de ejemplo | ⛔ **NO ES ERRATA — VERIFICADO CONTRA LA CAPTURA (2026-07-19).** Es la misma cifra, distinta precisión — no hay transposición de dígitos. **Sacada del recuento** |
| **12-E4** | T4 | «**Idex** Laboratories» `[VÍDEO 12, 05:31]` | **NO** — nombre propio, inocuo | ✅ **DICTAMINADO POR EVIDENCIA** — es **IDEXX**, ya establecida así en [[ejemplo_09_idexx]]. Precedente `08-E5` |

> ⭐ **`12-E1` es el caso que originó D-73.** Bajo la regla anterior se habría elevado; pero el deck
> traía los números que la desmentían (36,62 > 29,22) — **el corpus se desambiguaba solo**. Elevarla
> habría sido trasladar al usuario una lectura que la fuente ya cerraba.

---

## Módulo 13 — Múltiplo y BPA

*Detectadas en la ingesta del vídeo 13 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): **T1 y T3 son
estructuralmente imposibles** — que no haya ninguna de esos dos tipos **no dice nada** sobre la
calidad de esta fuente. Detalle completo en [[marco_valoracion]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **13-E1** | **T2** | **Tres cuantificaciones del alcance suficiente** en 60 segundos: **30-40 %** `[02:49]` · **40-70 %** `[03:18]` · **20/80** `[03:41]` | 🔴 **SÍ, criterio (b)** — el criterio de profundidad es cimiento de [[capa_decision]] §2.2 y [[marco_analisis_fundamental]] campo 7. **Se elevó, no se acumuló** | ✅ **DICTAMINADO** — **NO es contradicción: es un GRADIENTE compatible.** Estándar operativo fijado: **40-70 %**. *Resuelto por Gerard, 2026-07-19* |
| **13-E2** | T4 | «vais a aquí arriba, **pestaña** Earnings» `[VÍDEO 13, 13:01]` | **NO** — ruta de interfaz, descartada del método por diseño | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido (D-46) |
| **13-E3** | T4 | «un vídeo dedicado a **destripar** esta plataforma» `[VÍDEO 13, 12:05]` | **NO** — anuncio de material futuro | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido (D-46) |

> ⭐ **`13-E1` valida la regla de arrastre Y la de elevación a la vez.** Arrastraba (criterio b), así
> que se elevó en vez de acumularse; y **no era resoluble por evidencia** (sin deck, podía ser
> interpretación, tocaba método) — los tres supuestos de D-73. **El dictamen confirmó que en efecto
> era interpretación y no error.** Corregir por cuenta propia habría inventado una contradicción que
> no existía.

---

## Módulo 14 — ¿Cuándo usarlos?

*Detectadas en la ingesta del vídeo 14 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 y T3
imposibles. ⭐ **Estrena un patrón: T2 ENTRE VÍDEOS** — umbrales del mismo ratio dados en módulos
distintos, un choque que **solo aparece cuando el corpus está lo bastante ingerido para cruzarlos**.
Detalle completo en [[marco_multiplos]] §11.*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **14-E1** | **T2 entre vídeos** | **Deuda/Patrimonio**: `< 1` (vídeo 14) vs `< 1,5` ([[balance_general]], vídeo 03) | 🔴 **SÍ (b)** — umbral de método ya fichado | ✅ **DICTAMINADO — GRADIENTE COMPATIBLE.** Ideal `<1` · aceptable `<1,5`. La propia voz del 14 lo enuncia: «menor a uno **es lo ideal**, aunque **tampoco es malo ligeramente por encima**». *Gerard, 2026-07-19* |
| **14-E2** | **T2 entre vídeos** | **PER**: `< 15` = barato (vídeo 14) vs escala `<10`/`10-20`/`>20` ([[per]], vídeo 15) | 🔴 **SÍ (b)** — umbral de método ya fichado | ✅ **DICTAMINADO — ATAJO vs. ESCALA.** El `<15` es un **atajo orientativo declarado como tal** por el experto; **la escala del 15 es la referencia principal**. *Gerard, 2026-07-19* |
| **14-E3** | T4 | «hacer una **modilización** buena» `[14, 02:48]` | **NO** | ✅ **DICTAMINADO POR EVIDENCIA** — es **modelización**, usada bien por el experto en [[marco_valoracion]] `[13, 09:52]` |
| **14-E4** | T4 | «hasta que tengamos **más manga ancha**» `[14, 04:44]` | **NO** | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** Es el idiom «manga ancha». `.srt` canónico corregido (D-46) |

> ⭐ **Las dos T2-entre-vídeos se resolvieron como COMPATIBLES, y eso fija criterio para el bloque.**
> Cuando dos cifras del mismo criterio encajan como **gradiente** (ideal/aceptable) o como **atajo vs.
> escala fina**, se registran así — **no como contradicción**. **Se eleva solo lo que no encaje**: una
> contradicción real, no una diferencia de grano.

---

## Módulo 15 — Ratios fundamentales

*Detectadas en la ingesta del vídeo 15 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 y T3
imposibles — las tres son T4. Su capa visual son **4 capturas**, todas diapositivas de texto **sin
una sola cifra**.*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **15-E1** | T4 | «el **EV/BITDA**» `[VÍDEO 15, 02:44]` | **NO** — nombre de ratio, inocuo | ✅ **DICTAMINADO POR EVIDENCIA** — es **EV/EBITDA**. Lo resuelve el propio vídeo, que lo dice bien después `[10:10]`, y `[CAPTURA 15_ratios_de_valoracion]`, que lo rotula correctamente |
| **15-E2** | T4 | «el grado de **aplancamiento** general» `[VÍDEO 15, 17:36]` | **NO** — término, no definición | ✅ **DICTAMINADO POR EVIDENCIA** — es **apalancamiento**, usado correctamente en [[deuda_financiera]] campo 1 (vídeo 06) |
| **15-E3** | T4 | «**¿Y por qué la duda es?** ¿Y por qué usar el EV/EBITDA en lugar del EV/Free Cash Flow?» `[VÍDEO 15, 10:03]` — la primera pregunta es agramatical | **NO** — muletilla de transición; la pregunta real viene inmediatamente después y es clara | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO — trivial.** Muletilla de transición, sin ambigüedad sobre la pregunta real |

---

## Módulo 17 — Multibagger (**estreno del molde 5**)

*Detectadas en la ingesta del vídeo 17 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 y T3
imposibles — las seis son T4. **En el molde 5 un bloque sin T1/T3 es lo esperable.** Detalle
completo en [[multibagger]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **17-E1** | T4 | **Criterio 3 (FCF), sin referente:** «si el free cash flow **es mayor**, genial, pero **si no llega ni a la mitad**…» `[VÍDEO 17, 08:42–09:00]` — ¿mayor / la mitad **de qué**? | **NO** — el filtro es autocontenido | ✅ **DICTAMINADO** — el referente es el **BENEFICIO NETO**. *Resuelto por Gerard contra el audio (D-46), 2026-07-19.* ⚖️ **Se elevó correctamente bajo D-73**: tocaba método, sin deck, y el referente era **indeterminable desde la sola transcripción** — dependía de la escucha del audio. Ver [[multibagger]] campo 4.3 |
| **17-E2** | T4 | «net debt/**eebitda**» · «deuda neta sobre **Eebitda**» ×3 `[17, 09:19 · 09:56 · 10:36]` | **NO** — nombre de ratio | ✅ **DICTAMINADO POR EVIDENCIA** — es **EBITDA**, correcto en todo el corpus ([[deuda_neta]] campo 3) |
| **17-E3** | T4 | «las **multibugger** suelen esconderse» `[VÍDEO 17, 06:11]` | **NO** — el propio concepto del vídeo | ✅ **DICTAMINADO POR EVIDENCIA** — es **multibagger**, correcto ~15 veces en el mismo vídeo |
| **17-E4** | T4 | «un **doble dígito**» `[00:55]` · «no hace falta ser **un analista de fondos de inversión** para que puedas **detectar** calidad» `[13:16]` | **NO** — no tocan definición ni umbral | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** `.srt` canónico corregido en los dos fragmentos (D-46) |
| **17-E5** | T4 | «no queremos ver porcentajes locos [de payout]. **En algunas REITs sí**, porque es su modelo» `[VÍDEO 17, 12:29–12:34]` | **NO** — matiz sobre una excepción, no toca el criterio | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** Son REITs (payout alto por ley). `.srt` canónico corregido (D-46) |
| **17-E6** | T4 | «el **levered** free cash flow» `[VÍDEO 17, 09:52]` — leyendo una métrica de TIKR | **NO** — rótulo de herramienta, no definición del experto | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO, y confirmado por evidencia.** `.srt` canónico corregido (D-46). Coincide con lo que el vídeo 16 explica para el mismo término — confirma `09-E1` → [[fcf_yield]] campo 14 |

> ⭐ **`17-E1` es el reverso de `12-E1`.** Aquélla se corrigió **por evidencia** porque la fuente se
> desambiguaba sola (el deck traía los números); ésta **se elevó** porque la fuente **no** la
> desambiguaba —sin deck, referente indeterminable— y su resolución dependía de algo que solo el
> usuario tiene: **su escucha del audio**. Las dos son T4; el tratamiento distinto **es exactamente
> lo que D-73 prescribe**.

---

## Módulo 16 — La realidad de los múltiplos (**cierra el bloque de múltiplos, 12–16**)

*Detectada en la ingesta del vídeo 16 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 estructural
(voz↔PDF) es imposible por falta de deck, pero el vídeo trae **capturas** como capa visual, y ahí sí
choca con la voz — tratada como T1 (voz↔capa visual), igual que las capturas de otros módulos.
Detalle completo en [[p_s]] campo 4.*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **16-E1** | T1 (voz ↔ capa visual) | **Banda media del P/S**: la voz sitúa «ya está cara» a partir de **6** `[16, 18:43–18:51]`; la captura rotula **4-9 = «Normalizado»** `[CAPTURA 16_precio_ventas]` | 🔴 **SÍ (b)** — es la banda operativa del múltiplo | ✅ **DICTAMINADO — GRADIENTE, no contradicción** (dictamen del usuario, verificado contra el vídeo). Los extremos `<3` y `>10` **coinciden y los enfatiza el experto**; el tramo medio se lee como el rango normalizado de mercado (captura, 4-9) con un punto de inflexión personal más exigente dentro de él (voz, 6). Las dos procedencias conviven en el cuerpo. *Gerard, 2026-07-19* |

✅ **Sin más erratas registradas en el resto del material del vídeo 16** (siete múltiplos revisados;
todas las cifras que traen las capturas coinciden con la voz salvo `16-E1`).

> ⭐ **Primer caso del corpus en que una T1 contra capa visual (no deck) se dictamina como gradiente.**
> Hasta ahora el patrón «gradiente compatible» solo se había visto en T2 **entre vídeos** (`14-E1`,
> `14-E2`). Aquí el mismo criterio —dos lecturas que encajan como rango amplio + punto de inflexión
> más fino, en vez de chocar sin margen— se aplica **dentro de un mismo vídeo**, entre voz y captura.
> Confirma que el criterio de D-71/D-73 no es propio de un tipo de errata: es una forma de leer
> cualquier choque de cifras antes de darlo por irreconciliable.

---

## Módulo 18 — Medir el riesgo (**estrena la variante `SCORING` del molde 5**)

*Detectadas en la ingesta del vídeo 18 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 y T3
estructuralmente imposibles — las tres son T4. **La mejor puntuación del corpus** (ratio ~14/100
palabras). Detalle completo en [[medir_el_riesgo]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **18-E1** | T4 | «tenemos **dos setores** claros, **setores** cíclicos» `[VÍDEO 18, 02:13]` — «setores» no es palabra española | **NO** — error ortográfico/fonético, no toca ninguna definición | ✅ **DICTAMINADO POR EVIDENCIA** — es **sectores**, usado correctamente en el mismo vídeo tres veces más (`[02:04]`, `[02:33]`, `[05:10]`) |
| **18-E2** | T4 | «situaciones especiales, tipo **Zegona** o **New Princes**» `[VÍDEO 18, 03:26–03:30]` | **NO** — ejemplo de pasada, no toca el criterio | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** Es **Zegona Communications**. `.srt` canónico corregido (D-46). «New Princes» ya era correcto (antes Newlat Food), no se tocó |
| **18-E3** | ~~T4~~ | «¿o es sólo ruido de mercado, como por ejemplo **las tablillas** de Donald Trump?» `[VÍDEO 18, 11:56–12:00]` | **NO** | ⛔ **NO ES ERRATA — VERIFICADO CONTRA EL AUDIO.** El experto dice literalmente «tablillas» — la transcripción es fiel. **Sacada del recuento** |

✅ **Ninguna inversión direccional** en las diez direcciones de riesgo del scoring.

> ⚠️ **Dos ambigüedades registradas FUERA de la tabla de erratas, a propósito — decisión del
> usuario.** El sistema de puntuación trae dos imprecisiones que **no son choque entre capas ni
> defecto de transcripción** (no encajan en T1-T4): las fronteras de banda se solapan (`1-3` / `3-6`
> / `6-8` / `8-10`, cada límite cae en dos bandas) y no queda claro si la «situación especial» del
> factor 3 suma un punto extra fuera del máximo de 10. **Se quedan como `[HUECO]` citado en
> [[medir_el_riesgo]] campos 4 y 5, sin dictamen**: es imprecisión del experto describiendo su
> propio sistema — un dato sobre el sistema, no un defecto de la ficha a resolver.

---

## Módulo 19 — Cuándo acumular, mantener o vender (🏁 **ÚLTIMO VÍDEO DEL CORPUS**)

*Detectada en la ingesta del vídeo 19 (2026-07-19). ⚠️ **Vídeo SIN DECK** (D-13): T1 y T3
imposibles. **Con este módulo, los 19 vídeos quedan escrutados.** Detalle en
[[cuando_acumular_mantener_vender]].*

| # | Tipo | Qué choca | ¿Arrastra? | Estado |
|---|---|---|---|---|
| **19-E1** | T4 | «lo que dice un analista, lo que dice un **rotativo**, lo que dice un gran inversor» `[VÍDEO 19, 11:16–11:21]` | **NO** — enumeración de fuentes de opinión externa, no toca ningún criterio del sistema | ✅ **DICTAMINADO — VERIFICADO CONTRA EL AUDIO.** Es **rotativo** (periódico). `.srt` canónico corregido (D-46) |

✅ **Ninguna otra errata.** Junto con el 11, es el vídeo con menos entradas del corpus — coherente
con ser de los mejor puntuados.

✅ **Ninguna inversión direccional.** Comprobado en particular el cruce que más lo pedía: «correcciones
del **10-20 %** son normales» `[19, 09:19]` (motivo de MANTENER) frente a «las empresas caras pueden
corregir un **30, 40 % o 50 %** sin que cambie nada en el negocio» ([[medir_el_riesgo]] factor 8).
⛔ **NO es `T2 entre vídeos`:** son **fenómenos distintos** —ruido de mercado normal vs. corrección
por sobrevaloración—, no el mismo umbral con dos valores. **No se registra errata donde no la hay.**

---

## Recuento

🏁 ⭐ **RECUENTO TRAS EL PASE DE DICTAMEN FINAL (2026-07-19).** Las 33 erratas que seguían
`PENDIENTE` se resolvieron en una sola sesión, verificando cada una contra el audio original. El
recuento **baja de 63 a 59** — no por descuido, sino por **depuración**: cuatro entradas resultaron
no ser defectos de la fuente en absoluto (`12-E3`, `07-E4`, `07-E8`, `18-E3`) y salen del cómputo.
Dos que parecían defectos de transcripción resultaron ser **lapsus del propio experto** (`04-E1`,
`08-E4`) y pasan de T4 a T2 — **ahora sí cuentan para la tasa de error del curso**, cuando antes
contaban (erróneamente) para la del instrumento de transcripción.

| Tipo | Nº | Dictaminadas |
|---|---|---|
| **T1** · voz ↔ PDF | 15 | 14 |
| **T2** · voz ↔ voz | 8 | 8 |
| **T3** · PDF ↔ PDF | 8 | 8 |
| **T4** · transcripción | 28 | 28 |
| **TOTAL** | **59** | **58** |

> 🏁 ⭐ **Solo UNA errata sigue sin dictaminar: `10-E3`** (ASML, «toda la producción» vs «la máquina
> más importante») — y no por falta de tiempo o de evidencia, sino por **decisión explícita del
> usuario de no elegir ganador**: es un ejemplo, no método, y lo que importa es el concepto
> (conocer el contexto de la empresa), no la situación exacta de esta compañía concreta. **Queda
> registrada como tensión abierta, no como pendiente por descuido.**

> ⚠️ **Corrección del desfase anterior.** El recuento previo a este pase decía «32 pendientes»;
> contando fila por fila había en realidad **33**. Quedó corregido al recomponer la tabla completa
> en esta sesión — no afecta a ninguna errata en sí, solo a la aritmética del índice.

> 🆕 ⭐ **Sub-tipo dentro de T2: «entre vídeos».** `14-E1` y `14-E2` son umbrales del mismo ratio
> dados en módulos distintos — un choque que solo aparece cuando el corpus está lo bastante
> ingerido para cruzarlos. **Criterio fijado (Gerard, 2026-07-19):** si dos cifras encajan como
> **gradiente** (ideal/aceptable) o como **atajo vs. escala fina**, se registran así, no como
> contradicción. Se eleva solo la contradicción real. El corpus completo confirmó que **solo
> aparecieron dos** (`14-E1`, `14-E2`) — el patrón no proliferó al cerrar el resto de los vídeos.

> 🆕 **La columna «Dictaminadas» mezcla tres procedencias distintas de evidencia (D-73 + esta
> sesión), de más a menos fuerte:**
>
> | Categoría | Qué significa | Nº |
> |---|---|---|
> | ✅ **`DICTAMINADO POR EVIDENCIA`** | Resuelto por el escritor citando **otra parte del corpus** — sin que el usuario tuviera que volver al audio | **11** — `10-E1`, `10-E6`, `12-E1`, `12-E2`, `12-E4`, `14-E3`, `15-E1`, `15-E2`, `17-E2`, `17-E3`, `18-E1` *(corregido: antes se contaban 10, faltaba `14-E3`)* |
> | ✅ **`DICTAMINADO`** (por criterio del usuario, sesiones anteriores) | Resuelto por el usuario en rondas previas, sin el marco formal de «verificado contra el audio» de esta sesión | **19** — `06-E1` a `06-E4`, `01-E1` a `01-E3`, `02-E1`, `05-E1`, `08-E1`, `09-E1`, `10-E2`, `11-E1`, `07-E5`, `13-E1`, `14-E1`, `14-E2`, `16-E1`, `17-E1` |
> | ⭐ 🆕 **`DICTAMINADO — VERIFICADO CONTRA EL AUDIO`** | El usuario **volvió a cada vídeo** en esta sesión de dictamen final para comprobar qué dice el experto — la categoría de evidencia más fuerte del proyecto, por encima de «evidencia del corpus» | **28** — todas las de este pase, ver sus módulos |
>
> Suma: 11 + 19 + 28 = **58 dictaminadas**. La única que queda fuera es `10-E3` (sin dictamen, por
> decisión, no por evidencia insuficiente).

*(Criterio de recuento, constante desde el módulo 03: una errata de tipo doble —`03-E1` T1+T3,
`09-E1` T1+T3, `11-E1` T1+T4— **se cuenta una sola vez, bajo su tipo primario**.)*

| Vídeo | Duración | Erratas |
|---|---|---|
| 06 · Deuda y caja | 10,6 min | 4 |
| 07 · ROIC vs ROE | 11,4 min | 7 *(antes 9 — bajan `07-E4`, `07-E8`)* |
| 03 · Balance general | 9,2 min | 2 |
| 10 · El moat ✅ reingerido | 6,4 min | 7 |
| 01 · Marco del análisis fundamental | 11,6 min | 3 |
| 02 · Cuenta de resultados | 7,8 min | 1 |
| 04 · Estado de flujos de caja | 10,4 min | 2 |
| 05 · El informe 10-K | 7,3 min | 2 |
| 08 · CAPEX | 10,3 min | 6 |
| 09 · Free Cash Flow | 7,5 min | 1 |
| 11 · El equipo directivo | 5,5 min | 1 |
| 12 · Múltiplos de valoración | 6,6 min | 3 *(antes 4 — baja `12-E3`)* |
| 13 · Múltiplo y BPA ⚠️ sin deck | 14,0 min | 3 |
| 14 · ¿Cuándo usarlos? ⚠️ sin deck | 9,4 min | 4 |
| 15 · Ratios fundamentales ⚠️ sin deck | 22,1 min | 3 |
| 17 · Multibagger ⚠️ sin deck | 14,4 min | 6 |
| 16 · La realidad de los múltiplos ⚠️ sin deck (capturas) | 38,5 min | 1 |
| 18 · Medir el riesgo ⚠️ sin deck | 12,1 min | 2 *(antes 3 — baja `18-E3`)* |
| 19 · Acumular/mantener/vender ⚠️ sin deck | 11,8 min | 1 |
| 🏁 **Total — LOS 19 VÍDEOS** | **226,9 min** | **59** |

> ⚠️ **El 15 refuerza el aviso de abajo hasta el extremo: 22 minutos —el vídeo más largo escrutado—
> y solo 3 erratas, todas triviales.** No es que sea la fuente más limpia: es que **sin deck no hay
> segunda capa contra la que contrastar**, y T1/T3 son imposibles. **Comparar su cifra con la del
> vídeo 07 (7 erratas, 11 min, con deck) sería un error de método.**

> ⚠️ **El 13 es el primer vídeo escrutado SIN DECK.** Sus 3 erratas salen de **una sola capa**,
> mientras que las de los otros 12 salen de dos. **No son comparables** con las de un vídeo con
> deck — refuerza el aviso de abajo: la cuenta mide la fuente **y el instrumento**.

---

## ⚠️ Cómo NO leer estos números

**La cuenta no mide solo la fuente: mide la fuente Y el método con que se buscó.**

| Pasada | Instrumento | Erratas registrables |
|---|---|---|
| Primera ingesta (módulo 06) | sin bloque de tipos | 4 |
| Piloto v1 | solo transcripción | 0 |
| Piloto v2 | + deck, 1 tipo | 9 |
| Piloto v3 | + los 4 tipos | 17 |

**La fuente no cambió. El instrumento sí**, y cada mejora casi dobló la cuenta.

> ### 🔴 🆕 Y el instrumento no solo hace SUBIR la cuenta: también la **infla con erratas falsas**
>
> Hasta la reingesta del vídeo 10, el aviso decía que un mejor método **encuentra más** erratas —
> por eso las cifras son un **suelo**. **La reingesta demuestra el efecto contrario y peor:** una
> transcripción degradada **fabricó una errata que no existía** (`10-E1`, un supuesto lapsus del
> experto que era ruido de máquina). Al corregir la fuente, **la cuenta de T1 BAJÓ**.
>
> **Por tanto la cuenta no es un suelo limpio: es un suelo con ruido en las dos direcciones.**
> Faltan las que el método no vio **y sobran las que el método inventó**. La única forma de saber
> cuáles son cuáles es **verificar la transcripción contra el audio** (D-46) — que es exactamente lo
> que se hizo con los vídeos 10, 14 y 16.
>
> ⚠️ **Alcance del daño, acotado:** de los 19 vídeos escrutados, **solo el 10 se ingirió (en su
> primera pasada) desde una transcripción degradada**, y **ya está reingerido** sobre la versión
> puntuada a mano contra el audio (D-46). Los otros 18 se ingirieron con `.srt` de calidad normal,
> así que **el efecto de fabricación no se les presume**. Pero **el vídeo 01, con puntuación
> intermedia (2,63), nunca se ha reverificado** — 🔴 **es el único cabo suelto de fiabilidad de
> fuente que queda en todo el corpus.**

> ### 🏁 🆕 Una segunda bajada — distinta de la primera, y más grande: DEPURACIÓN, no fabricación
>
> El recuento **volvió a bajar** en el pase de dictamen final (2026-07-19): de 63 a 59 erratas. **No
> es el mismo fenómeno que la bajada del vídeo 10.** Aquella vez el instrumento había **fabricado**
> una errata inexistente (ruido de máquina). Esta vez, el usuario **verificó contra el audio original
> las 33 que seguían `PENDIENTE`** y encontró que **4 nunca fueron defectos de la fuente**: dos eran
> lecturas correctas mal comparadas (`12-E3`, la voz redondeaba una cifra que la captura daba con más
> precisión), una era un criterio de muestra confundido con un umbral (`07-E4`), y una era el límite
> físico del vídeo original, no de la transcripción (`07-E8`).
>
> **Y dos más cambiaron de naturaleza sin salir del recuento:** `04-E1` y `08-E4` parecían ruido de
> máquina (T4) y resultaron ser **lapsus del propio experto** (T2) — dicho de otro modo, **empezaron
> a contar para la tasa de error del CURSO en vez de para la del INSTRUMENTO de transcripción**, que
> es justo la distinción que este apartado lleva insistiendo en hacer desde el vídeo 10.
>
> **Por tanto: la cuenta bajó por depuración, no por descuido.** Sigue siendo un suelo del método
> —58 de 59 quedaron dictaminadas en una sola sesión porque el usuario volvió al audio, no porque el
> corpus fuera más limpio de lo que parecía—, pero ahora **mide con más precisión qué defectos son
> del curso** (lapsus del experto, inconsistencias de deck) **y cuáles nunca lo fueron**.

Por tanto:

1. **Son un SUELO**, no una medida. Con mejor método saldrían más.
2. **Las cifras por vídeo NO son comparables entre sí**: el 07 tiene 7 y el 03 tiene 2, pero el 07 se
   escrutó mucho más. **La diferencia mide atención, no calidad de la fuente.**
3. 🏁 **Los 19 vídeos están escrutados** (el 03 y el 10 cuentan ya por su ingesta piloto /
   reingesta, ver abajo). ⚠️ **Pero siete son sin deck** (13, 15, 16, 17, 18, 19 y el propio 10 en su
   ingesta piloto original): sus cuentas **no son comparables** con las de los vídeos con deck.
   ⛔ **Sigue sin haber una «tasa de error del curso»** — la cobertura es completa, pero **el
   instrumento no fue homogéneo**: doce vídeos se contrastaron contra dos capas y siete contra una.
4. El único uso legítimo hoy es **cualitativo**: qué **tipos** de defecto tiene esta fuente —
   contradicciones internas de la voz, deck internamente inconsistente, transcripciones que no
   determinan el contenido.

> **No derivar de aquí ninguna conclusión sobre «cuánta autoridad merece el curso»** hasta que el
> método esté congelado y aplicado por igual a los 19 vídeos.

## 🏁 Lo que desbloqueó varias de golpe (histórico — ya ejecutado)

*Esta sección listaba acciones pendientes. Las tres ya se ejecutaron; se conserva como traza.*

| Acción | Desbloqueó | Estado |
|---|---|---|
| **Verificar el `.srt` del vídeo 07** contra el vídeo (D-46) | `07-E8`, `07-E9` — y de paso, verificando el vídeo entero, las otras siete pendientes del módulo | ✅ Hecho — pase de dictamen final, 2026-07-19 |
| **Verificar el `.srt` del vídeo 10** (D-46) | `10-E6` | ✅ Ya hecho en la reingesta del vídeo 10 |
| **Captura del balance de Meta** del vídeo 03 → `capturas_pendientes.md` | Cierra el hueco de cobertura del 03 | ✅ Ya resuelta (ver [[capturas_pendientes]]) |

**No queda ninguna acción de este tipo pendiente.** Lo único sin cerrar en todo el índice es
`10-E3`, y no por falta de una acción que lo desbloquee — es una tensión que el usuario decidió
dejar registrada, no resuelta.
