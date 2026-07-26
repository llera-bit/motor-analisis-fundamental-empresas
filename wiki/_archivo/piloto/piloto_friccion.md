# piloto_friccion.md — Reporte de fricción · **v2**

> **v1** (piloto 1): 3 moldes contra solo la transcripción. **v2** (este): los 5 arreglos aplicados +
> el PDF como capa visual. Todo sigue en `wiki/piloto/`. Nada promovido a `curso/`. Nada commiteado.
> `CLAUDE.md`, `decisiones.md` y `log.md` **intactos**.
>
> **Los moldes no existían como archivo.** Solo habían vivido en tus mensajes de tarea; `CLAUDE.md`
> §4 sigue con los moldes viejos. No ha sido una edición: ha sido la **primera codificación**, en
> `moldes.md`. Es el único sitio donde poner los 5 arreglos sin tocar lo que me prohibiste tocar.

---

## 0. Veredicto en una tabla

| | Molde 1 | Molde 2 | Molde 3 |
|---|---|---|---|
| **v1** | Aguanta, 2 agujeros graves | El más sólido | **No aguanta** |
| **v2** | ✅ Aguanta | ✅ Aguanta | ✅ **Aguanta** |
| **Arreglos que rindieron** | 4 (umbral desdoblado) ⭐⭐ · 5 (demostración) ✅ · 3 (erratas) ✅ | 5 ✅ · 3 ✅ | 1 (contraejemplos/erosión/causal) ⭐⭐ · 2 (dirección) ✅ · 3 ✅ |
| **Contenido aún sin campo** | Concepto paraguas · secuencia (D-51) | Naturaleza temporal · alcance · señales clave · secuencia (D-51) | Herramientas externas · normativa de estrategia |
| **Campos que fuerzan** | Ninguno | Ninguno | Ninguno |

**Los 5 arreglos funcionan.** Los tres moldes sostienen ahora lo que antes se caía. **Y el PDF ha
sido más decisivo que los arreglos**: resolvió seis cosas que v1 declaró no verificables, y **cambió
un veredicto** (§4.2).

**Lo que queda mal, en una frase:** el bloque de erratas —la pieza que alimenta la tasa de error de
la fuente— solo sabe ver **un** tipo de error de los **cuatro** que este piloto ha encontrado.

---

## 1. El caso del ROIC: qué reveló el PDF ⭐

**La pregunta era: ¿tres gráficos distintos que la transcripción aplanó, o contradicción real?**
**Respuesta: las dos cosas. El PDF resuelve una de las dos tensiones y afila la otra.**

| Cifra | Dónde se dice | Sobre qué slide | Capas | Veredicto v2 |
|---|---|---|---|---|
| **13-15%** «promedio de la bolsa» | `[VÍDEO 07, 03:49]` | `[PDF 07, p.3]`, slide de bullets. Literal: «El ROIC promedio de la bolsa se sitúa en torno al 13-15% de forma general» | **voz + PDF** | Referencia general de mercado |
| **5-15%** «la mayoría de empresas… que es la media» | `[VÍDEO 07, 07:19]` | `[PDF 07, p.5]`, scatter **«Industrias con ROIC > 15% promedio desde 1998 (US)»** | solo voz | ✅ **RESUELTO — otro contexto** |
| **8-10%** «promedio del mercado» | `[VÍDEO 07, 07:28]` | `[PDF 07, p.5]`, la misma slide | solo voz, **sin ancla** | ⛔ **SUBSISTE** |

### ✅ Lo que el PDF resolvió

**El 5-15% nunca fue un promedio rival.** La p.5 es un **scatter filtrado**: solo industrias cuya
media desde 1998 supera el 15%, con puntos anuales dispersos entre −20% y 120%. Cuando dice «la
mayoría de empresas tienen un ROIC entre el 5 y el 15%», **está leyendo la nube de puntos de ese
gráfico**, no dando un promedio de mercado. **Es una lectura de la slide, no un umbral.** Registrado
como tal en [[roic]] §3d.

> **v1 lo contó como una contradicción a tres bandas. Con el PDF, son dos.** La transcripción sola no
> podía saberlo: el contexto estaba en la pantalla.

**Y de propina, el PDF ancló dos cosas que v1 dejó en `[HUECO]`:**

- **El umbral del 15% tiene origen visible.** No es una cifra suelta: **es el criterio de construcción
  del gráfico** — «Industrias con ROIC **> 15%** promedio desde 1998 (US)» `[PDF 07, p.5]`.
- **La clase `[ABSOLUTO-RELATIVIZADO]` ya no es síntesis mía.** El deck relativiza **en la misma
  frase**: «El ROIC promedio de la bolsa se sitúa en torno al 13-15% de forma general. **Porque luego,
  cada sector tiene su propio ratio promedio**» `[PDF 07, p.3]`. Y el criterio de moat que da es
  sectorial: «la empresa con **mejor ROIC del sector** suele ser la empresa con mayor ventaja
  competitiva» `[PDF 07, p.3]`. **En v1 me negué a clasificarlo por no forzar. Ahora está anclado.**

### ⛔ Lo que subsiste, y por qué ningún mecanismo lo coge

**13-15% contra 8-10%.** Misma expresión, rangos que no solapan, tres minutos y medio de distancia.
El 13-15% tiene **las dos capas**; el 8-10% **no tiene ancla en ninguna slide**.

> ⚠️ **La regla de conflicto no aplica: es VOZ contra VOZ**, no voz contra PDF. El PDF solo hace de
> testigo de uno de los dos lados. Elegir sería criterio propio → **RD-1**. Queda registrado en
> [[roic]] §3d con las tres cifras y su contexto, `PENDIENTE DE REVISIÓN HUMANA`.

