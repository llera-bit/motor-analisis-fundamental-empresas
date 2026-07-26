---
concepto: ROIC (Return on Invested Capital)
modulo: 07
molde: 1
estado: piloto
fuentes: [VIDEO-07, PDF-07]
enlaces: [roe, moat, balance_general]
---

# ROIC

> ⛔ **SUPERSEDIDA (2026-07-19).** Rehecha con el molde 1 definitivo (v4) en
> `wiki/curso/roic.md` — con el campo *Punto ciego* (nuevo desde el piloto), el umbral
> consolidado (10-15 %, dictamen del usuario) y la aplicabilidad a dos ranuras. Esta ficha **no se
> borra** (D-18, traza) pero **no se consulta como método**.

> ⚠️ **FICHA DE PILOTO.** Valida el MOLDE 1 v2 (`moldes.md`). No se promueve a `curso/`.
> Fuentes: `raw/transcript/07_roic_vs_roe.srt` (voz) + `raw/pdf/07_roic_vs_roe.pdf` (deck,
> 7 páginas, sección «5. LA RENTABILIDAD»). Las dos son mitades del mismo momento.
> **Ficha hermana de [[roe]].**

---

## 1. Definición y fórmula

**Definición.** El ROIC «mide el retorno sobre todo el capital operativo invertido, refleja el
negocio en sí» `[VÍDEO 07, 02:30]`; «evalúa qué tan bien se usa el capital total, mide también la
eficiencia de la gestión» `[VÍDEO 07, 02:37]`. El deck lo titula **«RETORNO SOBRE EL CAPITAL
INVERTIDO / Return on Invested Capital»** y lo llama «una métrica muy buena para medir la calidad de
los negocios no financieros» `[PDF 07, p.2]`.

Formulado como resultado: «cuánto gana una empresa después de impuestos por cada euro que necesita
operar» `[VÍDEO 07, 04:36]`.

**Encuadre.** Pertenece a la **rentabilidad económica**, que el deck define como «el beneficio
promedio de la compañía por el total de las inversiones hechas, expresada en términos %»
`[PDF 07, p.1]`; la voz lo dice como «el beneficio en relación al total de la inversión […] capital
más deuda» `[VÍDEO 07, 01:51]`. Es una de las cuatro formas que el deck enumera para medir la
rentabilidad: **ROIC, ROCE, ROE, ROA** `[PDF 07, p.1 + VÍDEO 07, 02:18]`.

**Fórmula — SECUNDARIA.**

```
ROIC = NOPAT / Capital invertido
       NOPAT = EBIT × (1 − tasa impositiva)
       Capital invertido = equity + deuda operativa neta
```
`[VÍDEO 07, 04:18–04:36]` — **aporte solo-verbal**

> ⚠️ **La fórmula NO está en el deck.** `[PDF 07, p.3]` no la trae. El experto **la dibuja a mano
> sobre la slide**: «la fórmula del ROIC **que la voy a dibujar**» `[VÍDEO 07, 04:18]`. Existe por
> tanto una tercera capa visual —la anotación en directo— que el PDF no captura. Ver `piloto_friccion.md`.

> **El propio experto marca la fórmula como secundaria**, no es una lectura nuestra: «las fórmulas
> las pongo aquí a modo anécdota, pero no hace falta conocer las fórmulas porque ahora hay
> herramientas que te facilitan mucho esto» `[VÍDEO 07, 04:39–04:47]`.

`[HUECO]` Ni la voz ni el deck definen «deuda operativa neta», ni dicen si el capital invertido se
promedia entre dos balances o se toma a cierre, ni qué tasa impositiva usa (efectiva o estatutaria).
*Resolución esperada:* decisión de arquitectura de la Capa 2 (datos), o `complemento/`.

---

## 2. Qué mide / interpretación direccional

Más alto es mejor, y el experto lo justifica **por riesgo**, no solo por retorno: «la clave aquí es
invertir en empresas con alta rentabilidad sobre el capital, porque esto **reduce el riesgo** y
aumenta mucho la probabilidad de un retorno superior sostenido» `[VÍDEO 07, 01:25]`. Mecanismo que
da: «con menos recursos, con menos capital, me ganes mucho más dinero, porque el margen es superior»
`[VÍDEO 07, 01:36]`.

**Pero la dirección no es solo "alto": es "alto Y estable o creciente".** «Es deseable ver un ROIC
estable o que aumenta con el tiempo» `[PDF 07, p.3]`; «lo que buscamos realmente en un ROIC es que
este sea estable o creciente» `[VÍDEO 07, 03:31]`. Ver *§8 Consistencia temporal*.

