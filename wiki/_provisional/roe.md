---
concepto: ROE (Return on Equity)
modulo: 07
molde: 1
estado: piloto
fuentes: [VIDEO-07, PDF-07]
enlaces: [roic, balance_general]
---

# ROE

> ⛔ **SUPERSEDIDA (2026-07-19).** Rehecha con el molde 1 definitivo (v4) en
> `wiki/curso/roe.md` — con el campo *Punto ciego* (nuevo desde el piloto) y la aplicabilidad a
> dos ranuras. Esta ficha **no se borra** (D-18, traza) pero **no se consulta como método**.

> ⚠️ **FICHA DE PILOTO.** Valida el MOLDE 1 v2 (`moldes.md`). No se promueve a `curso/`.
> Fuentes: `raw/transcript/07_roic_vs_roe.srt` (voz) + `raw/pdf/07_roic_vs_roe.pdf` (deck,
> sección «5. LA RENTABILIDAD»).
> **Ficha hermana de [[roic]]** — la tesis comparativa del vídeo se cruza entre las dos (§6, §7).

---

## 1. Definición y fórmula

**Definición.** El ROE «mide el retorno sobre los fondos propios, y esto afecta sobre todo al
accionista, y es que evalúa qué tanto gana el accionista por su inversión» `[VÍDEO 07, 02:53–03:03]`.
El deck lo titula **«RETORNO SOBRE LOS FONDOS PROPIOS (EQUITY) / Return on Equity»** y lo define como
«Indicador que nos indica **cuánto ha ganado la compañía como % del dinero de los accionistas**»
`[PDF 07, p.2]`. Ampliado: «nos cuenta la rentabilidad que obtiene el accionista a partir del capital
que ha invertido en la Compañía» `[PDF 07, p.4]`.

**Encuadre.** Pertenece a la **rentabilidad financiera** `[PDF 07, p.1 + VÍDEO 07, 01:59]`.

> ⚠️ **Anomalía interna del deck** (registrada, no corregida). `[PDF 07, p.1]` define la rentabilidad
> financiera como «el beneficio que los accionistas de la compañía obtienen por haber invertido en
> ella», y a continuación añade: «**En otras palabras**, mide la capacidad del negocio para generar
> ingresos a través de las inversiones» — formulación muy próxima a la que el mismo deck usa para la
> rentabilidad **económica** en esa misma página («el beneficio promedio de la compañía por el total
> de las inversiones hechas»). **La voz no dice la segunda cláusula**, solo la primera: «mide la
> ganancia sobre el equity, sobre los fondos propios» `[VÍDEO 07, 01:59]`.
> No se resuelve. **No cabe en `## Errata de la fuente`**, que solo cubre choques voz↔PDF, y esto es
> una inconsistencia **interna del PDF**. Ver `piloto_friccion.md`.

**Fórmula — `[HUECO]` en LAS DOS CAPAS.**

**Ni la voz ni el deck dan la fórmula del ROE.** Lo que dan es la definición del **denominador**:

> «El EQUITY lo obtenemos por la diferencia entre los ACTIVOS (ASSETS) los PASIVOS (LIABILITIES)»
> `[PDF 07, p.4]`
>
> «se calcula cogiendo el equity, que es igual a los activos menos los pasivos, que esto acordaros,
> ya lo dimos en uno de los tres estados financieros» `[VÍDEO 07, 04:52–05:03]` → [[balance_general]]

**El numerador nunca se enuncia, en ninguna capa.** Completarlo con «beneficio neto / equity» sería
rellenar por conocimiento externo — prohibido (RD-1, RD-4). Se deja vacío.

> **Asimetría con [[roic]]:** el ROIC recibe fórmula completa (dibujada a mano, `[VÍDEO 07, 04:18]`);
> el ROE no recibe ninguna en ninguna capa. El piloto v1 dejó abierto si el PDF la traería.
> **No la trae.** El hueco es de la fuente, no del material disponible.