**Y no es cosmético:** el sentido del umbral operativo depende de cuál sea el promedio. Con promedio
8-10%, «>15% sostenido» es una barra exigente. Con promedio 13-15% —el que respaldan las dos capas—,
15% es el borde superior de la media. **Dos lecturas muy distintas del mismo criterio.**

---

## 2. MOLDE 1 · Métrica cuantitativa

### 2.1 ARREGLO 4 (umbral desdoblado) — ⭐⭐ **el arreglo más rentable del piloto**

**Sí, sostiene lo que antes quedaba mudo. Y el sub-campo que más rinde no es el que esperabas: es 3c.**

**3c · Justificación** convirtió un vacío invisible en un dato medible:

| Umbral | Ficha | 3c · Justificación del experto |
|---|---|---|
| ROIC > 15% sostenido | [[roic]] | ⛔ **AUSENTE** — ninguna capa dice por qué 15% |
| ROIC > coste del capital | [[roic]] | ✅ presente — «puede reinvertir en proyectos que generan más de lo que cuestan» |
| ROE ≈ 14% (promedio) | [[roe]] | ⛔ **AUSENTE** |
| ROE > 30% (techo) | [[roe]] | ✅ presente — «puede ser debido a un apalancamiento excesivo» |
| Liquidez corriente > 1,5 | [[balance_general]] | ⛔ **AUSENTE** — «lo ideal es que sea» |
| Deuda/equity < 1,5 | [[balance_general]] | ⛔ **AUSENTE** — «lo ideal es que sea» |
| Solvencia | [[balance_general]] | — no da umbral |

> ⭐ **4 de 6 umbrales del piloto no tienen ninguna justificación.** Y los dos que sí la tienen la
> tienen **por mecanismo**, no por autoridad. **Antes de este arreglo esto era invisible**: el campo
> registraba «>15%» y quedaba formalmente correcto. **D-08 pasa de principio declarado a casilla que
> se rellena o se marca AUSENTE.** Es, de largo, lo más útil que ha salido del piloto 2.

**3d · Tensiones** hizo su trabajo: sostuvo las tres cifras del ROIC con su contexto **sin aplanarlas
ni elegir** (§1). Sin él, o se elegía una (RD-1) o se tiraban dos.

**3b · Clase** ahora distingue grados de anclaje, y eso resultó importante:
- **[[roic]]**: anclado fuerte — el deck relativiza en **una sola frase** («porque luego…»).
- **[[roe]]**: anclado **débil** — la cifra (14%) y la regla sectorial («Debe usarse para comparar
  empresa del mismo sector») están en **dos bullets contiguos que el experto nunca conecta**
  `[PDF 07, p.4]`. Lo marqué `[ABSOLUTO-RELATIVIZADO]` **diciendo que el anclaje es de dos frases
  sueltas, no de una**.
- Donde clasificar habría sido forzar, dejé `[HUECO]` (el umbral «> coste del capital» no es ninguna
  de las tres clases: es relativo a la propia empresa).

### 2.2 ARREGLO 5 (Demostración) — ✅ sostiene, con un matiz

**Novo Nordisk vs Moderna ya tiene casa** ([[roic]] §10). En v1 no cabía en ningún campo y hubo que
improvisar un bloque fuera de molde. **Ahora es un campo, marcado PEDAGOGÍA, y D-49 se respeta sin
tensión.**

**Y el PDF lo volvió verificable.** v1 dijo: *«las afirmaciones sobre la forma de las curvas son
deícticas y no verificables con el material actual»*. Ya no:

| La voz dice | La slide muestra `[PDF 07, p.7]` | |
|---|---|---|
| «el ROIC que está en **naranja**» (Moderna) `[09:07]` | *MRNA Return on Capital %* = serie naranja | ✅ |
| «en Novo Nordisk en **negro** está el ROIC» `[09:24]` | *NOVO B Return on Capital %* = serie oscura | ✅ |
| «y en **azul** está el ROE» `[09:24]` | *NOVO B Return On Equity %* = serie azul | ✅ |

*(Marca de agua de la slide: **TIKR.com** → concuerda con D-06.)*

⚠️ **Matiz:** la demostración es **cruzada** (ROIC↔ROE), así que con dos fichas hay que elegir dónde
vive. La puse en [[roic]] §10 y crucé desde [[roe]] §10. Funciona, pero **el campo asume una
demostración por ficha y aquí una demostración cubre dos**. Menor; lo reporto.

### 2.3 ARREGLO 3 (erratas) — ✅ sostiene, y ya produjo material real

**4 erratas en el vídeo 07**, todas voz↔PDF, todas `PENDIENTE DE REVISIÓN HUMANA`:

- **07-E1** — «empresas» (voz `[07:00]`) vs «**Industrias**» (título del gráfico, `[PDF 07, p.5]`).
  Unidad de análisis distinta. **Afecta a las tres cifras leídas sobre esa slide.**
- **07-E2** — «filtro para **detectar empresas de calidad**» (voz `[03:08]`) vs «filtro para **al
  menos descartar empresas mediocres**» (`[PDF 07, p.2]`). Cribar dentro vs cribar fuera: operaciones
  distintas, y el «al menos» del deck es mucho más modesto.
- **07-E3** ⭐ — **postura sobre el ROE.** El deck lo llama «una **métrica muy buena** para comparar
  empresas financieras» en una caja **simétrica** a la del ROIC `[PDF 07, p.2]`; la voz dice «**no me
  gusta el ROE**» `[05:43]` y construye toda una jerarquía. **El deck presenta dos métricas
  equivalentes; la voz una superior y otra sospechosa.** No es choque de dato: es de **postura**, y
  decide el rol del ROE en el método.
- **07-E4** — el gráfico de ROE está filtrado a «**ROE > 15%**» `[PDF 07, p.6]` y **la voz nunca
  enuncia ese umbral** (sí lo hace para el ROIC). Silencio sobre un criterio visible.