**Razón de ser frente al beneficio neto a secas:** «no basta solo con el beneficio neto, porque dos
empresas con el mismo beneficio pueden tener estructuras de capital muy distintas, y es que una puede
generar ese beneficio con mucho menos capital» `[VÍDEO 07, 01:12–01:30]`.

**Veredicto global:** «el ROIC es la mejor métrica para evaluar si una empresa crea valor»
`[VÍDEO 07, 10:02]`.

---

## 3. Umbral(es)

### UMBRAL A — «ROIC > 15% sostenido → ventaja competitiva duradera»

**3a · Valor + procedencia** — **DOS CAPAS.**
- **Voz:** «un ROIC por encima del **15%** y sostenido es indicio de una ventaja competitiva
  duradera» `[VÍDEO 07, 07:22]`. Reforzado: «un ROIC superior al 15% con un ROE equilibrado sin
  distorsión por deuda son buenas señales» `[VÍDEO 07, 08:40]`.
- **PDF:** el 15% es **el criterio de construcción del gráfico**. Su título literal es
  **«Industrias con ROIC > 15% promedio desde 1998 (US)»** `[PDF 07, p.5]`.
- Como criterio de selección: «todos aquellos inversores que busquen empresas de calidad sostenible
  deberían centrarse en aquellas que superen este umbral promedio de ROIC» `[VÍDEO 07, 07:34–07:43]`.

**3b · Clase — `[ABSOLUTO-RELATIVIZADO]`.**
Y esta vez **la relativización es del experto, no nuestra**. El deck la enuncia en la misma frase:

> «El ROIC promedio de la bolsa se sitúa en torno al 13-15% de forma general. **Porque luego, cada
> sector tiene su propio ratio promedio.**» `[PDF 07, p.3]`

Y el criterio de moat que da el deck es **explícitamente sectorial**:

> «Normalmente, la empresa con **mejor ROIC del sector** suele ser la empresa con mayor ventaja
> competitiva (MOAT).» `[PDF 07, p.3]`

Coherente con la voz: «lo que hacemos es comparar el ROIC histórico de la empresa **y con el
sector**» `[VÍDEO 07, 03:37]`. Y el propio gráfico del 15% es de **industrias**, no de empresas
`[PDF 07, p.5]`.

> *(En el piloto v1 esta clase quedó `[HUECO]` porque etiquetarla habría sido síntesis mía. El PDF
> la ancla: es la estructura del experto.)*

**Fuente viva del benchmark sectorial (D-56):** `[HUECO]`. El gráfico dice **«desde 1998 (US)»** —
industrias estadounidenses, serie desde 1998— pero **no lleva atribución de fuente** `[PDF 07, p.5]`.
Damodaran no aparece ni en la voz ni en el deck del 07. No se enlaza con D-56 por inferencia.

**3c · Justificación del experto — `AUSENTE`.**
**No dice por qué 15%.** Ni la voz ni el deck dan razón del valor concreto: el gráfico ya viene
construido con ese filtro `[PDF 07, p.5]` y la voz lo enuncia como dato `[VÍDEO 07, 07:22]`.

Lo único adyacente es la relación aritmética con sus propias cifras: **15% es el extremo superior de
la banda 13-15% que él llama promedio de bolsa** `[PDF 07, p.3]`. Se registra el hecho; no se
interpreta.

⚠️ **D-08: sin justificación anclada, este umbral NO se adopta por autoridad.** Queda registrado
como lo que el experto enseña, pendiente de validación.

**3d · Tensiones — tres cifras, y el PDF resuelve una de las dos.**

| Cifra | Enunciado | Capas | Contexto (según el PDF) |
|---|---|---|---|
| **13-15%** | «el promedio de mercado, el ROIC se encuentra entre el 13 y el 15%» `[VÍDEO 07, 03:49]` · «El ROIC promedio de la bolsa se sitúa en torno al 13-15% de forma general» `[PDF 07, p.3]` | **voz + PDF** | Slide de bullets sobre el ROIC. Promedio de bolsa, general. |
| **5-15%** | «la mayoría de empresas tienen un ROIC entre el 5 y el 15% que es la media» `[VÍDEO 07, 07:19]` | **solo voz** | Dicho **sobre `[PDF 07, p.5]`**, el scatter «Industrias con ROIC > 15% promedio desde 1998 (US)». Es una **lectura de la nube de puntos** de un gráfico ya filtrado. |
| **8-10%** | «el ROIC promedio del mercado suele rondar entre el 8 y 10%, lo que es un punto de referencia bastante útil» `[VÍDEO 07, 07:28]` | **solo voz** | Dicho también sobre `[PDF 07, p.5]`. **Sin ancla en ninguna slide.** |