*Resolución esperada:* módulo posterior, o `complemento/` con tres pilares.

---

## 2. Qué mide / interpretación direccional

**La dirección es ambigua por diseño, y el experto lo sabe.** Más alto es mejor *para el accionista*,
pero un ROE más alto puede significar **menos equity**, no mejor negocio:

> «cuanto menos equity más alto es el ROE, y esto si el beneficio se mantiene» `[VÍDEO 07, 05:31–05:35]`

Y por tanto:

> «el ROE no siempre refleja eficiencia de negocios sino **eficiencia para el accionista**,
> condicionada por algunas decisiones financieras como el apalancamiento o como la recompra de
> acciones» `[VÍDEO 07, 08:16–08:26]`

Esto hace que el ROE sea la única de las dos métricas del vídeo en la que **subir puede ser mala
señal** (ver §3 UMBRAL B y §9).

> ⚠️ **Todo este matiz es solo-verbal.** El deck no lo insinúa: presenta el ROE como «una métrica muy
> buena para comparar empresas financieras» `[PDF 07, p.2]` y su única reserva es que «no tiene en
> cuenta la deuda» `[PDF 07, p.4]`. Ver §11 (07-E3).

---

## 3. Umbral(es)

### UMBRAL A — «promedio de mercado ≈ 14%»

**3a · Valor + procedencia** — **DOS CAPAS.**
- **PDF:** «El ROE promedio del mercado está en torno al **14%**» `[PDF 07, p.4]`
- **Voz:** «el ROE promedio del mercado está en torno al **14%**» `[VÍDEO 07, 05:24]` — literal, lee
  la slide.
- **Variante solo-verbal, compatible:** «el ROE promedio del mercado suele situarse entre el **10 y
  15%**» `[VÍDEO 07, 08:13]`, dicho sobre `[PDF 07, p.6]`. El 14% cae dentro. **No es tensión.**

**3b · Clase — `[ABSOLUTO-RELATIVIZADO]`, con anclaje MÁS DÉBIL que el del [[roic]].**
El deck da la cifra absoluta y la regla sectorial en **dos bullets contiguos de la misma página**:

> «**Debe usarse para comparar empresa del mismo sector.** Y se suele usar en el sector financiero.»
> «El ROE promedio del mercado está en torno al 14%.» `[PDF 07, p.4]`

Y la voz igual: «debe usarse para comparar empresas del mismo sector, a diferencia del ROIC que
permite comparar entre distintos sectores» `[VÍDEO 07, 05:15–05:19]`.

⚠️ **Pero el experto NUNCA conecta los dos bullets** — a diferencia del [[roic]], donde los une en una
sola frase con un «porque luego» explícito (`[PDF 07, p.3]`). Aquí la conexión la hace el lector.
**Se marca la clase, y se marca que su anclaje es de dos frases sueltas, no de una.**

**Fuente viva del benchmark sectorial (D-56):** `[HUECO]`. El gráfico `[PDF 07, p.6]` dice «desde
1998 (US)» y **no lleva atribución**. Damodaran no aparece ni en la voz ni en el deck del 07.

**3c · Justificación del experto — `AUSENTE`.** Ninguna capa dice de dónde sale el 14% ni por qué.
⚠️ **D-08: no se adopta por autoridad.**

**3d · Tensión — la cifra y su regla de uso se contradicen.**
El experto da un número **de mercado** (14%; 10-15%) y a la vez prohíbe la comparación **a nivel de
mercado** («debe usarse para comparar empresas del mismo sector»). El 14% es, según su propia regla,
un número que no debería usarse tal cual. **Está en las dos capas, así que no es lapsus.**
No se resuelve: se registra. `PENDIENTE DE REVISIÓN HUMANA`.

### UMBRAL B — «ROE > 30% → examinar con lupa»

**Es un TECHO, no un suelo.**