### 2.4 Contenido que AÚN no cabe

1. **El concepto paraguas — y ahora es peor, porque el deck le da página propia.** `[PDF 07, p.1]`
   es una slide entera: «¿QUÉ ENTENDEMOS POR EL CONCEPTO DE RENTABILIDAD?», con rentabilidad económica
   vs financiera y las cuatro métricas (ROIC/ROCE/ROE/ROA). **Ninguna de las dos fichas es dueña de
   esa página.** En v1 era un hueco conceptual; ahora es **una slide sin ficha**.
2. **La secuencia (D-51).** «a partir de aquí **todas las métricas que veamos deben responder a esta
   gran pregunta**: ¿está esta empresa creando valor con el capital que gestiona?» `[07, 10:20]`.
   Sigue sin campo y sin puntero a `protocolo_analisis.md`. Ver §5.1.
3. **ROA y ROCE descartados sin criterio** — `[HUECO]` confirmado en las dos capas: el deck los pone
   como iguales en p.1 y en p.2 ya solo hay dos, sin decir por qué.

### 2.5 Solape sin resolver (v1, sigue igual)

**ROE > 30% es umbral y bandera roja a la vez** `[07, 08:02]`. El molde sigue sin regla de desempate;
lo dupliqué otra vez, declarándolo. Causa de fondo: *Umbral(es)* **presupone un suelo de calidad**
(por encima = bueno) y el del ROE es un **techo de sospecha**. No lo he tocado (no era de los 5).

---

## 3. MOLDE 2 · Estado financiero

### 3.1 ARREGLO 5 — ✅ sostiene, y reveló algo sobre el curso

**Meta ya tiene casa** ([[balance_general]] §5). Pero al ponerlo en su campo se ve la proporción:

> **La «demostración» es ~4 de los 9:17 del vídeo 03.** No es una ilustración al final: **es el
> cuerpo de la lección**. Los tres ratios se calculan sobre el balance de Meta; la lectura del estado
> se hace sobre Meta; la ecuación se verifica sobre Meta.

Marcarlo PEDAGOGÍA es **correcto** (D-49, RD-1) y no transcribí ninguna cifra. Pero deja constancia
de que **~40% del vídeo 03 vive en un campo etiquetado «no es metodología»**. El campo no falla; lo
que revela es cómo enseña el curso. Lo reporto sin tocarlo.

### 3.2 ARREGLO 3 — ✅ y aquí el PDF dio la errata más limpia del piloto

- **03-E1** ⭐ — **la slide se contradice a sí misma.** «ACTIVOS NO CORRIENTES: PATRIMONIO (BIENES)
  QUE PERMANECE **MÁS DE 1 AÑO MENOS DE 12 MESES**» `[PDF 03, p.1]`. «Más de 1 año» y «menos de 12
  meses» no pueden ser ambos — y «menos de 1 año» es literalmente el criterio que **esa misma slide**
  da para los activos **CORRIENTES**. La voz dice solo «**más de un año**» `[03, 01:11]`.
  → Jerarquía aplicada: **el cuerpo lleva la voz**. No dictamino cuál es correcta (RD-1). Registrada.
- **03-E2** — *(en v2 registré aquí «la cobertura del deck». **Retirado en v3: no es una errata, es un
  hueco de material** — no hay dos polos que choquen. Movido a [[balance_general]] §7 y a
  `capturas_pendientes.md`. El ID se reutilizó para una errata `T3` real: la slide de activos omite
  inventario, maquinaria y goodwill. Ver `registro_organizacion.md` O-18.)*

### 3.3 Lo que el PDF cambió en las partidas

⭐ **Aporte solo-PDF que la voz nunca da:** la slide rotula las columnas **«APLICACIÓN DEL CAPITAL»**
(activos) y **«ORIGEN DEL CAPITAL»** (pasivos) `[PDF 03, p.1]`. **El experto no pronuncia esas
palabras en todo el vídeo**; dice «cómo financiamos la izquierda con la derecha». El encuadre
canónico existe **solo en la capa visual**. También añade los «Derechos de leasings» como activo
`[PDF 03, p.3]`, que la voz nunca menciona.

⭐ **Y un patrón que solo se ve cruzando capas:** **el deck da los NOMBRES, la voz da la VIGILANCIA.**
El deck es un diccionario de partidas y **no señala ni una sola cosa que mirar**. Las cinco banderas
rojas, los tres ratios, el «no todo activo es productivo», el goodwill desproporcionado: **todo
solo-verbal**. Es la asimetría **inversa** a la del vídeo 07, donde el deck sí aportaba criterio (la
relativización sectorial, el «pero esto por sí solo no es suficiente»).

### 3.4 Contenido que AÚN no cabe (sin cambios respecto a v1)

1. **Naturaleza temporal (stock vs flujo).** «el balance presenta una **fotografía de la empresa en
   un momento específico**» `[03, 00:41]` — solo-verbal, y **el campo definitorio de un estado
   financiero**. El molde viejo lo tenía (campo 6, con aviso de mezclas stock/flujo y look-ahead).
   Lo metí a la fuerza en *Estructura*. **No estaba en los 5 arreglos; no lo he añadido.**
2. **«Qué NO responde este estado».** «aquí **no se habla de rentabilidad**, sino de la estructura»
   `[03, 00:16]` — el experto **abre** delimitando. Sin campo.
3. **Las «señales clave»** — 45 s de *preguntas de lectura* `[03, 06:09–06:54]` que no son partidas ni
   ratios. Improvisé sección.
4. **El orden de lectura en cinco pasos** `[03, 06:54–07:37]` → D-51. Ver §5.1.
5. **La afirmación sobre el esfuerzo**: «son **cuatro cosas** del balance» `[03, 06:09]`, «de un simple
   vistazo… es una página, son cuatro datos» `[03, 08:35]`. Repetido tres veces: es una tesis sobre
   **cuán hondo hay que ir**. Sin campo — y no es trivial: un copiloto que no lo sepa sobreanalizará
   donde el experto echa un vistazo.