**✅ RESUELTO — el 5-15% no era una contradicción.** El contraste con el PDF muestra que es
**otro contexto**: no es un promedio de mercado, es él **leyendo la dispersión anual del scatter de
la p.5**, cuyo eje va de −20% a 120% y cuya nube densa está en esa banda. Se registra como lectura
del gráfico, no como umbral rival. *(En el piloto v1, sin el PDF, parecía contradicción.)*

**⛔ SUBSISTE — 13-15% contra 8-10%.** Las dos usan la **misma expresión** («promedio de la bolsa» /
«promedio del mercado») con rangos que no solapan, con **3 minutos y medio de diferencia**. El
13-15% tiene **respaldo en las dos capas**; el 8-10% **no tiene ancla en ninguna slide**.

> ⚠️ **No se resuelve aquí, y la regla de conflicto no ayuda:** voz > PDF sirve para un choque
> voz↔PDF, pero esto es **voz contra voz** (03:49 contra 07:28). El PDF solo actúa como testigo de
> uno de los dos lados. **Elegir sería criterio propio → RD-1.** Queda `PENDIENTE DE REVISIÓN HUMANA`.

**Por qué importa y no es cosmético:** el sentido del UMBRAL A depende de cuál sea el promedio. Con
promedio 8-10%, «>15% sostenido» es una barra exigente. Con promedio 13-15% —el respaldado por las
dos capas—, «>15%» es el borde superior de la media. Son dos lecturas muy distintas del mismo
criterio. Se registra el hecho; la lectura es del humano.

### UMBRAL B — «ROIC > coste del capital, de forma consistente»

**3a · Valor + procedencia** — **solo voz**, sin cifra. «solo unas pocas empresas logran un ROIC
consistentemente superior al coste del capital que es el WAC» `[VÍDEO 07, 07:12–07:19]`; reinvertir
«en proyectos que generan más rentabilidad de lo que cuestan (WAC)» `[VÍDEO 07, 10:54]`.
*Nota literal:* dice **«el WAC»** las dos veces, no «WACC». Se transcribe tal cual (D-46: no se
corrigen los errores del experto). No se expande: sería `[INFERIDO]`.

**3b · Clase** — `[HUECO]`. Es un umbral **relativo a la propia empresa** (su coste de capital), que
no es ninguna de las tres clases. No se fuerza.

**3c · Justificación** — **presente, y es la única del vídeo**: «significa que la empresa puede
reinvertir beneficios en proyectos que generan más rentabilidad de lo que cuestan» `[VÍDEO 07, 10:49]`
→ vínculo con las compounders `[VÍDEO 07, 10:58]`.

**3d · Tensiones** — ninguna.

`[HUECO]` No dice **cómo se obtiene** el coste del capital. Ni voz ni deck. *Resolución esperada:*
módulo posterior o `complemento/`.

---

## 4. Aplicabilidad condicionada

**Sirve para: negocios NO financieros.** Dos capas.
- «Es una métrica muy buena para medir la calidad de los **negocios no financieros**» `[PDF 07, p.2]`
- «es ideal para negocios no financieros. Es un detalle importante, porque se miden diferente los
  bancos al resto de los sectores» `[VÍDEO 07, 02:45–02:53]`

**Sirve especialmente para comparar ENTRE sectores distintos** — su ventaja diferencial frente al
[[roe]]: «se puede comparar entre empresas de distintos sectores algo que no es viable con el ROE,
por eso el ROIC es especialmente útil en análisis sectoriales o entre empresas con estructuras
financieras distintas, como por ejemplo si comparamos una tecnológica contra una utility»
`[VÍDEO 07, 05:52–06:41]`. También `[VÍDEO 07, 05:17]`. **Aporte solo-verbal**: el deck no lo dice.

**No sirve para / precaución:** bancos y financieras. Ni la voz ni el deck lo **prohíben**
explícitamente; lo que hay es la asignación positiva («ideal para no financieros», `[VÍDEO 07, 02:48]`
y `[PDF 07, p.2]`) más la observación de que «se miden diferente los bancos» `[VÍDEO 07, 02:48]`, y
por separado la asignación del ROE al sector financiero. **No se endurece.**

`[HUECO]` **Por qué** los bancos se miden diferente: no lo dice ninguna capa. *Resolución esperada:*
`complemento/`.