**3a · Valor + procedencia** — **solo voz, sin ancla en ninguna slide.**
> «empresas con un ROE muy alto **por encima del 30%** deben examinarse con lupa porque puede ser
> debido a un apalancamiento excesivo» `[VÍDEO 07, 08:02–08:13]`

**3b · Clase — `[ABSOLUTO]`**, tal como se enuncia: no lo relativiza a nada.
⚠️ Choca con su propia regla de uso (comparar dentro del sector, §3 UMBRAL A 3b). Y `[HUECO]`: **no
dice si en un banco el techo del 30% sigue valiendo**, siendo el apalancamiento consustancial al
negocio bancario — pregunta que su propio criterio hace inevitable, y que ninguna capa aborda.

**3c · Justificación del experto — `PRESENTE`**, y es la única justificación de umbral del vídeo:
«**porque puede ser debido a un apalancamiento excesivo**» `[VÍDEO 07, 08:02]`. Es un mecanismo, no
una autoridad. *(Aun así no dice por qué 30% y no 25% o 40%.)*

**3d · Tensiones** — ninguna.

### ⚠️ Umbral del deck que la voz NUNCA enuncia

El gráfico de ROE está construido con el mismo filtro que el de ROIC: **«Industrias con ROE > 15%
promedio desde 1998 (US)»** `[PDF 07, p.6]`. Pero **el experto no enuncia jamás un umbral del 15%
para el ROE** — solo para el ROIC `[VÍDEO 07, 07:22]`. Sobre esta slide habla de 10-15% (promedio) y
de 30% (techo), nunca de 15% como criterio.

**Aporte solo-PDF, no verbalizado → NO se adopta como umbral.** Se registra la existencia del filtro.

---

## 4. Aplicabilidad condicionada

**Sirve para: el sector FINANCIERO.** Dos capas.
- «Es una métrica muy buena para **comparar empresas financieras**» `[PDF 07, p.2]`; «se suele usar en
  el sector financiero» `[PDF 07, p.4]`
- «últimamente está muy utilizado en empresas financieras» `[VÍDEO 07, 03:03–03:08]`; «el ROE suele
  usarse en el sector financiero» `[VÍDEO 07, 05:19]`

**Sirve para: comparar DENTRO del mismo sector, nunca entre sectores.** Dos capas.
- «**Debe usarse para comparar empresa del mismo sector**» `[PDF 07, p.4]`
- «debe usarse para comparar empresas del mismo sector, a diferencia del ROIC que permite comparar
  entre distintos sectores» `[VÍDEO 07, 05:15–05:19]`

Es la restricción de aplicabilidad más dura del vídeo, y la única respaldada por las dos capas.

**Sirve para: aportar la perspectiva del accionista**, como complemento del [[roic]]: «también el ROE
nos da una visión desde la cara del accionista» `[VÍDEO 07, 11:18–11:27]`. Solo-verbal.

`[HUECO]` **Por qué el ROE es la métrica del sector financiero.** Ninguna capa da el fundamento:
ambas observan la práctica («suele usarse», «está muy utilizado»). *Resolución esperada:*
`complemento/`. **No se rellena por deducción.**

---

## 5. Advertencia de uso aislado / cuándo engaña

**El campo más denso de la ficha — y casi todo es SOLO-VERBAL.**

**Limitación estructural — la única que respalda el deck:**

> «La principal desventaja o limitación que tiene esta métrica es que **no tiene en cuenta la deuda
> de la compañía**» `[PDF 07, p.4]`
>
> «es la principal desventaja o limitación que tiene esta métrica, y es que no tiene en cuenta la
> deuda de la compañía, **por eso debe usarse con precaución**» `[VÍDEO 07, 05:03–05:15]`
> — *«por eso debe usarse con precaución» es añadido de la voz.*

**Mecanismos de inflado — enumerados por la voz, AUSENTES del deck por completo:**