### 3.5 Los ratios siguen apuntando a fichas que no existen

`[[ratio_liquidez_corriente]]`, `[[ratio_deuda_equity]]`, `[[ratio_solvencia]]`: **ninguna existe.**
Sin cambios respecto a v1. Es **D-54 con otra cara** (allí protocolo↔fichas; aquí estado↔ratios): una
ficha de MOLDE 2 no se puede cerrar hasta que existan sus fichas de MOLDE 1.

**Y el corolario se confirma: las fichas NO son 1:1 con los vídeos.** El umbral «liquidez > 1,5» se
dice en el vídeo 03 y pertenece a la ficha del ratio.

---

## 4. MOLDE 3 · Cualitativo

**Era el molde que no aguantaba. Ahora aguanta.** Y es donde el PDF ha sido más decisivo.

### 4.1 ARREGLO 1 · «Señales de erosión» — ✅ **la ausencia ahora SE VE**

**Campo `AUSENTE EN LA FUENTE`, en las dos capas**, escrito en grande en [[moat]] §5.

Y el campo permitió una **precisión** que sin él era imposible: MySpace (§4.2) **describe un
desenlace, no una señal**. «Que no se usaba y acabó en el olvido» dice que el moat desapareció; **no
dice qué habría que haber mirado para verlo venir**. Sin el campo, esa distinción —entre *sé que pasó*
y *sé detectarlo*— no tiene dónde formularse.

> **Consecuencia registrada:** «sostenible» es constitutivo de la definición del moat
> `[10, 00:26]` y **la fuente no da ni un solo modo de comprobar la sostenibilidad**.

### 4.2 ARREGLO 1 · «Contraejemplos» — ⭐⭐ **el campo corrigió al piloto v1**

**v1 dijo: «9 de 9 ejemplares ganadores. Contraejemplos: cero.»**
**v2, con el deck: no es cero. Es uno — y estaba en la slide.**

> «**¿Qué pasó con MySpace? Que no se usaba y acabó en el olvido.**» `[PDF 10, p.5]`

Dentro del cuadro de EFECTO RED, como contraste inmediato a WhatsApp/Instagram: la misma caja muestra
una red que murió y dos que crecieron.

**Pero el campo también mide lo que el contraejemplo NO hace:**

| | |
|---|---|
| ✅ Es la **única evidencia en toda la fuente** de que un moat puede desaparecer | |
| ⛔ **El experto NO lo verbaliza.** `[VÍDEO 10, 05:17–05:31]` habla de Meta/WhatsApp/Instagram y **no menciona MySpace** | |
| ⛔ No explica por qué pasó, ni lo vuelve señal de erosión, ni advertencia de falso positivo | |
| ⛔ Cubre **una** categoría de siete | |

> **Proporción real: ≈11 ganadores contra 1 perdedor**, y el perdedor vive en **dos líneas de una
> slide que el experto no lee en voz alta**.
>
> ⭐ **D-21 (sesgo de supervivencia) queda CONFIRMADO y, por primera vez, MEDIDO** en vez de supuesto.
> **El campo restaurado hizo las dos cosas: corregir el error de v1 y cuantificar el sesgo.** Es el
> mejor argumento del piloto a favor de ARREGLO 1.

### 4.3 ARREGLO 1 · «Cadena causal» — ✅ y el deck la trae DIBUJADA

**El campo era más necesario de lo que v1 supuso: el deck codifica las cadenas con flechas.**
`[PDF 10, p.3–p.5]` monta cada categoría como **`[ejemplar] → [categoría] → [efecto económico]`**:

| Ejemplar | Categoría | → Efecto (rótulo literal) |
|---|---|---|
| ASML | MONOPOLIOS | «MONOPOLIO SE CARACTERIZA POR LA CAPACIDAD DE FIJACIÓN DE PRECIOS» |
| Ferrari | SECTOR LUJO: EXCLUSIVIDAD | «LA DIFERENCIACIÓN PERMITE CAPACIDAD DE FIJACIÓN DE PRECIOS» |
| Mercadona, Zara | RETAILERS: BAJOS COSTES | «EFICIENCIA EN COSTES. BAJOS PRECIOS PARA AUMENTAR VOLUMEN DE VENTAS» |
| Salesforce | TECNNOLOGÍA: SWITCHING COSTS | «LOS SWITCHING COSTS IMPLICAN FIDELIZAR CLIENTES» |
| Meta | EFECTO RED | «INCREMENTO CRECIMIENTO DE Nº USUARIOS. AUMENTO DE VENTAS Y BENEFICIOS» |
| Coca-Cola, Apple | PODER DE MARCA | «1ª OPCIÓN DE COMPRA Y FIDELIZACIÓN DE CLIENTES. AUMENTA VENTAS» |

### 4.4 ARREGLO 2 · Dirección — ✅ **el PDF lo vindica**, con un matiz que debes decidir

> ⭐ **Las seis flechas del deck van en el mismo sentido: `moat → efecto`. Ninguna va al revés.**
> **La capa visual solo codifica la causa.** ARREGLO 2 no era una precaución teórica: era la
> estructura de la fuente.

**El matiz — y es una pregunta para ti, no algo que yo deba resolver:**

ARREGLO 2 dice: *«NO registres la recíproca ("márgenes altos ⇒ hay moat"): es la inversa y no se
sigue.»* **Pero la recíproca está en la fuente, dicha por el experto:**

