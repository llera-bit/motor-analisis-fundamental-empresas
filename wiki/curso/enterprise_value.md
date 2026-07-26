---
concepto: Enterprise Value (EV)
modulo: 06
molde: 1
estado: completo
fuentes: [VIDEO-06, PDF-06]
enlaces: [deuda_neta, deuda_financiera, ev_ebitda, ev_fcf]
---

# Enterprise Value (EV)

> ✅ **Tres erratas aplicadas** (`06-E1`, `06-E3`, `06-E4`), **todas dictaminadas en sesión
> anterior — no se reelevan.** El cuerpo de esta ficha usa siempre la versión correcta: gana la
> voz en la fórmula y en el rótulo AMD/Intel; las cajas de decisión del deck ya eran correctas.
> Detalle completo en el bloque de erratas, más abajo.

---

## 1 · Definición y fórmula

> «cuando calculamos el valor real de una empresa, usaremos el enterprise value, y la fórmula de
> enterprise value es el **market cap más la deuda neta**» `[VÍDEO 06, 06:21–06:29]`

`MARKET CAP = Nº DE ACCIONES x PRECIO` `[PDF 06, p.5]`

> «el enterprise value... es el valor total de la empresa, teniendo en cuenta su deuda neta»
> `[VÍDEO 06, 07:13–07:19]` · «representa el coste total de adquirir una empresa, por tanto es
> **capital más deuda**» `[VÍDEO 06, 07:31–07:37]` · `[PDF 06, p.6]`: «El valor del ENTERPRISE
> VALUE te indica cuánto costaría tomar el control total de la empresa, no sólo adquiriendo todas
> las acciones disponibles (el Equity o Patrimonio Neto) a valor de mercado, sino también
> asumiendo todas sus deudas»

**Analogía del experto** (genérica, no es dato de empresa — se queda en la ficha, D-68):

> «imagina que compras una empresa como si compraras una casa, y esta casa o esta empresa tiene un
> valor de 1 millón, pero descubres cuando entras que en su interior tiene una caja fuerte con
> dinero dentro, y en este caso tiene 200 mil euros en cash. Pues la realidad es que has adquirido
> una deuda financiera... por una hipoteca de 1 millón, pero tu deuda real, tu deuda neta, en
> realidad es de 800 mil» `[VÍDEO 06, 06:33–07:00]` · «esto como si compras una casa y la casa
> tiene deudas, también compras las deudas, o si compras un coche tiene multas por pagar» `[VÍDEO
> 06, 08:10–08:18]`

---

## 2 · Qué mide / interpretación direccional

> «una empresa con mucha caja, tiene un EV más bajo, lo que puede hacerla más atractiva en
> múltiplos de valoración» `[VÍDEO 06, 06:29–06:33]`

**Cajas de decisión** `[PDF 06, p.5]` (✅ ya correctas — ver errata `06-E3`):

| Condición | Lectura |
|---|---|
| **MARKET CAP < EV** | La empresa **tiene deuda** (deuda neta positiva) |
| **MARKET CAP > EV** | La empresa **no tiene deuda** (caja neta) |

---

## 3 · Umbral(es)

`AUSENTE EN LA FUENTE` — el EV es una cifra absoluta de valoración (no un ratio con banda ideal
propia). El umbral relevante del bloque es el de Net Debt/EBITDA, propiedad de [[deuda_neta]]
campo 3.

---

## 4 · Aplicabilidad: dónde SÍ

> «cuando vayamos a valorar si una empresa está cara o barata en términos fundamentales, te puedes
> apoyar en esta valoración de múltiples múltiplos que emplean justamente el EV en su cálculo
> (EV/FCF, EV/EBITDA, EV/EBIT)» `[VÍDEO 06, 08:18–08:34]` · `[PDF 06, p.6]` — cita ya registrada en
> [[capa_decision]] §2.4 (fase de la valoración), no se duplica aquí

> «permite comparaciones entre empresas con estructuras de capital distintas» `[VÍDEO 06,
> 07:42–07:49]`

## 5 · Aplicabilidad: dónde NO

`AUSENTE EN LA FUENTE`.

---

## 6 · Advertencia de uso aislado / cuándo engaña

`AUSENTE EN LA FUENTE` — el material no describe cómo se manipula el EV desde la empresa.

---

## 7 · Punto ciego

`AUSENTE EN LA FUENTE`.

---

## 8 · Lectura relacional

Input directo: [[deuda_neta]] (`EV = Market Cap + Deuda neta`), que a su vez se deriva de
[[deuda_financiera]] menos la caja. Se usa como numerador de [[ev_ebitda|EV/EBITDA]],
[[ev_fcf|EV/FCF]], EV/EBIT (este último sin ficha propia en el corpus) — **molde 4, bloque de
múltiplos**. 🆕 *(Enlace cerrado en el lint del corpus completo, 2026-07-19: cuando se escribió esta
ficha —vídeo 06— los múltiplos aún no estaban ingeridos y quedó como forward pointer sin resolver.)*

---

## 9 · Recomendación comparativa

> «el EV, el enterprise value, es mucho más realista que no solo mirar la capitalización
> bursátil» `[VÍDEO 06, 07:19–07:24]` — EV preferido sobre market cap en solitario.

---

## 10 · Consistencia temporal

`AUSENTE EN LA FUENTE`.

## 11 · Banderas rojas

`AUSENTE EN LA FUENTE` — específico del EV (las banderas de deuda a corto plazo son propiedad de
[[deuda_financiera]]).