1. **Deuda / apalancamiento.** «una empresa con mucha deuda puede mostrar un ROE alto, pero eso no
   significa que el negocio sea eficiente, porque quizás no lo están gestionando bien»
   `[VÍDEO 07, 03:11–03:19]`; «el ROE se puede inflar con deuda» `[VÍDEO 07, 05:29]`.
2. **Recompra de acciones.** «una empresa que recompre acciones reduce su equity y sube
   **artificialmente** el ROE, en cambio no mejora su negocio real, **por eso no me gusta el ROE**»
   `[VÍDEO 07, 05:35–05:46]`.
3. **Cambios contables.** «el ROE se puede inflar mediante recompra de acciones, endeudamiento o
   **cambios contables**» `[VÍDEO 07, 08:26–08:32]`.

**Conclusión:** «el ROE por sí solo no basta, necesitamos el ROIC para tener una visión mucho más
limpia» `[VÍDEO 07, 05:46–05:52]`. Solo-verbal.

> ⚠️ **Hallazgo del contraste de capas:** el deck **no advierte de ninguno de los tres mecanismos**.
> Toda la desconfianza hacia el ROE vive en la voz. Ver §11 (07-E3).

`[HUECO]` No explica **cómo** los cambios contables inflan el ROE (mecanismo 3, enunciado y no
desarrollado, en ninguna capa). *Resolución esperada:* `complemento/`.

---

## 6. Lectura relacional

> La tesis comparativa del vídeo vive **repartida entre esta ficha y [[roic]]**. Aquí, desde el lado
> del ROE: el ROE **necesita** al ROIC. Allí, desde el lado del ROIC: el ROIC **no necesita** al ROE
> pero lo complementa. Es la misma tesis vista por sus dos extremos.

| Se cruza con | Cómo | Fuente |
|---|---|---|
| **[[roic]]** | «Ambas medidas juntas son un potente filtro para al menos descartar empresas mediocres» | `[PDF 07, p.2]` |
| **[[roic]]** | «ambos juntos forman un filtro potente para detectar empresas de calidad» | `[VÍDEO 07, 03:08]` |
| **[[roic]]** | «el ROIC y el ROE deben analizarse juntos, no por separado» | `[VÍDEO 07, 11:07]` |
| **[[roic]]** | ⭐ El ROE **no se puede leer solo**: «el ROE por sí solo no basta, necesitamos el ROIC para tener una visión mucho más limpia» | `[VÍDEO 07, 05:46]` |
| **[[roic]]** | Patrón bueno: «un ROIC superior al 15% con un ROE **equilibrado sin distorsión por deuda**» | `[VÍDEO 07, 08:40]` |
| **[[roic]]** | Patrón malo: «un ROE altísimo y un ROIC medio o bajo, cuidado» | `[VÍDEO 07, 08:47]` |
| **Deuda / apalancamiento** | Mecánico: más deuda → menos equity → más ROE, sin mejorar el negocio | `[VÍDEO 07, 03:11]`, `[VÍDEO 07, 05:29]` |
| **Recompra de acciones** | Mecánico: recompra → menos equity → ROE «artificialmente» alto | `[VÍDEO 07, 05:35]` |
| **Equity** → [[balance_general]] | El denominador sale del balance: «los activos menos los pasivos» | `[PDF 07, p.4 + VÍDEO 07, 04:52]` |

> **La lectura relacional del ROE no es opcional: es constitutiva.** El experto no lo presenta como
> una métrica que *se puede* cruzar con el ROIC, sino como una que **no se puede leer sola**
> `[VÍDEO 07, 05:46]`. Diferencia de grado con el [[roic]], del que dice que «por sí solo no es
> suficiente» `[VÍDEO 07, 03:59]` pero al que sí llama «la mejor métrica» `[VÍDEO 07, 10:02]`.

---

## 7. Recomendación comparativa

**El experto prefiere el [[roic]], en primera persona — y esto NO está en el deck.**