> «se recomienda siempre estudiar métricas como el margen, el EBIT, el ROIC o la evolución del free
> cash flow, **para identificar si tiene algún moat**» `[VÍDEO 10, 03:25–03:40]`
>
> Y la checklist: «**detectar un moat** […] requiere mirar: el histórico de rentabilidad y ROIC, la
> estabilidad en el margen bruto y EBIT…» `[VÍDEO 10, 03:40–04:06]`

**Cómo lo he resuelto** (y quiero que lo confirmes o lo corrijas):
- *Cadena causal* (§3) = **solo sus flechas causales**. No fabriqué ninguna recíproca.
- *Señales de detección* (§4) = **sus propias frases de detección, citadas**, marcadas como la
  dirección inversa y como **solo-verbales** (el deck no tiene ninguna página de detección).
- Y registré el hecho: **la fuente contiene las dos direcciones y el experto nunca advierte de que la
  segunda es más débil.**

He leído ARREGLO 2 como **«no fabriques la recíproca»**, no como **«no registres la recíproca que el
experto sí dice»**. Si querías lo segundo, dímelo: implicaría **tirar §4 entero**, que es el núcleo
declarado del molde.

### 4.5 El PDF cerró dos `[HUECO]` de v1

- ⭐ **Ferrari SÍ cabe.** v1: *«el ejemplar más desarrollado del vídeo no cabe en su propia
  clasificación»*. **Falso, con el deck:** existe la categoría **«SECTOR LUJO: EXCLUSIVIDAD»**, con
  el **logo de Ferrari** al lado y su propia flecha `[PDF 10, p.3]`. La lista verbal de seis se
  quedaba corta; la del deck no.
- ⭐ **La exhaustividad estaba declarada.** v1 lo dejó abierto («o la lista no es exhaustiva y el
  experto no lo dice»). **Lo dice**: «¿Qué ventajas competitivas puede tener una empresa? **Algunas
  pueden ser éstas…**» `[PDF 10, p.2]`.

### 4.6 El PDF resolvió 10-E1 — y me obligó a **retirar** una afirmación de v1

- ⭐ **10-E1 confirmada.** v1: *«"activos tangibles" — errata aparente, no verificable sin captura»*.
  **La slide dice «CON ACTIVOS INTANGIBLES»** `[PDF 10, p.2]`. Voz y rótulo son opuestos, y la voz
  está leyendo esa caja (sus tres sub-ítems van en el mismo orden). **Jerarquía aplicada: el cuerpo
  lleva la voz («tangibles»); la errata registra el choque. No dictamino cuál es correcta** (RD-1) —
  aunque sí registro un dato interno a la fuente: el propio experto los llama «intangibles» en el
  vídeo 03 `[03, 04:20]`.

- ⚠️ **Y RETIRO una afirmación de v1.** v1 dijo: *«el experto divide los moats en dos familias
  (aumentan ingresos / reducen costes)»*. **Eso era una lectura mía apoyada en puntuación que el
  `.srt` no tiene.** En crudo: «pueden dividirse en aquellas que aumentan los ingresos o la propuesta
  de valor **también** reducen los costes o mejoran la eficiencia» `[10, 01:10]`. Sin comas admite
  **dos familias** o **una lista de efectos**, y no son equivalentes. La primera mitad **reproduce la
  cabecera de la slide**; lo que añade después no tiene equivalente visual. **He dejado el eje
  superior en `[HUECO]` y he registrado 10-E2 con las dos lecturas.**
  → *Es un aviso sobre el método de trabajo: en una transcripción sin puntuar, puntuar es interpretar.*

### 4.7 Contenido que AÚN no cabe

1. **Herramientas externas.** «análisis **Porter**», «**economic moat de Morningstar**» `[10, 04:06]`.
   Sin campo; lo metí dentro de *Señales de detección* con marca.
2. **La normativa de estrategia.** «buscar empresas con ventajas competitivas sostenibles **es clave
   para una estrategia de inversión fundamentada y exitosa**» `[10, 06:04]`. No es definición, ni
   señal, ni cadena causal, ni aplicabilidad.

> ✅ **Lo que v1 llamaba «"Por qué importa el moat" — un bloque entero sin destino» está en gran parte
> RESUELTO por ARREGLO 1.** *Cadena causal* absorbe legítimamente `moat → flujos proyectables → menor
> riesgo, mayor visibilidad` y `moat → resiliencia`, porque **son flechas del experto**. Lo que queda
> huérfano es solo el residuo normativo del punto 2.

---

## 5. Problemas que REPORTO y NO he tocado

> Fuera de los 5 arreglos. **No he ajustado nada de esto.**

### 5.1 ✅ **PROBLEMA 6 — RESUELTO en v3** (el bloque de erratas veía UNO de los CUATRO tipos)

> **Estado v3: CERRADO.** El bloque se amplió a los cuatro tipos (`moldes.md`) y las erratas que no
> tenían sitio **ya están colocadas**: **17 en total, de las cuales 10 (T2/T3/T4) se habrían perdido**.
> Índice y recuento en `erratas_piloto.md`. El diagnóstico de abajo se conserva como registro.

**Este fue el hallazgo estructural del piloto 2.**

`## Errata de la fuente`, tal como lo definiste, registra **discrepancias voz↔PDF**. El piloto ha
encontrado **cuatro** tipos de defecto de fuente, y el bloque solo coge el primero:

| Tipo | Ejemplo del piloto | ¿Cabe? |
|---|---|---|
| **1. voz ↔ PDF** | 07-E1/E2/E3/E4 · 03-E1/E2 · 10-E1/E2/E3 — **9 erratas registradas** | ✅ **Sí** |
| **2. voz ↔ voz** | ROIC: «promedio de mercado» = **13-15%** `[03:49]` y **8-10%** `[07:28]` | ⛔ **No** |
| **3. PDF ↔ PDF** | ROE: el deck define rentabilidad financiera y la reformula con la fórmula de la **económica** `[PDF 07, p.1]` · `[PDF 03, p.1]` incluye «EL INVENTARIO» y `[PDF 03, p.3]` lo omite (igual con maquinaria y goodwill) · `[PDF 10, p.2]` no incluye «SECTOR LUJO», que p.3 desarrolla; e incluye «PATENTES/LICENCIAS», que no se desarrolla | ⛔ **No** |
| **4. Ambigüedad de la transcripción** | 10-E2: sin puntuación, «dos familias» vs «lista de efectos» no es decidible | ⛔ **A medias** |