---

## 5. Advertencia de uso aislado / cuándo engaña

**Un ROIC bueno no basta.** Es la advertencia más rotunda, y está en **las dos capas casi con las
mismas palabras**:

> «Es importante encontrar empresas con buenos valores de ROIC. **Pero esto por sí solo no es
> suficiente.** Se hace necesario también ver la **TASA DE REINVERSIÓN**. ¿En qué reinvierten el Cash
> Flow que generan? ¿En CapEx, M&A (fusiones y/o adquisiciones), otros?» `[PDF 07, p.3]`
>
> «es importante sobre todo que encontremos empresas con buenos valores de ROIC, pero esto por sí
> solo no es suficiente […] es necesario también ver la tasa de reinversión […] **no me sirve que
> tengas un buen ROIC si después la gestión es nefasta**» `[VÍDEO 07, 03:55–04:15]`

La coletilla «si después la gestión es nefasta» es **aporte solo-verbal**: añade el juicio sobre la
gestión que el deck no formula.

Cierre: «la clave es invertir en empresas con ROIC alto y que sea sostenible, **no solo con
beneficios crecientes**» `[VÍDEO 07, 10:11–10:20]`.

`[HUECO]` **¿Cuándo engaña el ROIC?** **Ninguna capa lo dice.** El experto describe mecanismos
concretos por los que el ROE engaña (ver [[roe]]) y para el ROIC **no describe ninguno**: solo dice
que es «bastante menos manipulable» `[VÍDEO 07, 03:19]`. «Menos manipulable» no es «no manipulable»,
pero la frase no se completa. *Resolución esperada:* `complemento/` — es el contraejemplo que D-21
exige. **No se rellena por deducción.**

---

## 6. Lectura relacional

> La tesis comparativa del vídeo vive **repartida entre esta ficha y [[roe]]**, y se cruza en los dos
> sentidos. Ver también *§7*.

| Se cruza con | Cómo | Fuente |
|---|---|---|
| **[[roe]]** | «Ambas medidas juntas son un potente filtro para al menos descartar empresas mediocres» | `[PDF 07, p.2]` |
| **[[roe]]** | «ambos juntos forman un filtro potente para detectar empresas de calidad» | `[VÍDEO 07, 03:08]` |
| **[[roe]]** | «el ROIC y el ROE deben analizarse juntos, no por separado» | `[VÍDEO 07, 11:07]` |
| **[[roe]]** | Patrón bueno: «un ROIC superior al 15% con un ROE equilibrado sin distorsión por deuda son buenas señales» | `[VÍDEO 07, 08:40]` |
| **[[roe]]** | Patrón malo: «si vemos un ROE altísimo y un ROIC medio o bajo, cuidado porque el negocio puede ser que no sea tan eficiente como parece» | `[VÍDEO 07, 08:47]` |
| **Tasa de reinversión** (CapEx, M&A) | Obligatoria junto al ROIC; sin ella el ROIC no basta | `[PDF 07, p.3 + VÍDEO 07, 04:02]` |
| **Coste del capital («el WAC»)** | El ROIC debe superarlo consistentemente | `[VÍDEO 07, 07:12]` |
| **[[moat]]** | «Normalmente, la empresa con mejor ROIC del sector suele ser la empresa con mayor ventaja competitiva (MOAT). Por tanto, se trata de un indicador que nos puede servir para **encontrar empresas con MOAT**» | `[PDF 07, p.3]` |
| **[[moat]]** | «un buen ROIC suele indicar ventaja competitiva el MOAT, el foso defensivo que estudiaremos en otras clases» | `[VÍDEO 07, 03:44]` |
| **[[moat]]** | «el ROIC alto y sostenido indica una ventaja competitiva porque significa que la empresa puede reinvertir beneficios en proyectos que generan más rentabilidad de lo que cuestan (WAC)» | `[VÍDEO 07, 10:49–10:58]` |
| **Compounders** | «esto está directamente vinculado al concepto de las compounders, que son empresas capaces de crecer de forma rentable año tras año» | `[VÍDEO 07, 10:58–11:07]` |
| **Beneficio neto** | El ROIC lo corrige: mismo beneficio ≠ misma calidad si el capital empleado difiere | `[VÍDEO 07, 01:12]` |

**Dirección del cruce ROIC↔moat — el experto la enuncia en los dos sentidos y no jerarquiza:**
ROIC alto *sirve para encontrar* moat `[PDF 07, p.3 + VÍDEO 07, 03:44]`; y en el módulo 10 el moat
*produce* ROIC alto y estable `[VÍDEO 10, 03:08]`. **No se resuelve aquí.**