---

## 12 · Demostración del experto

→ [[ejemplo_06_amd_intel]] · **PEDAGOGÍA**

El experto compara AMD e Intel — market cap vs. EV, con datos reales — para mostrar cómo la
posición de caja/deuda neta cambia la valoración por EV frente a mirar solo el market cap: «a
igualdad de EBITDA, AMD puede parecer más barata por tener menos EV» `[VÍDEO 06, 09:04–09:14]`.

---

## 13 · Equivalencia técnica 🆕

> ⚠️ **APORTACIÓN EXTERNA — `[COMPLETADO-EST]`, pilar (a).** Nada de este bloque es palabra del
> experto. Se registra para que el cerebro empareje su definición con el dato real (D-72). Borrar
> este bloque debe dejar la ficha íntegra.

| | |
|---|---|
| **Lo que define el experto** | «EV = Market Cap + Deuda neta» — campo 1 |
| **Término estándar equivalente** | **EV** · *Enterprise Value*. Ya es el término estándar — el experto lo usa tal cual |
| ⭐ **El matiz — qué más se suma en algunas fuentes** | **Algunos screeners añaden participaciones minoritarias (*minority interest*) y acciones preferentes al EV**, además de Market Cap + Deuda neta. El experto no las menciona (campo 1 y [[deuda_neta]] no las tratan). Para la mayoría de empresas del corpus (sin estructura accionarial compleja) la diferencia es nula o marginal — pero **si una fuente da un EV distinto al calculado a mano, comprobar si incluye estas partidas antes de asumir un error** |
| **Dónde llega el dato** | Los screeners publican **EV** ya calculado como campo propio, y también por separado **Market Cap** y **Net Debt** para reconstruirlo |

---

## Errata de la fuente

| # | Tipo | Qué choca | Estado |
|---|---|---|---|
| **06-E1** | T1 | El deck imprime `ENTERPRISE VALUE (EV) = MARKET CAP – NET DEBT` `[PDF 06, p.5]` — signo invertido. La voz dice «market cap **más** la deuda neta» `[VÍDEO 06, 06:21]` | ✅ **DICTAMINADO** — gana la voz: `EV = Market Cap + Deuda neta`. *Ya dictaminado en sesión anterior; no se reeleva* |
| **06-E3** | T1/T3 | Las dos cajas de decisión de `[PDF 06, p.5]` («Si MARKET CAP < EV → tiene deuda» / «Si MARKET CAP > EV → no tiene deuda») son **incompatibles con la fórmula errónea de `06-E1`** impresa en la misma página | ✅ **DICTAMINADO** — **las cajas ya son correctas** (coinciden con la fórmula correcta, `EV=MC+ND`); la incoherencia es interna a la propia página, entre la fórmula (mal) y las cajas (bien). *Ya dictaminado; no se reeleva* |
| **06-E4** | T1 | `[PDF 06, p.9]` rotula **los dos paneles «AMD»**; el panel derecho (rojo, «AMD ES UNA EMPRESA CON DEUDA») es en realidad **Intel** — confirmado por la voz: «aquí vemos a Intel y es todo lo contrario, este tiene deuda neta positiva» `[VÍDEO 06, 08:50]` | ✅ **DICTAMINADO** — es Intel. *Ya dictaminado; no se reeleva* |

> ⚠️ **`[ANOTACIÓN-EDITORIAL]`, no se cita como frase del experto.** En `[VÍDEO 06, 09:41]` el
> `.srt` trae un paréntesis del usuario: *«y en cambio Intel **(en el pdf sale AMD, esto está mal y
> debería poner Intel)** tiene más enterprise value que market cap»*. Ese paréntesis **no es del
> experto** — es la corrección del usuario insertada en la transcripción. Sirve de indicio para
> `06-E4` (y de hecho la confirma), pero no entra al cuerpo con atribución al experto.

---

## Fuente

| Capa | Cobertura | Fiabilidad |
|---|---|---|
| `raw/transcript/06_deuda_y_caja.srt` | Tramo 06:11–10:24 | ✅ **PLENA** (D-46) |
| `raw/pdf/06_deuda_y_caja.pdf`, p.5–6 | Texto extraíble (469 y 702 caracteres) — cajas de decisión nativas del deck (no imagen) | ✅ **PLENA** — con la fórmula errónea de `06-E1` y las cajas correctas de `06-E3`, ambas dictaminadas |
| `raw/pdf/06_deuda_y_caja.pdf`, p.7–8 | 65 caracteres cada una — solo el título; contenido pictórico, estados intermedios de la misma animación que culmina en p.9 | ⚠️ **CAUTELA** — no aportan texto propio, no se usan |
| `raw/pdf/06_deuda_y_caja.pdf`, p.9 | Rótulos «AMD ES UNA EMPRESA CON CAJA/DEUDA» son texto nativo (152 caracteres, con la errata `06-E4`); la tabla de datos (TIKR) es una captura embebida, sin capa de texto | ✅ **PLENA** en los rótulos · ⚠️ **CAUTELA** en la tabla de datos — ver [[ejemplo_06_amd_intel]] |

**Clase de procedencia:** `[VÍDEO]`, `[PDF]` y `[ANOTACIÓN-EDITORIAL]` (no citada como fuente, solo
como indicio). Sin `[INFERIDO]`, sin `[COMPLETADO-EST]`, sin `[JUICIO-CLAUDE]`.