- «por eso el ROIC en este aspecto me gusta mucho más que el ROE» `[VÍDEO 07, 04:15]`
- «por eso **no me gusta el ROE**» `[VÍDEO 07, 05:43]`
- «el porqué el ROIC **es superior** al ROE» `[VÍDEO 07, 05:52]`
- «el ROIC es más fiable para comparar modelos de negocio» `[VÍDEO 07, 08:32]`
- «el ROIC es la mejor métrica para evaluar si una empresa crea valor y **el ROE lo que hace es
  complementar, pero siempre hay que matizarlo**» `[VÍDEO 07, 10:02–10:11]`

**Criterio de la preferencia** (el porqué, no solo el qué): el ROIC «tiene en cuenta la deuda más el
equity, en cambio el ROE se enfoca solo en lo que gana el accionista» `[VÍDEO 07, 05:57–06:05]`; el
ROIC va «sin verse distorsionado por decisiones financieras como apalancamientos o recompra de
acciones **que sí lo tiene el ROE**» `[VÍDEO 07, 06:15–06:26]`.

**Pero el ROE NO se descarta:** «el ROIC y el ROE deben analizarse juntos, no por separado, **a pesar
de que el ROIC sea mucho mejor que el ROE**, también el ROE nos da una visión desde la cara del
accionista» `[VÍDEO 07, 11:07–11:27]`.

**Rol resultante:** métrica **complementaria y subordinada**, con función propia (perspectiva del
accionista) que el ROIC no cubre.

> ⚠️ **El deck NO jerarquiza.** `[PDF 07, p.2]` presenta ROIC y ROE en dos cajas simétricas, cada una
> «una métrica muy buena» para su ámbito. **La subordinación del ROE es enteramente de la voz.**
> Ver §11 (07-E3).

---

## 8. Consistencia temporal

- **El ROE es estructuralmente más disperso que el [[roic]]** — y el deck lo respalda **visualmente**:
  «a diferencia del ROIC, el ROE es más disperso porque depende directamente de la estructura de
  capital, que suelen ser empresas muy apalancadas que muestran un ROE más alto pero, atención, con
  mayor riesgo» `[VÍDEO 07, 07:48–08:00]`.
  → El eje del gráfico de ROE llega al **250%** `[PDF 07, p.6]`; el de ROIC, al **120%**
  `[PDF 07, p.5]`. Las dos slides son gemelas y están construidas con el mismo filtro (>15% promedio
  desde 1998), así que la diferencia de escala es del dato, no del diseño.
  *(En el piloto v1 esta afirmación no se podía verificar. Ahora sí.)*
- Cierre general, aplicable a las dos métricas: «no basta con ratios altos, también importa su
  consistencia en el tiempo y la rima» `[VÍDEO 07, 11:21–11:31]`.
- «ROE inestable» aparece como señal negativa **solo dentro de la demostración** → ver §10 de [[roic]].
  Por D-49 no se promueve a regla.

`[HUECO]` **El experto no pide nunca ROE estable ni creciente**, a diferencia del ROIC, donde ambas
capas lo exigen («Es deseable ver un ROIC estable o que aumenta con el tiempo», `[PDF 07, p.3]`).
`[PDF 07, p.4]` no dice **nada** sobre la evolución temporal del ROE. **No se traslada el requisito
del ROIC por simetría.**

---

## 9. Banderas rojas

- **ROE > 30%** → «deben examinarse con lupa porque puede ser debido a un apalancamiento excesivo»
  `[VÍDEO 07, 08:02–08:13]`. *(También en §3 UMBRAL B: el mismo dato es umbral y bandera roja. El
  molde no da regla de desempate — ver `piloto_friccion.md`.)*
- **ROE altísimo + ROIC medio o bajo** → «cuidado porque el negocio puede ser que no sea tan eficiente
  como parece» `[VÍDEO 07, 08:47–08:55]`.
- **ROE alto en empresa muy apalancada** → «empresas muy apalancadas que muestran un ROE más alto
  pero, **atención, con mayor riesgo**» `[VÍDEO 07, 07:55–08:00]`.
