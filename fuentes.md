# fuentes.md — Inventario del material fuente

**Curso:** Invest Club — Bolsa y Trading
**Alcance del cerebro (D-12):** Módulo 3 — Análisis Fundamental de Empresas (19 vídeos)
**Fuera de alcance:** Módulo 1 (Introducción a finanzas), Módulo 2 (Macroeconomía),
Módulos 1–2 de Trading.
*Excepción:* los condicionantes macro que afecten a reglas fundamentales se capturan
*in situ* donde aparezcan (no como módulo aparte).

---

## Fiabilidad de lectura de cada fuente (RD-1 §2)

**No todas las fuentes se leen igual.** La fiabilidad **no es propiedad del fichero, sino de cada
cita**: un mismo deck mezcla las dos clases.

| Fuente | Carpeta | Fiabilidad | Marcador de cita |
|---|---|---|---|
| Transcripción corregida a mano (D-46) | `raw/transcript/*.srt` | ✅ **PLENA** | `[VÍDEO NN, mm:ss]` |
| Capa de **texto** del deck (bullets, rótulos, tablas) | `raw/pdf/` | ✅ **PLENA** | `[PDF NN, p.X]` |
| **Gráfico** o página sin capa de texto dentro del deck | `raw/pdf/` | ⚠️ **CAUTELA** | `[PDF NN, p.X · IMAGEN]` |
| Captura de pantalla | `raw/capturas/` | ⚠️ **CAUTELA** | `[CAPTURA NN_nombre]` |
| Material externo que el experto reparte | `raw/externo/` | ✅ PLENA, pero **externa** | `[EXTERNO-AVALADO]` |
| Recurso enlazado en la descripción del vídeo | — | ⚠️ con reserva | `[ENLACE-DESC]` |
| Exportado del `.srt` | `raw/transcript/*.txt` | ⛔ **NO es fuente** | — |
| Audio | `raw/audio/` | ⛔ **NO es fuente** (gitignored, D-47) | — |

> ⛔ **Ninguna cifra se extrae a ciegas de una fuente marcada CAUTELA.** Se marca y **se eleva para
> verificación humana**. *Es el riesgo que motivó descartar Whisper (D-45): un dato mal leído de una
> imagen no falla — sale plausible, y se propaga invisible.*

**Verificado sobre `[PDF 07]`**, que demuestra por qué la clase es de la cita y no del fichero:

| Página | Texto extraíble | Clase |
|---|---|---|
| p.1–p.4, p.7 | 423–843 caracteres | ✅ PLENA |
| **p.5, p.6** | **41 caracteres** (solo el título) — son **gráficos** | ⚠️ **CAUTELA** |

Y p.5/p.6 son **justo de donde el experto lee cifras en voz alta**.

⚠️ **Esto muerde ya en el bloque de múltiplos:** las 13 capturas cubren **exactamente los vídeos 14,
15 y 16**, que **no tienen deck**. Ahí la **única** capa visual es la de cautela.

*Cada subcarpeta de `raw/` declara su clase en su propio `README.md`.*

---

## Estado del material

| # | Vídeo | PDF slides | Transcripción | Auditado |
|---|---|---|---|---|
| 01 | ¿Qué es el Análisis Fundamental | ✅ FUNDAMENTAL_1 | ⬜ | ⬜ |
| 02 | Los Estados Financieros — La Cuenta de Resultados | ✅ FUNDAMENTAL_2 | ⬜ | ⬜ |
| 03 | El Balance General — Estructura Financiera | ✅ FUNDAMENTAL_3 | ⬜ | ⬜ |
| 04 | Estado de Flujos de Caja — La Verdadera Salud Financiera | ✅ FUNDAMENTAL_4 | ⬜ | ⬜ |
| 05 | El Informe 10-K — La Fuente más completa | ✅ FUNDAMENTAL_5 | ⬜ | ⬜ |
| **06** | **La Deuda y la Caja — Analizando la Estructura de Financiación** | ✅ `6 (25 08 08) DEUDA Y CAJA` | 🟡 PENDIENTE (corrección manual, D-46) | 🟡 parcial |
| 07 | Rentabilidad del Capital — ROIC vs ROE | ✅ FUNDAMENTAL_7 | ⬜ | ⬜ |
| 08 | El Capex (Capital Expenditures) | ✅ FUNDAMENTAL_8 | ⬜ | ⬜ |
| 09 | El Free Cash Flow | ✅ FUNDAMENTAL_9 | ⬜ | ⬜ |
| **10** | **El Moat (Foso Defensivo)** | ✅ FUNDAMENTAL_10 | ⬜ | 🟡 parcial |
| 11 | El Equipo Directivo | ✅ FUNDAMENTAL_11 | ⬜ | ⬜ |
| 12 | Múltiplos de Valoración | ✅ FUNDAMENTAL_12 | ⬜ | ⬜ |
| 13 | El Múltiplo y el BPA | ❌ | ⬜ | ⬜ |
| 14 | ¿Cuándo Usarlos? | 🟡 *Multiples_por_Sector_ABREVIADO* (tabla, no slides) | ⬜ | ⬜ |
| 15 | Los Ratios Fundamentales | ❌ | ⬜ | ⬜ |
| 16 | La Realidad de los Múltiplos | 🟡 *enlace Damodaran* (ver abajo) | ⬜ | ⬜ |
| 17 | Cómo Detectar Empresas Multibagger | ❌ | ⬜ | ⬜ |
| 18 | Cómo Medir el Riesgo de una Acción | ❌ | ⬜ | ⬜ |
| 19 | Cuándo Acumular, Mantener o Vender | ❌ | ⬜ | ⬜ |