**Consecuencias concretas:**
- **La contradicción del ROIC no llegará a `erratas.md`.** Vive solo en [[roic]] §3d, gracias a
  ARREGLO 4. Sin ese arreglo se habría perdido del todo.
- **Las tres inconsistencias internas del deck no llegarán a `erratas.md`.** Las he anotado en las
  fichas, fuera de bloque.
- **Por tanto la «tasa de error de la fuente» que calcules será un SUELO, no una medida.** Contará 9
  de al menos 14 defectos que este piloto ha visto. Y precisamente el más grave —la contradicción del
  promedio del ROIC, que vacía de sentido su único umbral operativo— **es de los que no cuenta**.

**Lo reporto y paro.** Es tu decisión si el bloque debe ampliar su alcance.

### 5.2 ⛔ Los campos procedimentales de D-51 siguen sin existir en ningún molde

**Rol en el análisis** · **Momento de evaluación** · **Criterio de parada** (D-51) no están en 1, 2 ni
3. Y el material de secuencia sigue sin ruta:

- `[07, 10:20]` «a partir de aquí **todas las métricas que veamos deben responder a esta gran
  pregunta**: ¿está esta empresa creando valor con el capital que gestiona?»
- `[03, 06:54–07:37]` el orden de lectura del balance — ⚠️ **v2 lo llamó «cinco pasos» y «la única
  secuencia real de los tres vídeos». RETIRADO en v3: es UNA transición ordenada** («y después»); el
  resto es enumeración («también», «y si»). Ver `capa_decision.md` §1 y `registro_organizacion.md` O-17.
- `[03, 09:10]` «la siguiente clase veremos el tercer estado»
- `[03, 00:08]` «el **segundo** estado clave»

D-51 manda esas frases **verbatim** a `protocolo_analisis.md`. **Ningún campo de ningún molde las
recoge ni apunta allí.** Un escritor que ingiera el vídeo 03 con estos moldes **no tiene ningún motivo
estructural para acordarse de `protocolo_analisis.md`**. Se perderán en silencio. Todo ese material
queda marcado en las fichas para que se pueda rescatar.

### 5.3 ⚠️ El modelo de fuente se cumple **de forma desigual** — y el vídeo 03 **sigue necesitando captura**

**«PDF = capa visual completa» vale para el 07. No vale para el 03 ni del todo para el 10.**

| Vídeo | Duración | Págs. | Cobertura del deck | Qué queda fuera |
|---|---|---|---|---|
| **07** | 11:31 | 7 | ✅ **casi total** | Solo la fórmula **dibujada a mano** |
| **10** | 6:28 | 5 | ⚠️ **≈4 min** | `02:17–04:16`: **el núcleo de detección** y la cadena causal verbal |
| **03** | 9:17 | 4 | ⛔ **≈3,5 min** | `02:45–03:44` y `05:09–09:17`: **el caso Meta y LOS TRES RATIOS CON UMBRAL** |

**El patrón:** el deck trae **definiciones, taxonomía y ejemplos**. Cuando el experto pasa a **lo
operativo** —calcular ratios sobre un balance real, enumerar señales— **se sale del deck a una
pantalla que no tenemos**.

⚠️ **Consecuencia dura: en el vídeo 03, el contenido más operativo del módulo (liquidez > 1,5;
deuda/equity < 1,5; solvencia) se enuncia sobre el balance de Meta, que NO está en el PDF.**
**D-48 sigue vigente para el vídeo 03**: hace falta captura de esa pantalla. Para el 07 ya no.

### 5.4 ⚠️ Hay una **tercera** capa visual: la anotación en directo

«la fórmula del ROIC **que la voy a dibujar**» `[07, 04:18]`. **El experto escribe encima de la
slide.** `[PDF 07, p.3]` no trae la fórmula. Así que «transcripción + PDF = las dos mitades del mismo
momento» **no es exacto**: hay una tercera capa —lo que dibuja— que solo existe en el vídeo.

Aquí es benigno (dicta la fórmula en voz alta mientras la dibuja, así que la voz la salva). **Pero si
en otro módulo dibuja algo sin verbalizarlo, se pierde entero y ninguna capa lo detectará.**

### 5.5 ✅ Incidental: **D-19 queda explicado** (no lo he tocado — está `PENDIENTE DE VERIFICACIÓN`)

Extraje la numeración de sección de los 12 decks:

| Vídeo | Sección del deck | | Vídeo | Sección del deck |
|---|---|---|---|---|
| 01 | *(sin numerar)* | | 07 | **5.** LA RENTABILIDAD |
| 02 | **2.** LOS 3 ESTADOS FINANCIEROS | | 08 | **6.** EL CAPEX |
| 03 | **2.** EL BALANCE | | 09 | **7.** EL FREE CASH FLOW |
| 04 | **3.** LOS ESTADOS DE FLUJOS DE CAJA | | 10 | **8.** EL MOAT |
| 05 | **3.** EL INFORME FINACIERO 10Q | | 11 | **9.** EL EQUIPO DIRECTIVO |
| 06 | **4.** LA DEUDA Y LA CAJA | | 12 | **10.** MÚLTIPLOS DE VALORACIÓN |

**El deck es UN solo documento con 10 secciones numeradas, repartido en 12 vídeos.** Los vídeos
**02+03 comparten la sección 2**; **04+05 comparten la 3**. Por eso el desfase no es constante
(03→2, 07→5, 10→8).