- **ROE que sube tras recompras** → «sube artificialmente el ROE, en cambio no mejora su negocio real»
  `[VÍDEO 07, 05:40–05:46]`.

> **Las cuatro son solo-verbales: el deck no señala ninguna bandera roja del ROE.**
>
> Y todas son «ROE alto». `[HUECO]`: ninguna capa dice qué significa un ROE **bajo**, ni si hay suelo.

---

## 10. Demostración / ejemplar del experto

**Novo Nordisk vs Moderna** `[VÍDEO 07, 08:55–10:20]` + `[PDF 07, p.7]`.

La demostración es **compartida con [[roic]]** — es una lectura *cruzada* de las dos métricas, no de
una. **Está desarrollada en [[roic]] §10** para no duplicarla. Lo que aporta del lado del ROE:

- El deck pide explícitamente el cruce: «Compara **el ROE y ROIC** de Novo Nordisk con el ROE y ROIC
  de Moderna» `[PDF 07, p.7]`.
- Moderna: «presenta a la vez un **ROE inestable**» `[VÍDEO 07, 09:14]` — es la única vez que el ROE
  inestable aparece como señal, y es dentro del ejemplar.
- Novo Nordisk: «en **azul** está el ROE» `[VÍDEO 07, 09:24]` → en la slide, *NOVO B Return On
  Equity %* es la serie azul ✓

> ⚠️ **PEDAGOGÍA, no metodología. No entra en el Inventario Atómico. No se transcriben cifras**
> (RD-1 + D-49).

---

## 11. Errata de la fuente

> **Cuatro tipos** (`moldes.md`): `T1` voz↔PDF · `T2` voz↔voz · `T3` PDF↔PDF · `T4` ambigüedad de
> transcripción. **Se registran, NO se resuelven.** Índice: `erratas_piloto.md`.
> *(Las erratas 07-E1, 07-E2, 07-E5, 07-E6, 07-E8 y 07-E9 viven en [[roic]] §11.)*

### 07-E3 · `T1` · Postura sobre el ROE: el deck lo respalda, la voz lo desautoriza

| | |
|---|---|
| **VOZ** | «por eso **no me gusta el ROE**» `[VÍDEO 07, 05:43]` · «el ROIC es superior al ROE» `[VÍDEO 07, 05:52]` · «el ROE lo que hace es complementar, pero siempre hay que matizarlo» `[VÍDEO 07, 10:02]` · tres mecanismos de inflado (deuda, recompras, cambios contables) `[VÍDEO 07, 03:11 / 05:35 / 08:26]` |
| **PDF** | «Es una **métrica muy buena** para comparar empresas financieras» `[PDF 07, p.2]`, en una caja **simétrica** a la del ROIC. Su única reserva: «no tiene en cuenta la deuda de la compañía» `[PDF 07, p.4]`. **Ningún mecanismo de inflado. Ninguna jerarquía. Ninguna bandera roja.** |
| **Choque** | El deck presenta dos métricas **equivalentes**, cada una buena en su ámbito. La voz construye una **jerarquía** (ROIC superior, ROE subordinado y sospechoso) que el material escrito no sostiene. No es un choque de dato: es de **postura**, y afecta al rol del ROE en el método. |
| **Cuerpo** | La voz (jerarquía): la ficha registra la subordinación y los tres mecanismos, con la postura del deck anotada en §2, §5 y §7. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |

### 07-E4 · `T1` · Umbral del 15% presente en el gráfico de ROE y nunca verbalizado

| | |
|---|---|
| **VOZ** | Sobre esa slide habla de 10-15% (promedio) y >30% (techo). **Nunca menciona el 15% como criterio de ROE** `[VÍDEO 07, 07:43–08:26]` |
| **PDF** | El gráfico está filtrado: «Industrias con **ROE > 15%** promedio desde 1998 (US)» `[PDF 07, p.6]` |
| **Choque** | La slide encarna un umbral del 15% para el ROE que la voz no enuncia. No es contradicción, es **silencio sobre un criterio visible**. Relevante porque el 15% **sí** se verbaliza para el ROIC `[VÍDEO 07, 07:22]`, y las dos slides son gemelas. |
| **Cuerpo** | No se adopta como umbral (§3). Solo se registra la existencia del filtro. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |

### 07-E7 · `T3` · El deck define la rentabilidad financiera y la reformula con la fórmula de la económica

| | |
|---|---|
| **Polo A** | «**RENTABILIDAD FINANCIERA.** Se refiere al beneficio que **los accionistas** de la compañía obtienen por haber invertido en ella, también expresada en términos %.» `[PDF 07, p.1]` |
| **Polo B** | «**En otras palabras**, mide la capacidad **del negocio** para generar ingresos a través de **las inversiones**.» `[PDF 07, p.1]` — la frase inmediatamente siguiente, en la misma caja |
| **En qué chocan** | El «en otras palabras» **no reformula el Polo A: lo cambia de sujeto**. El A mide lo que gana **el accionista**; el B, lo que genera **el negocio sobre las inversiones**. Dato interno que ayuda al revisor: el B se parece mucho a la definición que **esa misma página** da para la rentabilidad **ECONÓMICA** — «el beneficio promedio de la compañía **por el total de las inversiones hechas**» `[PDF 07, p.1]`, que es la otra mitad de la slide. |
| **Testigo de la voz** | ⚠️ **Parcial.** La voz solo dice el Polo A: «la rentabilidad financiera mide la ganancia sobre el equity, sobre los fondos propios» `[VÍDEO 07, 01:59]`. **Sobre el Polo B calla**: no lo lee ni lo contradice. |
| **Qué lleva el cuerpo** | El **Polo A** (§1), por ser el único con testigo en la voz. **El Polo B se registra aquí y NO se descarta**: `T3` sin testigo pleno no se dictamina — la voz calla sobre él, no lo niega. |
| **Estado** | `PENDIENTE DE REVISIÓN HUMANA` |

*(Ver también **07-E1**, **07-E2**, **07-E5**, **07-E6**, **07-E8** y **07-E9** en [[roic]] §11:
afectan al vídeo entero o a la otra métrica.)*

### Aportes que NO son errata (las capas se complementan)

- **Solo-verbal:** los tres mecanismos de inflado; el «no me gusta»; toda la jerarquía ROIC>ROE; la
  dispersión como argumento; las cuatro banderas rojas; el techo del 30%.
- **Solo-PDF:** el filtro >15% del gráfico `[PDF 07, p.6]`; la escala de 250% que respalda la
  dispersión; el alcance del dato («US», «desde 1998»).

---

## 12. Fuente

- **Vídeo 07 — «ROIC vs ROE»**, `raw/transcript/07_roic_vs_roe.srt` (canónico, D-46).
  Rango citado: `01:47–11:31`. Clase `[VÍDEO]`.
- **Deck 07**, `raw/pdf/07_roic_vs_roe.pdf`, sección **«5. LA RENTABILIDAD»**. Clase `[PDF]`.
  Páginas usadas: p.1 (rentabilidad financiera), p.2 (ROE en paralelo al ROIC), p.4 (consideraciones
  ROE + el 14%), p.6 (gráfico ROE sectorial), p.7 (demostración).
- **Cobertura del deck sobre el contenido de ROE:** **parcial y asimétrica**. El deck cubre
  definición, limitación de la deuda, uso sectorial y promedio. **No cubre** nada de lo que hace al
  ROE sospechoso: ni mecanismos de inflado, ni banderas rojas, ni el techo del 30%, ni la
  subordinación al ROIC. Ese ~60% de la ficha es **solo-verbal**.
- **Capturas:** ya **no necesarias** — el deck cubre los artefactos visuales del vídeo.
- **`[ENLACE-DESC]`:** no aplica.
