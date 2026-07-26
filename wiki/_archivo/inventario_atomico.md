---
tipo: tabla-derivada
estado: en-construccion
modulos: [06]
---

# Inventario Atómico — puente al futuro embudo (D-02, D-10)

> Tabla **derivada** del campo "Inputs atómicos" de las fichas de `curso/`. Aplana cada dato atómico
> que el método necesita, su estado financiero de origen y qué concepto lo usa. Es el prerrequisito
> del eventual embudo cuantitativo (Arquitectura A, **diferida** — D-10). **Se regenera de las fichas;
> no es fuente editable a mano.**
>
> ⚠️ **Solo REGLAS y datos metodológicos.** Los EJEMPLOS (cifras de TIKR de AMD/Intel, la analogía de
> la casa) **NO entran** (D-49).

## Inputs atómicos (líneas reportadas / datos de mercado)

| Input atómico | Estado financiero de origen | Naturaleza | Usado en | Notas |
|---|---|---|---|---|
| Deuda financiera CP | Balance — pasivo corriente | stock | [[deuda_financiera]], [[deuda_neta]] | — |
| Deuda financiera LP | Balance — pasivo no corriente | stock | [[deuda_financiera]], [[deuda_neta]] | ¿incluye *leasings* (IFRS 16)? [HUECO] |
| Cash & Cash Equivalents | Balance — activo corriente | stock | [[caja]] | — |
| Marketable Securities (inversiones líquidas) | Balance | stock | [[caja]] | perímetro no cerrado [HUECO] |
| Commercial Papers | Balance | stock | [[caja]] | — |
| Treasury bills / bonos gub. CP | Balance | stock | [[caja]] | — |
| Nº de acciones (shares outstanding) | Balance / mercado | dato | [[enterprise_value]] (Market Cap) | — |
| Precio de la acción | Mercado (intradía) | dato | [[enterprise_value]] (Market Cap) | look-ahead vs balance [HUECO] |
| Intereses minoritarios | Balance | stock | [[enterprise_value]] | puente EV [HUECO] |
| Acciones preferentes | Balance | stock | [[enterprise_value]] | puente EV [HUECO] |
| EBITDA (TTM) | Cuenta de resultados | flujo | [[deuda_neta]] (ratio Net Debt/EBITDA) | mezcla stock/flujo |

## Métricas construidas

| Métrica | Fórmula | Ficha |
|---|---|---|
| Deuda Financiera Total | Deuda fin. CP + Deuda fin. LP | [[deuda_financiera]] |
| Caja (agregada) | Σ partidas líquidas | [[caja]] |
| Deuda Neta | Deuda Financiera Total − Caja | [[deuda_neta]] |
| Enterprise Value | Market Cap + Deuda Neta (+ minoritarios + preferentes) | [[enterprise_value]] |

## Reglas / umbrales (entran al inventario — D-49)

| Regla | Valor | Estado epistémico | Ficha |
|---|---|---|---|
| Net Debt / EBITDA | `< 2` (idealmente) | HEURÍSTICA DEL EXPERTO, SIN JUSTIFICAR (D-08); revisar D-15 en vídeo 16 | [[deuda_neta]] |

## Fuera del inventario (EJEMPLOS — D-49, no metodológicos)
Cifras de TIKR (AMD/Intel: 141.426 / 82.546 / −2.811 / 27.796 / −0,52x / 3,58x…) y la analogía de la
casa (1 M€ / 200.000 €). Son **pedagogía**, no datos operativos (RD-1). No entran aquí.