`[HUECO]` No enlaza el ROIC con el margen ni con el FCF en este vídeo (sí lo hará el módulo 10).

---

## 7. Recomendación comparativa

**El experto prefiere el ROIC sobre el [[roe]], y da criterio.** Es la tesis central del vídeo,
repetida seis veces — y es **casi toda solo-verbal**: el deck presenta las dos métricas en paralelo
y sin jerarquizarlas `[PDF 07, p.2]`.

1. «el ROIC es bastante menos manipulable y es más comparable entre empresas con distintas
   estructuras de capital» `[VÍDEO 07, 03:19]`
2. «por eso el ROIC en este aspecto **me gusta mucho más que el ROE**» — en el contexto de la tasa de
   reinversión / calidad de la gestión `[VÍDEO 07, 04:15]`
3. «el porqué el ROIC **es superior** al ROE, y es que el ROIC refleja la eficiencia del negocio
   completo porque tiene en cuenta la deuda más el equity, en cambio el ROE se enfoca solo en lo que
   gana el accionista» `[VÍDEO 07, 05:52–06:05]`
4. «el ROIC mide realmente la rentabilidad real del negocio, sin verse distorsionado por decisiones
   financieras como apalancamientos o recompra de acciones que sí lo tiene el ROE»
   `[VÍDEO 07, 06:15–06:26]`
5. «el ROIC es **más fiable** para comparar modelos de negocio» `[VÍDEO 07, 08:32]`
6. «el ROIC es **la mejor métrica** para evaluar si una empresa crea valor y el ROE lo que hace es
   complementar» `[VÍDEO 07, 10:02]`

**La preferencia NO es descarte:** «el ROIC y el ROE deben analizarse juntos, no por separado, a
pesar de que el ROIC sea mucho mejor que el ROE, también el ROE nos da una visión desde la cara del
accionista» `[VÍDEO 07, 11:07–11:27]`.

**Frente a ROA y ROCE:** los **nombra y los descarta sin criterio**. El deck los presenta como
iguales — «ROIC, ROCE, ROE, ROA: Diferentes formas de medir la rentabilidad» `[PDF 07, p.1]` — y la
slide siguiente ya solo trae dos: «Nos centramos en 2 indicadores de la rentabilidad: ROIC y ROE»
`[PDF 07, p.2]`. La voz: «hay diferentes formas (ROA, ROCE, ROE y el ROIC) pero nos vamos a centrar
en estas dos primeras, en el ROIC y en el ROE» `[VÍDEO 07, 02:18]`.
`[HUECO]` **Ninguna capa dice por qué ROA y ROCE quedan fuera.**

---

## 8. Consistencia temporal

**Es un requisito, no un adorno — y está en las dos capas.**

- «Es deseable ver un ROIC **estable o que aumenta con el tiempo**. Lo más interesante de esta
  métrica es comparar la **evolución histórica** que ha tenido el propio ratio de la empresa a lo
  largo de los años» `[PDF 07, p.3]`
- «lo que buscamos realmente en un ROIC es que este sea estable o creciente, y para ello lo que
  hacemos es comparar el ROIC histórico de la empresa **y con el sector**» `[VÍDEO 07, 03:31–03:40]`
  — *la comparación con el sector es aporte solo-verbal: el deck solo pide comparar con su propia historia.*
- El umbral lleva la sostenibilidad incorporada: «por encima del 15% **y sostenido**» `[VÍDEO 07, 07:22]`;
  y el gráfico mide **«ROIC > 15% promedio desde 1998»**, es decir, una media de ~16 años `[PDF 07, p.5]`
- «un ROIC **consistentemente** superior al coste del capital» `[VÍDEO 07, 07:12]`
- «las mejores empresas mantienen un ROIC de forma consistente, positivo y eso es precisamente lo que
  el mercado premia a largo plazo» `[VÍDEO 07, 10:28–10:35]`
- Cierre: «no basta con ratios altos, también importa su consistencia en el tiempo y la rima»
  `[VÍDEO 07, 11:21–11:31]` — *«y la rima» se transcribe tal cual; no se interpreta.*
- Contraste con el ROE: «en general la rentabilidad sobre este capital invertido se mantiene en
  rangos más estables» `[VÍDEO 07, 07:03]`. **El deck lo respalda visualmente:** el eje del gráfico
  de ROIC llega al 120% `[PDF 07, p.5]`, el de ROE al 250% `[PDF 07, p.6]`.