> **D-19 hipotetizaba que el desfase «sugiere edición anterior del curso».** La explicación es más
> simple y benigna: **el corte en vídeos no coincide con el corte en secciones.** No es evidencia de
> PDFs desactualizados. **Refuerza el modelo de fuente nuevo** (el PDF no es un borrador viejo).
>
> Evidencia adicional en la misma dirección: `[PDF 07, p.7]` trae series de precio **con datos hasta
> ~mediados de 2025**. El deck está al día del vídeo.

**No he tocado `decisiones.md`.** Lo dejo aquí para que decidas.

- *Aparte, gratis y para una ingesta futura:* el deck del vídeo 05 se titula «EL INFORME **FINACIERO
  10Q**» (con la errata «FINACIERO») mientras el slug del proyecto es `05_informe_10k`. **10Q ≠ 10K.**
  Fuera del alcance del piloto; no he actuado.

### 5.6 ⚠️ Menores, sin tocar

- **Frontmatter:** los moldes siguen sin declararlo. Mantengo el mínimo de v1 (`concepto`, `modulo`,
  `molde`, `estado`, `fuentes`, `enlaces`) y lo declaro **invención mía**.
- **El campo «Fuente»** sigue siendo, de hecho, un bloque de **estado de la evidencia** (cobertura del
  deck, capturas, estatus canónico del `.srt`) más que una cita. Útil, pero no es lo que su nombre
  dice.
- **La advertencia del `.srt` del vídeo 10** sigue en pie: 0 comas en el texto (14: 1 coma; 16: 3
  comas sobre 790 subtítulos). **10-E2 depende directamente de eso.** Y **D-56 se resolvió con el
  vídeo 16.** No he actuado.

---

## 6. Los hallazgos que decidirían mi voto

1. ⭐⭐ **Los campos que registran ausencias se pagaron solos en el primer intento — y uno corrigió al
   propio piloto.** *Contraejemplos* no salió vacío: salió **MySpace** `[PDF 10, p.5]`, que v1 no
   podía ver. La cuenta real es **≈11 ganadores contra 1 perdedor**, y el perdedor está en **dos
   líneas de una slide que el experto no lee en voz alta**. **D-21 pasa de sospecha a medida.** Y
   *Señales de erosión* quedó `AUSENTE` con una precisión que sin el campo no existiría: MySpace
   demuestra que un moat **muere**, y no da **ni una señal** para verlo venir — siendo «sostenible»
   parte de la definición del concepto.

2. ⭐⭐ **El sub-campo 3c (justificación) es el mayor rendimiento por línea de todo el piloto: 4 de 6
   umbrales no tienen ninguna.** ROIC >15%, ROE 14%, liquidez >1,5, deuda/equity <1,5 → **AUSENTE**.
   Solo ROE >30% y «ROIC > coste del capital» dan mecanismo. **Antes era invisible**: el campo
   registraba la cifra y quedaba formalmente correcto. **D-08 deja de ser un principio declarado y
   pasa a ser una casilla que se rellena o se marca AUSENTE.**

3. ⛔ **PROBLEMA 6: el bloque de erratas solo ve uno de los cuatro tipos de error de la fuente.**
   Cubre voz↔PDF (9 erratas registradas, material real para `erratas.md`). **No cubre voz↔voz, ni
   PDF↔PDF, ni la ambigüedad de una transcripción sin puntuar.** Consecuencia: **la tasa de error que
   calcules será un suelo, no una medida** — contará 9 de al menos 14 defectos vistos. Y el más grave
   de todos, **la contradicción del promedio del ROIC (13-15% vs 8-10%), es de los que no cuenta**:
   sobrevive solo porque ARREGLO 4 le dio un sitio en §3d. **Reportado, no arreglado.**

---

---

# v3 · Pasada preventiva bajo el método nuevo

> Objetivo: cazar **errores tontos** que el cambio de modo pueda provocar. Una pasada, sin
> perfeccionismo. Decisiones de organización en `registro_organizacion.md`.

## V3.1 · Los errores tontos que salieron — **tres, y los tres son míos**

**No, no salió «nada tonto». Salieron tres, y son instructivos porque los tres son del mismo tipo:
convertir en estructura algo que la fuente no tiene.**

### ⚠️ TONTO 1 · Numeré una enumeración y la llamé secuencia

`piloto_friccion.md` v2: *«el orden de lectura del balance **en cinco pasos** […] **la única secuencia
real de los tres vídeos**»*. **Falso.**

En `[VÍDEO 03, 06:54–07:37]` hay **un solo marcador de orden**: «**y después** revisar la parte de la
deuda». Todo lo demás llega con «**también** es importante ver el equity», «**y si** la deuda de largo
plazo…». **Una transición ordenada, no cinco pasos.**

> **Por qué es grave y no cosmético.** **Numerar es ordenar.** Al escribirlo como lista 1..5 le di al
> curso una secuencia que no enuncia — exactamente lo que **la regla de oro de D-51** prohíbe («NO se
> deduce la secuencia»). Y lo hice **mientras escribía el reporte que denunciaba que el material
> procedimental no tenía ruta**: iba a enrutar hacia `capa_decision.md` una secuencia inventada.
> **El molde correcto no protege de esto; solo lo hace la disciplina de citar en crudo.**
> → Corregido en `capa_decision.md` §1, que ahora separa **lo ordenado** de **lo enumerado**.

### ⚠️ TONTO 2 · Metí en el bloque de erratas algo que no es una errata

`03-E2` en v2 registraba **«la cobertura del deck»** — que el PDF del 03 no tiene páginas para los
ratios ni para Meta. **Eso no es una errata: no hay dos polos que choquen.** Es un **hueco de
material**, y del nuestro, no de la fuente.

