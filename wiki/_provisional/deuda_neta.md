---
concepto: Deuda Neta
modulo: 06
perfil: cuantitativo
estado: completo
fuentes: [VIDEO-06, PDF-06]
huecos: 5
erratas: 1
enlaces: [deuda_financiera, caja, enterprise_value]
---

# Deuda Neta (Net Debt)

> ⛔ **SUPERSEDIDA (2026-07-19).** Rehecha con el molde 1 definitivo (v4) en
> `wiki/curso/deuda_neta.md` — incluye ahora la Caja como sub-definición y el umbral Net
> Debt/EBITDA < 2. Esta ficha **no se borra** (D-18, traza) pero **no se consulta como método**.

## Definición del experto
Lo que **realmente** tendría que pagar la empresa si cancelara toda su deuda ahora mismo, una vez
descontada la caja disponible.
— [VÍDEO 06, 05:05] *"la deuda neta es la deuda financiera total menos la caja disponible… cuánto
debería pagar realmente la empresa si quisiera cancelar toda su deuda ahora mismo."*

## Fórmula de cálculo
`Deuda Neta = Deuda Financiera Total (CP + LP) − Caja` — [VÍDEO 06, 05:22] · [PDF 06, p.4, recuadro]

**Interpretación del signo:**
- **Deuda Neta > 0** → más deuda que caja → la empresa **está endeudada** (*net debt*).
- **Deuda Neta < 0** → más caja que deuda → **caja neta** (*net cash*).
— [VÍDEO 06, 05:26] · [PDF 06, p.4]

## Tipo
**Métrica construida.** Se deriva de [[deuda_financiera]] − [[caja]].

## Inputs atómicos
| Input | Ficha / origen | Procedencia |
|---|---|---|
| Deuda Financiera Total (CP+LP) | [[deuda_financiera]] — Balance | [VÍDEO 06, 05:22] |
| Caja | [[caja]] — Balance | [VÍDEO 06, 05:22] |

## Decisiones de normalización / ajuste
Hereda las de sus inputs (leasings en la deuda; perímetro de la caja). Ver huecos de
[[deuda_financiera]] y [[caja]].

## Naturaleza temporal
**Stock** — foto de balance. ⚠️ Cuando alimenta el ratio `Net Debt/EBITDA` se combina con un **flujo**
(EBITDA, TTM): mezcla stock/flujo a vigilar.

## Umbral / referencia  (REGLA — entra en el Inventario Atómico, D-49)
> **`Net Debt / EBITDA` — idealmente `< 2`.** — [VÍDEO 06, 09:31]
>
> - **Estado epistémico: HEURÍSTICA DEL EXPERTO, SIN JUSTIFICAR.** Da el número, no su origen, y no
>   dice si varía por sector.
> - **NO se adopta por autoridad** (D-08). Se registra como **hipótesis a validar**, no como parámetro
>   de producción.
> - ⚠️ **Enlaza con D-15:** si el experto usa *benchmarks sectoriales* (Damodaran), este "2" podría ser
>   un umbral absoluto que él mismo relativiza más adelante. **Revisar en el vídeo 16.**

## Aplicabilidad sectorial
[HUECO] — **carece de sentido en bancos y aseguradoras** (la deuda es su negocio). No tratado en el
módulo.

## Cómo lo interpreta el experto
- Indicador **muy usado para comparar empresas dentro de un mismo sector**. [VÍDEO 06, 05:36] · [PDF 06, p.4]
- **Fundamental en ratios de valoración** como `EV/EBITDA`. [VÍDEO 06, 05:41]
- Modifica el [[enterprise_value]]: una empresa con caja tiene un EV más bajo.

## Ejemplos ilustrativos  ⚠️ PEDAGOGÍA — NO metodología · NO entra en el Inventario Atómico (D-49)
Datos de TIKR a 21-abr-2025 (ilustrativos, nunca operativos — RD-1):
| Empresa | Deuda Neta (MM) | Net Debt/EBITDA | Lectura |
|---|---|---|---|
| AMD | (2.811,00) → **caja neta** | (0,52x) | EV < Market Cap · [PDF 06, p.7/p.9] |
| Intel (INTC) | 27.796,00 → **deuda** | 3,58x | EV > Market Cap · [PDF 06, p.8] |

## Errata de la fuente
**El texto del PDF define la Deuda Neta al revés.** [PDF 06, p.4] dice *"restarle **a la caja** la suma
de todas las deudas"* (Caja − Deuda), pero su propio recuadro dice `DEUDA FINANCIERA TOTAL − CAJA`
(correcto). El vídeo confirma la versión correcta: *"deuda financiera total menos la caja"*
[VÍDEO 06, 05:22]. **El cuerpo de esta ficha usa Deuda − Caja (correcto).** *(erratas.md: 06-E2)*

## Huecos
- **[HUECO] Aplicabilidad sectorial** (exclusión de bancos/aseguradoras).
  - *Resolución esperada:* **complemento/ externo**.
- **[HUECO] Justificación y calibración del umbral "< 2"** (¿por qué 2? ¿varía por sector?).
  - *Resolución esperada:* **módulo posterior** — vídeo 16 ("La Realidad de los Múltiplos") + D-15.

## Enlaces
[[deuda_financiera]] · [[caja]] · [[enterprise_value]]

## Rol en el análisis
[HUECO] — **hueco crítico y explícito.** El experto da el umbral `Net Debt/EBITDA < 2` pero **no dice
si superarlo** (sin razón sectorial) **descarta la empresa (ELIMINATORIO) o solo es una alarma a
ponderar (CONDICIONANTE)**. No lo verbaliza.
- *Resolución esperada:* **módulo posterior** — vídeos 13–19 (función de decisión: cuándo un ratio
  descarta vs matiza).

## Momento de evaluación
Parcialmente capturado. *"En la siguiente clase entraremos ya en ratios financieros clave"* [VÍDEO 06,
10:30] → el análisis de deuda neta **precede** al bloque de ratios (módulo 07). Posición exacta en un
análisis completo de empresa: [HUECO].
- *Resolución esperada:* **módulo posterior** — vídeos 13–19.

## Criterio de parada
[HUECO] — el experto no dice que un `Net Debt/EBITDA` alto detenga el análisis (¿lo haría un valor
extremo? no lo verbaliza).
- *Resolución esperada:* **módulo posterior** — vídeos 13–19.