`[HUECO]` **No dice cuántos años.** «Histórico» y «sostenido» no se cuantifican en ninguna capa. El
único número temporal es el del gráfico —«desde 1998»— que es el rango del dato, no un criterio.
*Resolución esperada:* módulo posterior. **No se rellena.**

---

## 9. Banderas rojas

- **ROE altísimo + ROIC medio o bajo.** «cuidado porque el negocio puede ser que no sea tan eficiente
  como parece» `[VÍDEO 07, 08:47–08:55]`. Única bandera roja formulada como regla general. Solo-verbal.
- **ROIC por debajo del coste del capital de forma sostenida.** `[INFERIDO]` — dice que «solo unas
  pocas empresas logran un ROIC consistentemente superior al coste del capital» `[VÍDEO 07, 07:12]`,
  pero **nunca enuncia el reverso como bandera roja**. Marcado como inferencia; **no se adopta**.
- **ROIC decreciente.** Aparece **solo dentro de la demostración** (§10), no como regla. Por D-49 no
  se promueve.

---

## 10. Demostración / ejemplar del experto

> ⚠️ **PEDAGOGÍA, no metodología. Ilustración, nunca regla. No entra en el Inventario Atómico**
> (RD-1 + D-49). **No se transcriben las cifras** de estas empresas.

**Novo Nordisk vs Moderna** — `[VÍDEO 07, 08:55–10:20]` + `[PDF 07, p.7]` («5. LA RENTABILIDAD: ¿QUÉ
BUSCAMOS?»). ~1:30 de 11:31. **Es donde el experto demuestra la lectura cruzada ROIC↔ROE que predica.**

**Lo que plantea el deck** — la pregunta guía, literal: «Novo Nordisk vs Moderna. **¿En dónde
prefieres invertir?** Compara el ROE y ROIC de Novo Nordisk con el ROE y ROIC de Moderna.»
`[PDF 07, p.7]`. Y: «Si analizas bien, Moderna tuvo ese pico de cotización por la vacuna del Covid. A
partir de ahí, la rentabilidad ha ido en decremento. ¿Qué habrá pasado con un inversor que en 2021
haya invertido en Moderna y otro en Novonordisk?» `[PDF 07, p.7]`.

**Cómo está montada la slide** `[PDF 07, p.7]`: arriba, las dos **series de precio** superpuestas
(Moderna en naranja, Novo Nordisk en azul); abajo, un gráfico de barras con **cuatro series de
rentabilidad** — *NOVO B Return On Equity %*, *NOVO B Return on Capital %*, *MRNA Return On Equity %*,
*MRNA Return on Capital %* — por ejercicios. **Fuente del gráfico: TIKR.com** (marca de agua) →
concuerda con D-06.

**La lectura que hace** (los deícticos de color ahora **sí** se verifican contra la slide):
- Moderna: «tuvo un pico especulativo por el COVID, pero su rentabilidad cayó rápidamente»
  `[VÍDEO 07, 09:01–09:07]`; «el ROIC que está en **naranja**, este va a la baja y presenta a la vez
  un ROE inestable» `[VÍDEO 07, 09:07–09:14]` → en la slide, *MRNA Return on Capital %* es
  efectivamente la serie naranja ✓
- Novo Nordisk: «en **negro** está el ROIC y en **azul** está el ROE» `[VÍDEO 07, 09:24–09:28]` → en
  la slide, *NOVO B Return on Capital %* es la serie oscura y *NOVO B Return On Equity %* la azul ✓
- «tiene un ROIC muy elevado y consistente, por tanto es un negocio de calidad, a diferencia del
  naranja de Moderna que es negativo» `[VÍDEO 07, 09:28–09:36]`
- Señal que extrae: «estos son señales que muestran que tiene dificultad para mantener la rentabilidad
  pese a la escala» `[VÍDEO 07, 09:16–09:20]`
- Moraleja: «la importancia de mirar los fundamentales y no dejarse llevar solo por el precio, porque
  uno estaba volando con unas métricas malas y otro estaba poco a poco subiendo con métricas muy
  buenas» `[VÍDEO 07, 09:36–09:47]`

> *En el piloto v1 estas afirmaciones quedaron marcadas como «deícticas y no verificables». Con el
> deck **sí** son verificables, y las tres referencias de color casan.*

---

## 11. Errata de la fuente

