---
concepto: Deuda Financiera
modulo: 06
perfil: cuantitativo
estado: completo
fuentes: [VIDEO-06, PDF-06]
huecos: 5
erratas: 0
enlaces: [caja, deuda_neta, enterprise_value]
---

# Deuda Financiera

> ⛔ **SUPERSEDIDA (2026-07-19).** Rehecha con el molde 1 definitivo (v4) en
> `wiki/curso/deuda_financiera.md`. Esta ficha **no se borra** (D-18, traza) pero **no se
> consulta como método** — usa la de `curso/`.

## Definición del experto
Financiación de la empresa **con coste explícito** (pago de intereses) para sus necesidades. Es lo
que se conoce como **apalancamiento financiero**.
— [VÍDEO 06, 00:38] *"el dinero que una empresa pide prestado con coste explícito, es decir, pagando
intereses… apalancamiento financiero."* · [PDF 06, p.1]

## Fórmula de cálculo
`Deuda Financiera Total = Deuda Financiera CP + Deuda Financiera LP` — [VÍDEO 06, 01:14] · [PDF 06, p.1]
- **CP (corto plazo):** vencimiento < 1 año.
- **LP (largo plazo):** vencimiento > 1 año.

## Tipo
**Línea reportada** (agregada). Suma de dos partidas del **Balance** (pasivo corriente y no
corriente). No lleva supuestos.

## Inputs atómicos
| Input | Estado financiero de origen | Procedencia |
|---|---|---|
| Deuda financiera a corto plazo | Balance — pasivo corriente | [VÍDEO 06, 01:14] · [PDF 06, p.1] |
| Deuda financiera a largo plazo | Balance — pasivo no corriente | [VÍDEO 06, 01:14] · [PDF 06, p.1] |

**Origen de la financiación** (contexto, no altera el cálculo): (a) financiación bancaria;
(b) emisión de bonos corporativos —típico de grandes cotizadas—. [VÍDEO 06, 00:58] · [PDF 06, p.1]

## Decisiones de normalización / ajuste
- **¿Incluye *operating leases* (IFRS 16 / ASC 842)?** [HUECO] — ni el vídeo ni el PDF lo especifican;
  es determinante para el importe (ver Huecos).

## Naturaleza temporal
**Stock** — foto de balance a fecha de cierre (hasta ~90 días de retraso respecto al mercado).

## Umbral / referencia (REGLA)
Sin umbral propio en el módulo 06. La heurística cuantitativa (`Net Debt/EBITDA < 2`) vive en
[[deuda_neta]].

## Aplicabilidad sectorial
[HUECO] — en **bancos y aseguradoras** el concepto no es comparable (la deuda es su materia prima; los
depósitos no son "deuda financiera" en el mismo sentido). No tratado en el módulo.

## Cómo lo interpreta el experto
- **No toda la deuda es mala**; depende de si es **sostenible según el flujo de caja operativo**.
  [VÍDEO 06, 05:52]
- **La deuda de corto plazo es el riesgo clave:** una empresa solvente a LP puede tambalear si no
  cubre el CP por falta de caja → **riesgo de liquidez**; afecta a la cotización incluso con activos
  sólidos. [VÍDEO 06, 02:10]–[03:47] · [PDF 06, p.2]
- **Es clave mirar el calendario de vencimientos.** [VÍDEO 06, 02:10]
- **Bandera roja:** empresa sobreendeudada puede quebrar aunque tenga beneficios contables, sobre todo
  si la deuda es de CP. Sin deuda ⇒ flexibilidad estratégica. [VÍDEO 06, 10:11]

## Ejemplos ilustrativos  ⚠️ PEDAGOGÍA — NO metodología · NO entra en el Inventario Atómico (D-49)
- **Analogía de las dos familias** (hipoteca de 100.000 € con y sin 100.000 € de ahorro): ilustra
  solvencia CP vs LP. [VÍDEO 06, 02:53]–[03:31] · [PDF 06, p.2]. Cifras pedagógicas, no datos.

## Huecos
- **[HUECO] ¿La "Deuda Financiera Total" incluye *operating leases* (IFRS 16 / ASC 842)?**
  - *Resolución esperada:* **complemento/ externo** — norma contable, el curso no la aborda.
- **[HUECO] Aplicabilidad sectorial (exclusión de bancos/aseguradoras).**
  - *Resolución esperada:* **complemento/ externo** — conocimiento de industria fuera del curso.

## Enlaces
[[caja]] · [[deuda_neta]] *(= Deuda Financiera − Caja)* · [[enterprise_value]]

## Rol en el análisis
[HUECO] — el experto no clasifica explícitamente la deuda como ELIMINATORIO / CONDICIONANTE /
CONTEXTUAL. Dice que *"no toda deuda es mala"* [VÍDEO 06, 05:52], lo que sugiere que **no** es
eliminatoria per se, pero no lo afirma como regla de decisión.
- *Resolución esperada:* **módulo posterior** — la función de decisión está en los vídeos 13–19.

## Momento de evaluación
Parcialmente capturado (secuencia verbalizada, no deducida):
- **Antes:** la clasificación CP/LP *"ya la miramos en los estados financieros"* [VÍDEO 06, 01:20] →
  módulos previos (02–04).
- **Después:** *"en la siguiente clase entraremos ya en ratios financieros clave"* [VÍDEO 06, 10:30] →
  módulo 07.
- **Posición exacta en un análisis completo de empresa:** [HUECO] — *Resolución esperada:* vídeos 13–19.

## Criterio de parada
[HUECO] — el experto no da ningún valor de deuda ante el cual deje de analizar.
- *Resolución esperada:* **módulo posterior** — vídeos 13–19.
