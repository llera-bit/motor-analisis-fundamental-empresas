---
concepto: Deuda financiera (y su clasificación por plazo)
modulo: 06
molde: 1
estado: completo
fuentes: [VIDEO-06, PDF-06]
enlaces: [deuda_neta, flujo_de_caja]
---

# Deuda financiera

---

## 1 · Definición y fórmula

> «por deuda (financiera) entendemos la financiación de las empresas con coste explícito (pago de
> intereses) para sus necesidades. Es lo que se conoce como apalancamiento financiero» `[PDF 06,
> p.1]` · «la deuda financiera, pensar que es el dinero que una empresa pide prestado con coste
> explícito, es decir, pagando intereses, es lo que se conoce como un apalancamiento financiero»
> `[VÍDEO 06, 00:36–00:54]`

**Dos vías de financiación:**
> «financiación bancaria [tradicional]... y en segundo lugar, la emisión de bonos corporativos,
> especialmente en grandes compañías cotizadas» `[VÍDEO 06, 00:54–01:08]` · `[PDF 06, p.1]`

**Clasificación por plazo:**
> «corto plazo, con vencimiento menor a un año y largo plazo, con vencimiento mayor a un año»
> `[VÍDEO 06, 01:12–01:26]` · `[PDF 06, p.1]` — enlaza hacia atrás con los estados financieros
> ([[mapa_tematico]] §3, ya registrado, no se duplica aquí)

*(Fórmula secundaria, tal como pide el molde: no hay una fórmula de cálculo propia de "deuda
financiera" — es la suma directa de los pasivos con coste explícito.)*

---

## 2 · Qué mide / interpretación direccional

Mide el **apalancamiento financiero**: cuánto usa la empresa financiación externa con coste
explícito frente a financiarse con recursos propios.

**Analogía del experto** (genérica, no es dato de empresa — se queda en la ficha, D-68):

> «imagina una familia que no tiene capital invertido y ha pedido una hipoteca al banco de 100.000
> euros y esa familia va pagando mes a mes la hipoteca sin problemas. Y otra familia... que
> dispone de 100.000 para comprar una casa y aún así ha pedido una hipoteca de 100.000... ambas
> familias tienen una hipoteca de largo plazo de 100.000, pero una dispone de un cash de 100.000
> para cubrir gastos o deudas del corto plazo y la otra no, la otra vive al día» `[VÍDEO 06,
> 02:53–03:23]`

> «por eso esta familia, a pesar de que a largo plazo puede ser solvente igual como la de abajo, a
> corto plazo es insolvente o tiene alto riesgo financiero» `[VÍDEO 06, 03:23–03:31]`

---

## 3 · Umbral(es)

`AUSENTE EN LA FUENTE` — el material no da un valor numérico ideal para la deuda financiera bruta
en sí (a diferencia del ratio Net Debt/EBITDA, que sí lo tiene → ver [[deuda_neta]] campo 3).

---

## 4 · Aplicabilidad: dónde SÍ

`AUSENTE EN LA FUENTE` — no se asigna explícitamente a un tipo de empresa o sector.

## 5 · Aplicabilidad: dónde NO

`AUSENTE EN LA FUENTE` — sin marcadores de prohibición (D-70, coherente con lo esperado en el
bloque de métricas).

---

## 6 · Advertencia de uso aislado / cuándo engaña

> «no todas las deudas son malas, pero hay que entender si son sostenibles según el flujo de caja
> operativo» `[VÍDEO 06, 05:46–05:52]` → [[flujo_de_caja]]

---

## 7 · Punto ciego

`AUSENTE EN LA FUENTE` — el material no declara qué no ve la deuda financiera bruta por sí sola.

---

## 8 · Lectura relacional

Se cruza con [[deuda_neta]] (deuda financiera − caja) y con [[flujo_de_caja]] (sostenibilidad de
la deuda según el CFO).

---

## 9 · Recomendación comparativa

**Deuda a corto plazo frente a deuda a largo plazo — no son equivalentes:**

> «no es lo mismo deber a largo plazo que deber a corto plazo» `[VÍDEO 06, 02:15–02:17]` · «por
> eso el riesgo corto plazo es mucho más alto» `[VÍDEO 06, 03:31–03:34]`

---

## 10 · Consistencia temporal

> «es clave mirar el calendario de vencimientos» `[VÍDEO 06, 02:15]`

---

## 11 · Banderas rojas

- «estos problemas de deuda de corto plazo suelen afectar bastante a la cotización, incluso en
  empresas con activos sólidos» `[VÍDEO 06, 03:36–03:43]`
- «una empresa sobreendeudada puede quebrar aunque tenga beneficios contables, sobre todo si esta
  deuda es del corto plazo **(es una de las banderas rojas)**» `[VÍDEO 06, 09:47–10:24]` — marcador
  explícito del propio experto
- «una empresa que no tenga deuda puede tener gran flexibilidad estratégica» `[VÍDEO 06,
  09:47–09:57]` — contraste positivo

---

## 12 · Demostración del experto

`AUSENTE` — no hay demostración con empresa real específica de "deuda financiera" aislada (la
demostración con AMD/Intel es de deuda neta y EV → ver [[deuda_neta]] y [[enterprise_value]]). La
única ilustración de este concepto es la analogía genérica de las dos familias (campo 2), que no
es dato de empresa y por eso se queda en la ficha, no en `ejemplos/`.

---

## 13 · Equivalencia técnica

> ⚠️ **APORTACIÓN EXTERNA — `[COMPLETADO-EST]`, pilar (b).** Nada de este bloque es palabra del
> experto. Se registra para que el cerebro empareje su definición con el dato real (D-72). Borrar
> este bloque debe dejar la ficha íntegra.

| | |
|---|---|
| **Lo que define el experto** | «financiación con **coste explícito (pago de intereses)**» `[PDF 06, p.1]` — campo 1 |
| **Término estándar equivalente** | **Total Debt** — la suma de la deuda con coste financiero: *Short-term debt + Current portion of long-term debt + Long-term debt* |
| ⭐ **El matiz — la confusión más cara de este concepto** | **Total Debt ≠ Total Liabilities.** El pasivo total incluye partidas **sin coste explícito** (proveedores, impuestos diferidos, provisiones) que **NO son deuda financiera** según la definición del experto. Un ratio calculado sobre «Total Liabilities» **no es comparable** con el que él enseña. Su propia clasificación por plazo (CP/LP) es la que separa las dos líneas en el balance |
| **Dónde llega el dato** | Los screeners publican **Total Debt** como campo propio. En el 10-K hay que sumar las líneas de deuda del balance — no siempre vienen subtotalizadas (ver [[balance_general]] campo 9) |

---

## Errata de la fuente

✅ **Sin erratas detectadas en el material propio de este concepto.** Las cuatro erratas conocidas
del vídeo 06 (`06-E1` a `06-E4`, ya `DICTAMINADAS` en `erratas.md`) son todas de deuda neta / EV —
ver [[deuda_neta]] y [[enterprise_value]].

---

## Fuente

| Capa | Cobertura | Fiabilidad |
|---|---|---|
| `raw/transcript/06_deuda_y_caja.srt` | Tramo 00:00–03:52 | ✅ **PLENA** (D-46) |
| `raw/pdf/06_deuda_y_caja.pdf`, p.1–2 | Texto extraíble (716 y 994 caracteres) | ✅ **PLENA** |

**Clase de procedencia:** `[VÍDEO]` y `[PDF]`. Sin `[INFERIDO]`, sin `[COMPLETADO-EST]`, sin
`[JUICIO-CLAUDE]`.