> **Cuatro tipos** (`moldes.md`): `T1` voz↔PDF · `T2` voz↔voz · `T3` PDF↔PDF · `T4` ambigüedad de
> transcripción. **Se registran, NO se resuelven.** Índice: `erratas_piloto.md`.
> *(Las erratas 07-E3, 07-E4 y 07-E7 viven en [[roe]] §11 — afectan a esa métrica.)*

### 07-E1 · `T1` · Unidad de análisis: «empresas» (voz) vs «Industrias» (slide)

| | |
|---|---|
| **VOZ** | «aquí podemos ver el ROIC promedio de distintas **empresas** del mercado» `[VÍDEO 07, 07:00]` |
| **PDF** | Título del gráfico: «**Industrias** con ROIC > 15% promedio desde 1998 (US)» `[PDF 07, p.5]` |
| **Choque** | El gráfico agrega por **industria**; la voz lo lee como si fueran **empresas**. Unidades de análisis distintas. Afecta a las tres cifras leídas sobre esa slide (5-15%, 8-10%, y el 15%). |
| **Cuerpo** | La voz (jerarquía), con el contexto de la slide anotado en §3d. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |

### 07-E2 · `T1` · Función del par ROIC+ROE: «detectar calidad» (voz) vs «descartar mediocres» (slide)

| | |
|---|---|
| **VOZ** | «ambos juntos forman un filtro potente para **detectar empresas de calidad**» `[VÍDEO 07, 03:08]` |
| **PDF** | «Ambas medidas juntas son un potente filtro para **al menos descartar empresas mediocres**» `[PDF 07, p.2]` |
| **Choque** | Operaciones distintas: **cribar dentro** (encontrar buenas) vs **cribar fuera** (eliminar malas). El «al menos» del deck es más modesto que la voz. Afecta al rol del par en el método. |
| **Cuerpo** | La voz. Ambas versiones citadas en §6. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |

### 07-E5 · `T2` · ⭐ El promedio de mercado del ROIC: **13-15%** contra **8-10%**

| | |
|---|---|
| **Polo A** | «que sepáis que **el promedio de mercado**, el ROIC se encuentra entre el **13 y el 15%**» `[VÍDEO 07, 03:49]` |
| **Polo B** | «porque **el ROIC promedio del mercado** suele rondar entre el **8 y 10%**, lo que es un punto de referencia bastante útil» `[VÍDEO 07, 07:28]` |
| **En qué chocan** | **Misma expresión, rangos que no solapan**, con 3:39 de diferencia. Datos internos a la fuente que ayudan al revisor: **(a)** el Polo A tiene **testigo en el deck** — «El ROIC promedio de la bolsa se sitúa en torno al 13-15% de forma general» `[PDF 07, p.3]`; el Polo B **no tiene ancla en ninguna slide**. **(b)** El Polo B se dice sobre `[PDF 07, p.5]`, un gráfico **filtrado a >15%**, que por construcción no muestra el promedio del mercado. **(c)** No confundir con el «5-15%» de `[VÍDEO 07, 07:19]`: **ese no es un tercer promedio**, es una lectura de la nube de puntos de la p.5 → resuelto como contexto distinto en §3d, **no es errata**. |
| **Qué lleva el cuerpo** | **LOS DOS**, con su contexto, en §3d. **No se elige.** `T2` **no tiene jerarquía**: los dos polos son voz, así que la regla voz>PDF no aplica y el deck solo hace de testigo de uno. Elegir sería criterio propio → **RD-1**. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |
| **Por qué importa** | **No es cosmético: decide el sentido del UMBRAL A.** Con promedio 8-10%, «>15% sostenido» es una barra exigente. Con promedio 13-15%, 15% es el borde superior de la media. Dos lecturas muy distintas del único umbral operativo del vídeo. |

### 07-E6 · `T2` · «estas dos primeras» no son las dos primeras de su propia enumeración

