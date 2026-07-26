---
concepto: Enterprise Value
modulo: 06
perfil: cuantitativo
estado: parcial
transversal: true
fuentes: [VIDEO-06, PDF-06]
huecos: 5
erratas: 3
enlaces: [deuda_neta, market_cap]
---

# Enterprise Value (EV)

> ⛔ **SUPERSEDIDA (2026-07-19).** Rehecha con el molde 1 definitivo (v4) en
> `wiki/curso/enterprise_value.md` — con las tres erratas (fórmula, cajas de decisión, rótulo
> AMD/Intel) ya dictaminadas y aplicadas al cuerpo. Esta ficha **no se borra** (D-18, traza) pero
> **no se consulta como método**.

> ⚠️ **CONCEPTO TRANSVERSAL — FICHA ABIERTA. NO CERRAR AQUÍ.**
> El EV es un concepto de **valoración**, no de estructura financiera. Volverá en los módulos de
> **múltiplos (12–16)**. Esta ficha cubre **solo lo que aporta el módulo 06**; se enriquecerá después.

## Definición del experto
El **valor real / coste total de adquirir una empresa entera**: no solo comprar todas las acciones (el
equity a valor de mercado), sino **también asumir toda su deuda**.
— [VÍDEO 06, 06:21] · [VÍDEO 06, 07:27] *"el coste total de adquirir una empresa, por tanto es capital
más deuda."* · [PDF 06, p.6]

## Fórmula de cálculo
`Enterprise Value = Market Cap + Deuda Neta` [ + intereses minoritarios + acciones preferentes ]
— [VÍDEO 06, 06:24] *"la fórmula de enterprise value es el market cap más la deuda neta."*
**[CORREGIDO]** — el PDF la tiene **invertida** (ver *Errata de la fuente*).

## Tipo
**Métrica construida.** Market Cap + [[deuda_neta]] (+ puente pendiente).

## Inputs atómicos
| Input | Origen | Procedencia |
|---|---|---|
| Market Cap (nº acciones × precio) | Mercado (intradía) | [VÍDEO 06, 06:24] · [PDF 06, p.5] |
| Deuda Neta | [[deuda_neta]] — Balance | [VÍDEO 06, 06:24] |
| Intereses minoritarios + acciones preferentes | Balance | [HUECO] — el puente (ver Huecos) |

## Naturaleza temporal
⚠️ **Mezcla peligrosa:** Market Cap es **intradía**; Deuda Neta es **foto de balance** (hasta ~90 días
de retraso). Combinarlas sin control de fechas genera **look-ahead bias**. (Ver Huecos — arquitectura.)

## Papel metodológico (lo que aporta el módulo 06)
- **Denominador de múltiplos** que permiten comparar empresas con estructuras de capital distintas:
  **EV/FCF, EV/EBITDA, EV/EBIT.** [VÍDEO 06, 07:37] · [PDF 06, p.6]
- Una empresa **con mucha caja tiene un EV más bajo** → puede parecer más barata "a igualdad de EBITDA".
  [VÍDEO 06, 06:24] · [VÍDEO 06, 09:07]

## Cómo lo interpreta el experto
- El EV es **más realista** que mirar solo la capitalización bursátil (Market Cap). [VÍDEO 06, 07:21]
- Relación con la deuda neta: **EV < Market Cap → caja neta**; **EV > Market Cap → deuda**.
  [VÍDEO 06, 08:44]–[09:04] · [PDF 06, p.5]

## Ejemplos ilustrativos  ⚠️ PEDAGOGÍA — NO metodología · NO entra en el Inventario Atómico (D-49)
- **La casa con la caja fuerte:** compras una casa por 1 M€ (hipoteca) pero dentro hay 200.000 € en
  cash → tu deuda/coste real es 800.000 €. [VÍDEO 06, 06:33]–[07:13] · [PDF 06, p.5]
- **TIKR (21-abr-2025), ilustrativos (RD-1):**

  | Empresa | Market Cap (MM) | Deuda Neta (MM) | EV (MM) | Lectura |
  |---|---|---|---|---|
  | AMD | 141.426,03 | (2.811,00) | 138.615,03 | EV < MC (caja neta) · [PDF 06, p.7/p.9] |
  | Intel (INTC) | 82.546,00 | 27.796,00 | 116.104,00 | EV > MC (deuda) · [PDF 06, p.8] |

  *Verificación de la fórmula correcta: AMD 141.426,03 + (−2.811,00) = 138.615,03 ✓.*

## Errata de la fuente
1. **Fórmula del EV INVERTIDA.** [PDF 06, p.5] escribe `ENTERPRISE VALUE = MARKET CAP − NET DEBT`. Es
   **FALSO**. La correcta es **Market Cap + Deuda Neta**, confirmada por el vídeo [VÍDEO 06, 06:24] y
   por los propios números del PDF: AMD 141.426,03 **+** (−2.811,00) = 138.615,03 = EV reportado ✓; la
   resta daría 144.237 ✗. *(erratas.md: 06-E1)*
2. **Cajas de decisión correctas pero incompatibles con esa fórmula.** [PDF 06, p.5] "MC < EV → tiene
   deuda / MC > EV → no tiene deuda" son **correctas** (coinciden con MC + Deuda Neta) pero lógicamente
   **incompatibles** con la fórmula errónea impresa al lado. *El experto tiene la intuición bien y la
   formalización mal.* *(erratas.md: 06-E3)*
3. **Rótulo AMD/Intel.** [PDF 06, p.9] rotula **ambos** paneles como "AMD"; el panel derecho es
   **Intel (INTC)** —así en la captura [PDF 06, p.8] y en el vídeo [VÍDEO 06, 08:50]—. *(erratas.md: 06-E4)*

## Huecos
- **[HUECO] Puente completo del EV.** Intel: 82.546 + 27.796 = 110.342, pero EV reportado = 116.104 →
  faltan **5.762 MM** (minoritarios + preferentes). Ninguna fuente da la fórmula completa.
  - *Resolución esperada:* **decisión de arquitectura pendiente** — ¿fuente canónica del EV = cálculo
    propio o proveedor? Si el sistema lo calcula, no cuadrará con el del proveedor.
- **[HUECO] Naturaleza temporal / look-ahead** (Market Cap intradía vs Deuda Neta foto de balance).
  - *Resolución esperada:* **decisión de arquitectura pendiente** (alineación de fechas en ejecución).

## Enlaces
[[deuda_neta]] · [[market_cap]] *(ficha pendiente)*

## Rol en el análisis
[HUECO] — el EV es un **insumo de valoración** (denominador de múltiplos), no un filtro por sí mismo.
El experto no le asigna rol ELIMINATORIO / CONDICIONANTE / CONTEXTUAL en la secuencia.
- *Resolución esperada:* **módulo posterior** — su papel analítico se desarrolla en los múltiplos
  (módulos 12–16) y la decisión en 13–19.

## Momento de evaluación
[HUECO] en cuanto a su fase. El EV se usa *"cuando vayamos a valorar si una empresa está cara o
barata"* [VÍDEO 06, 08:44] → fase de **valoración por múltiplos** (módulos 12–16), posterior al
análisis de estructura financiera.
- *Resolución esperada:* **módulo posterior** — módulos 12–16.

## Criterio de parada
[HUECO] — sin criterio de parada asociado al EV en el módulo 06.
- *Resolución esperada:* **módulo posterior** — módulos 12–16 / 13–19.