> **Por qué importa.** El bloque de erratas alimenta **la tasa de error de la fuente**. Meter ahí
> ausencias de material **infla precisamente el número que existe para medir bien**. Con 4 tipos el
> riesgo se multiplica: el bloque se vuelve un cajón.
> → Movido a [[balance_general]] §7 + `capturas_pendientes.md`. Y añadí al molde una sección
> **«Qué NO es una errata»** (`registro_organizacion.md` O-10) para que no vuelva a pasar al escalar.

### ⚠️ TONTO 3 · Una entrada de errata mezclaba dos defectos distintos

`10-E2` en v2 tenía un «**choque doble**»: la ambigüedad de la transcripción **y** la cabecera de la
slide que no cubre sus contenidos. Son **dos defectos, de dos tipos, con dos resoluciones distintas**
(uno se cierra verificando el `.srt`; el otro, decidiendo sobre el deck). Empaquetados juntos,
**ninguno de los dos es contable**.
> → Re-partidos: `10-E2` (`T4`) y `10-E5` (`T3`).

**El patrón de los tres:** en v2 el molde no tenía casilla para estas cosas, así que **improvisé** — y
al improvisar, ordené de más. **Los tres errores nacieron de escribir fuera de molde.** Es un
argumento a favor de tener las casillas, y un aviso para el escalado: *donde falte casilla, el
escritor inventará estructura sin darse cuenta.*

## V3.2 · Erratas colocadas — 17, de las que **10 no tenían sitio antes**

| Tipo | Nº | Nuevas en v3 |
|---|---|---|
| `T1` voz↔PDF | 7 | — (ya existían) |
| `T2` voz↔voz | **2** | **07-E5** ⭐ (13-15% vs 8-10%) · **07-E6** |
| `T3` PDF↔PDF | **4** | **07-E7** · **03-E2** · **10-E4** · **10-E5** |
| `T4` transcripción | **4** | **10-E2** ⭐ · **10-E6** · **07-E8** · **07-E9** |

Índice, gravedad y recuento: **`erratas_piloto.md`**.

⭐ **La que más importaba ya tiene casa: `07-E5`.** La contradicción del promedio del ROIC —que decide
el sentido del único umbral operativo del vídeo— vivía solo en un sub-campo. Ahora es una errata
contable, con estado y con la nota de que **`T2` no tiene jerarquía que la resuelva** (los dos polos
son voz; voz>PDF no aplica).

## V3.3 · Un hallazgo nuevo sobre la tasa de error

**La cuenta no mide la fuente: mide la fuente Y el método.** Misma fuente, tres instrumentos:

| Pasada | Método | Erratas |
|---|---|---|
| v1 | solo transcripción | **0** |
| v2 | + PDF, 1 tipo | **9** |
| v3 | + 4 tipos | **17** |

Cada mejora del instrumento casi dobló la cuenta. Consecuencias en `erratas_piloto.md` §*Cómo NO leer
estos números*. **Recomendación que no ejecuto:** congelar el método **antes** de escalar y rehacer
07/03/10 con él, o los 19 no serán comparables (`registro_organizacion.md` H-03).

## V3.4 · Lo que sigue sin campo, después de todo

**Sin cambios respecto a v2** (no era el encargo tocarlo, y no lo he tocado):

- **Los campos procedimentales de D-51** (*Rol* · *Momento* · *Criterio de parada*) siguen sin existir
  en los tres moldes. Ahora el material **tiene destino** (`capa_decision.md`), pero **ningún campo
  apunta allí**: quien ingiera el vídeo 04 no tendrá motivo estructural para acordarse.
  → `capa_decision.md` §3 lo enseña en vivo: la regla del ROIC no dice si es eliminatoria o
  condicionante, y **ese `[HUECO]` no cabe en ninguna ficha**.
- **Molde 2 sin *naturaleza temporal*** (stock vs flujo) ni **«qué NO responde este estado»**.
- **Molde 3 sin campo para herramientas externas** (Porter, Morningstar).
- **«Umbral» y «Bandera roja» solapan** (ROE > 30%), sin regla de desempate.

---

## 7. Qué NO he hecho

- ❌ No he modificado `CLAUDE.md`, `decisiones.md`, `log.md`, `index.md`, `erratas.md`,
  `protocolo_analisis.md`, `inventario_atomico.md`, `fuentes.md` ni ninguna ficha de `curso/`.
- ❌ No he promovido nada a `curso/`. Todo en `wiki/piloto/`.
- ❌ No he commiteado.
- ❌ No he ajustado ningún molde más allá de los 5 arreglos. El 6º problema va reportado, no tocado.
- ❌ **No he resuelto ninguna discrepancia por criterio propio.** Las 9 erratas quedan
  `PENDIENTE DE REVISIÓN HUMANA`. En particular **no he dictaminado** si «activos tangibles» o
  «INTANGIBLES», ni cuál de los promedios del ROIC es el bueno, ni si el activo no corriente es «más
  de 1 año» o lo que dice la slide.
- ❌ No he rellenado huecos, ni completado la fórmula del ROE (ausente en **las dos** capas).
- ❌ No he transcrito ninguna cifra de empresa (RD-1 + D-49): ni las de Meta `[03, 05:15]`, ni las
  barras de ROE/ROIC de Novo Nordisk/Moderna `[PDF 07, p.7]`.
- ⚠️ **He retirado una afirmación de v1** (las «dos familias» del moat, §4.6) por apoyarse en
  puntuación que la fuente no tiene.
- ⚠️ **Decisiones mías, declaradas:** crear `moldes.md` (los moldes no existían como archivo y los 5
  arreglos tenían que ir a alguna parte); mantener el frontmatter mínimo; y leer ARREGLO 2 como «no
  fabriques la recíproca» y no como «no registres la que el experto dice» (§4.4 — **confírmalo**).