| | |
|---|---|
| **Polo A** | «hay diferentes formas (**ROA, ROCE, ROE y el ROIC**)…» `[VÍDEO 07, 02:18]` |
| **Polo B** | «…pero nos vamos a centrar en **estas dos primeras**, en el **ROIC y en el ROE**» `[VÍDEO 07, 02:18]` |
| **En qué chocan** | En la enumeración que **acaba de decir**, ROIC va el **cuarto** y ROE el **tercero**: no son «las dos primeras». Dato interno que ayuda al revisor: **el deck las lista en otro orden** — «ROIC · ROCE · ROE · ROA» `[PDF 07, p.1]` — donde el ROIC sí es el primero, pero el ROE sigue siendo el tercero. **Con ninguno de los dos órdenes cuadra «las dos primeras».** Probable deíctico sobre la slide. |
| **Qué lleva el cuerpo** | El par ROIC+ROE como los elegidos (que es lo que hace el resto del vídeo y confirma `[PDF 07, p.2]`: «Nos centramos en 2 indicadores»). La referencia «dos primeras» **no se usa** para nada. §7 lo anota. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` — probablemente inocuo, pero cuenta para la tasa de error. |

### 07-E9 · `T4` · «el WAC»: la transcripción no determina el término

| | |
|---|---|
| **Polo A** | «un ROIC consistentemente superior al coste del capital **que es el WAC**» `[VÍDEO 07, 07:12–07:19]` · «proyectos que generan más rentabilidad de lo que cuestan **(WAC)**» `[VÍDEO 07, 10:54]` |
| **Polo B** | — *(indeterminación)*. **Ninguna página del deck rotula el término**, así que no hay testigo visual. |
| **En qué chocan** | Aparece **dos veces con la misma grafía**, lo que puede indicar (a) que es como el experto lo dice, o (b) una mistranscripción sistemática de la máquina (la consonante final es fácil de perder). **La transcripción sola no permite decidirlo**, y sin slide no hay contraste. |
| **Qué lleva el cuerpo** | **«el WAC», literal** (§3 UMBRAL B). **No se expande** a ninguna forma larga: hacerlo sería aportar conocimiento externo → **RD-1**. D-46: no se corrigen los errores del experto, y aquí ni siquiera se sabe si es suyo. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` — se desbloquea **verificando el `.srt` contra el vídeo** (D-46). |

### 07-E8 · `T4` · «y la rima»: cierre corrupto

| | |
|---|---|
| **Polo A** | «no basta con ratios altos, también importa su consistencia en el tiempo **y la rima**» `[VÍDEO 07, 11:21–11:31]` |
| **Polo B** | — *(indeterminación)*. Última frase del vídeo; **no hay slide** (el deck termina en p.7). |
| **En qué chocan** | «y la rima» **no tiene sentido** en el contexto (consistencia temporal de un ratio). Texto aparentemente corrupto: la transcripción no determina qué dijo. |
| **Qué lleva el cuerpo** | **Literal, sin interpretar** (§8). No se sustituye por ninguna conjetura → RD-1 / D-46. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` — se desbloquea **verificando el `.srt` contra el vídeo** (D-46). |

### Aportes que NO son errata (las capas no chocan, se complementan)

- **Solo-verbal:** la fórmula del ROIC (dibujada a mano, `[VÍDEO 07, 04:18]`); la comparación con el
  sector en el histórico `[VÍDEO 07, 03:37]`; toda la tesis de superioridad sobre el ROE (§7); el
  «me gusta / no me gusta».
- **Solo-PDF:** la relativización sectorial explícita del promedio `[PDF 07, p.3]`; el criterio
  «mejor ROIC **del sector**» como señal de moat `[PDF 07, p.3]`; el alcance del gráfico («US»,
  «desde 1998») `[PDF 07, p.5]`; TIKR como proveedor `[PDF 07, p.7]`.

---

## 12. Fuente

- **Vídeo 07 — «ROIC vs ROE»**, `raw/transcript/07_roic_vs_roe.srt` (canónico, D-46).
  Rango citado: `00:09–11:31` (completo). Clase `[VÍDEO]`.
- **Deck 07**, `raw/pdf/07_roic_vs_roe.pdf`, 7 páginas, sección **«5. LA RENTABILIDAD»**.
  Clase `[PDF]`. Páginas usadas: p.1 (concepto y las 4 métricas), p.2 (ROIC vs ROE en paralelo),
  p.3 (consideraciones ROIC + el 13-15%), p.4 (consideraciones ROE), p.5 (gráfico ROIC sectorial),
  p.6 (gráfico ROE sectorial), p.7 (demostración Novo/Moderna).
- **Cobertura del deck sobre el vídeo:** alta. La única laguna es la **fórmula dibujada a mano**
  `[VÍDEO 07, 04:18–04:36]`, que no está en ninguna página.
- **Capturas:** ya **no son necesarias** para este vídeo — el deck cubre los artefactos visuales que
  en el piloto v1 quedaron sin verificar (tabla comparativa → p.2; gráfico ROIC → p.5; gráfico ROE →
  p.6; gráficos Novo/Moderna → p.7). *Salvo* la anotación en directo de la fórmula.
- **`[ENLACE-DESC]`:** no aplica — ningún recurso enlazado en la descripción.