**Herramienta de transcripción (D-46):** transcripción base local → **corrección manual del usuario
en Subtitle Edit** contra el vídeo → el `.srt` corregido = **fuente canónica**; el `.txt` se exporta
del `.srt` (nunca se edita a mano). *(Whisper descartado — D-45; ver `_archivo/whisper/`.)*

**Tercera fuente — capturas (D-48):** `raw/capturas/NN_descripcion.png` (versionadas). Todo elemento
visual con información **NO** presente en el PDF (tablas, gráficos, pantallazos de TIKR) que el
usuario capture durante la corrección. Motivo: Claude Code no ve vídeo ni oye audio; sin captura, ese
contenido visual se perdería para siempre.

---

## Observación estructural crítica (D-13)

**Los PDFs cubren exactamente la parte definicional (1–12) y desaparecen exactamente donde
empieza el juicio (13–19).**

Los vídeos 13–19 contienen la **función de decisión** del método: cuándo un múltiplo aplica,
cómo se detecta un multibagger, cómo se mide riesgo, cuándo se compra y cuándo se vende.

→ **Es lo único del curso que no está en un manual de contabilidad — y es lo único sin
diapositivas.** Refuerza D-23 (transcripción obligatoria de los 19).

---

## Fuentes de datos identificadas en el material

| Fuente | Qué aporta | Procedencia | Notas |
|---|---|---|---|
| **TIKR** | Datos financieros de empresa (capturas de pantalla en los PDFs) | `[INFERIDO]` — D-06 | Es el terminal que usa el experto. Las capturas revelan qué campos mira. |
| **Damodaran (NYU Stern)** — `pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html` | **Benchmarks sectoriales**: márgenes, ROIC, ratios de deuda, betas, coste de capital, múltiplos, por industria | `[ENLACE-DESC]` — **D-56 (confirmado)** | ✅ **CONFIRMADO** vía el enlace en la descripción del vídeo 16. El experto **nunca pronuncia «Damodaran»** en los 19 vídeos. **Fuente viva**: actualiza una vez al año (enero) → se guarda el **puntero, nunca la cifra**. |
| **Filings oficiales (10-K / 10-Q)** | Narrativa (MD&A, riesgos, guidance, moat, política de capital) | Fuente de **uso**, no de construcción | ⚠️ **Fuera del alcance de RD-1 hoy**: rige la CONSTRUCCIÓN, y el cerebro se construye solo con `raw/`. Los filings pertenecen a las capas de uso (D-59, aparcadas). |
| **Tabla sector→múltiplo** — `raw/externo/14_multiplos_por_sector_abreviado.pdf` | 34 sectores → qué múltiplo usar en cada uno | `[EXTERNO-AVALADO]` — D-68 | El experto la **reparte** como material de clase: *«os lo dejaré en descargable»* `[VÍDEO 14, 04:46]`. **No es del curso, pero la hace suya al distribuirla.** |
| **Gráfico «según Morgan Stanley»** — `raw/capturas/14_multiplos_mas_usados_morgan_stanley.jpg` | Los múltiplos más usados históricamente por los inversores | ⚠️ **CAUTELA** (imagen) | Atribuido en voz `[VÍDEO 14, 00:49]`. El vídeo 14 **no tiene deck**: esta captura es la única constancia visual. |

---

## Convención de nombres

`NN_slug.ext` — donde `NN` = número de vídeo del usuario (01–19, con cero delante).
Mismo `NN_slug` para audio, PDF y transcripción → se emparejan automáticamente.

```
raw/audio/06_deuda_y_caja.mp3          (gitignored; D-47)
raw/pdf/06_deuda_y_caja.pdf
raw/capturas/06_descripcion.png        (versionada; D-48)
raw/transcript/06_deuda_y_caja.srt     (corregido a mano = canónico, D-46; con timestamps)
raw/transcript/06_deuda_y_caja.txt     (exportado del .srt; lectura rápida)
```

