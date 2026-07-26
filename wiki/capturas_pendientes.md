# capturas_pendientes.md — Material visual que falta (piloto)

> **Por qué existe.** El modelo de fuente nuevo dice que **el PDF es lo que se ve en pantalla**. Es
> cierto **mientras el experto está en el deck**. Cuando se sale de él —a un balance real, a un
> proveedor de datos, a dibujar encima de la slide— **la capa visual no está en el PDF y no la
> tenemos**. D-48 sigue vigente exactamente ahí, y solo ahí.
>
> **Regla:** ninguna de estas lagunas bloquea la ficha. Se marca lo que falta, **no se inventa lo que
> no se ve** (RD-4). Las fichas están escritas y son usables; lo que falta está señalado en su campo.

---

## ✅ RESUELTA — vídeo 03, el balance de Meta

> **Cerrada el 2026-07-18.** El usuario añadió `raw/capturas/03_balance_meta.png` — el balance
> consolidado real de Meta (10-K 2024/2023) con las etiquetas del experto superpuestas. Cubre los
> cuatro puntos de abajo (los tres ratios están en el mismo tramo que la lectura de pasivo+equity,
> ítem 4 confirmado). Usada en `wiki/curso/balance_general.md` y `wiki/ejemplos/ejemplo_03_balance_meta.md`
> — CAUTELA (RD-1 §2), tratada como ejemplo, no como método. **No se borra el registro original**
> (queda abajo, como traza de qué hizo falta y por qué).

**Era la laguna grave del piloto.** El deck del 03 tiene 4 páginas para 9:17 de vídeo, y **el tramo sin
deck contiene el material más operativo del módulo: los tres ratios con umbral.** El experto los
calcula sobre el balance de Meta, en una pantalla que no existe en el PDF.

| # | Momento | Qué hay en pantalla | Por qué se necesita |
|---|---|---|---|
| **1** | `03 @ ~03:00` *(tramo `02:45–03:44`)* | El balance de Meta, vista completa | «Si esto lo pasamos a un **balance real** de una compañía se vería tal que así» `[02:45]` → «vemos que **la cifra es exactamente igual**» `[03:39]`. Es donde **verifica la ecuación contable** sobre un caso real. |
| **2** | `03 @ ~05:18` *(tramo `05:09–06:09`)* | La sección de pasivo + equity de Meta | ⚠️ **Aquí lee cifras en voz alta**: «fijaros aquí de **182** respecto a lo de **276** total» `[05:15]`. **No transcritas** (RD-1 + D-49). Sin la captura no se puede ni verificar de qué partidas habla. |
| **3** | `03 @ ~07:57` *(tramo `07:43–08:26`)* | Lo que mire al calcular los ratios | 🔴 **La más importante.** Aquí enuncia **liquidez corriente > 1,5**, **deuda/equity < 1,5** y **solvencia**, y dice «en este caso por ejemplo de Meta es un **ratio de casi 3**» `[07:57]`. **Los tres umbrales del módulo salen de este tramo y no hay slide.** |
| **4** | `03 @ ~06:30` *(tramo `06:09–07:43`)* | **Desconocido** | Las **cuatro señales clave** y el orden de lectura. Puede que siga sobre el mismo balance de Meta. **Si es así, basta con anotarlo** — no hace falta captura nueva. |

**Nombres propuestos** (convención D-48, `NN_descripcion.png`):
`03_balance_meta_completo.png` · `03_balance_meta_pasivo_equity.png` · `03_balance_meta_ratios.png`

---

## 🟡 PRIORIDAD MEDIA — vídeo 10, el núcleo de detección

| # | Momento | Qué hay en pantalla | Por qué se necesita |
|---|---|---|---|
| **5** | `10 @ ~03:00` *(tramo `02:17–04:16`)* | **Desconocido** | ~2 de 6:28 **sin página en el deck**, y es el núcleo del módulo: señales de detección, por qué importa el moat, la checklist de 5 puntos, Porter/Morningstar. **Si el experto simplemente mantiene la p.2 en pantalla, basta con anotarlo.** Sin cifras en juego → no hay riesgo RD-1. |

**Nombre propuesto:** `10_señales_deteccion.png` *(solo si hay algo que capturar)*

---

## 🟢 PRIORIDAD BAJA — vídeo 07, la fórmula dibujada

| # | Momento | Qué hay en pantalla | Por qué se necesita |
|---|---|---|---|
| **6** | `07 @ ~04:30` *(tramo `04:18–04:36`)* | `[PDF 07, p.3]` **con la fórmula del ROIC dibujada encima a mano** | «la fórmula del ROIC **que la voy a dibujar**» `[04:18]`. **Es una tercera capa visual** que el PDF no captura. **Baja prioridad porque la dicta entera en voz alta** mientras dibuja, así que la voz la salva. |

**Nombre propuesto:** `07_formula_roic_dibujada.png`

> ⚠️ **El aviso que deja este caso.** Si en otro módulo **dibuja algo sin verbalizarlo**, se pierde
> entero **y ninguna capa lo detectará**: ni la transcripción (no lo dice) ni el PDF (no lo trae).
> **Es un modo de fallo silencioso.** Merece un vistazo al ingerir los módulos con más carga de
> cálculo (06 deuda, 08 capex, 13/16 múltiplos).

---

## No es una captura, pero desbloquea más que ninguna

**Verificar el `.srt` del vídeo 10 contra el vídeo** (D-46) cierra **4 de las 17 erratas** del piloto
(las de tipo `T4`) — incluida **10-E2**, que ahora mismo decide si la taxonomía del moat tiene dos
niveles o ninguno.

`10_el_moat.srt` tiene **puntuación cero** (0 líneas de texto con coma; el 03 tiene 80 y el 07, 126).
Los vídeos **14** (1 coma) y **16** (3 comas sobre 790 subtítulos) tienen la misma pinta. ⚠️ **D-56 se
resolvió con el vídeo 16.** → Ver `erratas_piloto.md`.