> **El vídeo original NO vive en el proyecto (D-47).** Ninguna IA procesa vídeo hoy; los `.mkv`
> solo ocupaban espacio. Los originales están íntegros en carpeta del usuario, fuera del repo. En
> `raw/audio/` vive el `.mp3` (gitignored). Cuando haga falta ver una diapositiva, se abre el vídeo
> original desde fuera del proyecto.

**El usuario NO renombra nada.** Vuelca en `raw/_inbox/` y Claude Code ejecuta el
protocolo 6.0 (Ingesta cero): propone la tabla de correspondencias, espera confirmación,
y solo entonces renombra. Los nombres originales se registran aquí.

---

## Tabla de nombres originales

*(Rellenada en la Ingesta cero del 2026-07-12 — preserva la procedencia de cada archivo.)*

**Vídeos originales de la Ingesta cero** (procedencia del `NN_slug`; los `.mkv` se **retiraron** del
proyecto en D-47 — el audio `.mp3` en `raw/audio/` hereda el mismo slug)

| Nombre normalizado | Nombre original |
|---|---|
| `01_que_es_el_analisis_fundamental.mkv` | `1. ¿Qué es el Análisis Fundamental.mkv` |
| `02_cuenta_de_resultados.mkv` | `2. Los Estados Financieros - La Cuenta de Resultados.mkv` |
| `03_balance_general.mkv` | `3. El Balance General – Estructura Financiera de la Empresa.mkv` |
| `04_flujos_de_caja.mkv` | `4. Estado de Flujos de Caja – La Verdadera Salud Financiera.mkv` |
| `05_informe_10k.mkv` | `5. El Informe 10K - La Fuente mas completa de Información Financiera.mkv` |
| `06_deuda_y_caja.mkv` | `6. La Deuda y la Caja - Analizando la Estructura de Financiación.mkv` |
| `07_roic_vs_roe.mkv` | `7. Rentabilidad del Capital - ROIC vs ROE.mkv` |
| `08_capex.mkv` | `8. El Capex (Capital Expenditures).mkv` |
| `09_free_cash_flow.mkv` | `9. El Free Cash Flow.mkv` |
| `10_el_moat.mkv` | `10. El Moat (Foso Defensivo).mkv` |
| `11_equipo_directivo.mkv` | `11. El Equipo Directivo.mkv` |
| `12_multiplos_de_valoracion.mkv` | `12. Múltiplos de Valoración.mkv` |
| `13_multiplo_y_bpa.mkv` | `13. El Múltiplo y el BPA.mkv` |
| `14_cuando_usarlos.mkv` | `14. ¿Cuándo Usarlos.mkv` |
| `15_ratios_fundamentales.mkv` | `15. Los Ratios Fundamentales.mkv` |
| `16_realidad_de_los_multiplos.mkv` | `16. La Realidad de los Múltiplos.mkv` |
| `17_multibagger.mkv` | `17. Como Detectar Empresas Multibagger.mkv` |
| `18_medir_el_riesgo.mkv` | `18. Como Medir el Riesgo de una Acción.mkv` |
| `19_cuando_acumular_mantener_vender.mkv` | `19. Cuando Acumular, Mantener o Vender una Acción.mkv` |

**PDF de slides** — `raw/pdf/*.pdf`

| Nombre normalizado | Nombre original |
|---|---|
| `01_que_es_el_analisis_fundamental.pdf` | `FUNDAMENTAL 1.pdf` |
| `02_cuenta_de_resultados.pdf` | `FUNDAMENTAL 2.pdf` |
| `03_balance_general.pdf` | `FUNDAMENTAL 3.pdf` |
| `04_flujos_de_caja.pdf` | `FUNDAMENTAL 4.pdf` |
| `05_informe_10k.pdf` | `FUNDAMENTAL 5.pdf` |
| `06_deuda_y_caja.pdf` | `6 (25 08 08) DEUDA Y CAJA.pdf` |
| `07_roic_vs_roe.pdf` | `FUNDAMENTAL 7.pdf` |
| `08_capex.pdf` | `FUNDAMENTAL 8.pdf` |
| `09_free_cash_flow.pdf` | `FUNDAMENTAL 9.pdf` |
| `10_el_moat.pdf` | `FUNDAMENTAL 10.pdf` |
| `11_equipo_directivo.pdf` | `FUNDAMENTAL 11.pdf` |
| `12_multiplos_de_valoracion.pdf` | `FUNDAMENTAL 12.pdf` |

**Referencias externas** — `raw/externo/` (movidas aquí en la Ingesta cero; no son slides)

| Nombre normalizado | Nombre original | Nota |
|---|---|---|
| `14_multiplos_por_sector_abreviado.pdf` | `14. Multiples_por_Sector_ABREVIADO.pdf` | Tabla de múltiplos por sector (no diapositivas). Asociada al vídeo 14. |
| `16_damodaran_enlace.txt` | `16.txt` | Enlace a la página de datos sectoriales de Damodaran (NYU Stern). Asociado al vídeo 16. Ver D-15. |
