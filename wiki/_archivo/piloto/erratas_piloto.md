# erratas_piloto.md — Índice de erratas del piloto

> **Qué es.** El índice que hace **contables** las erratas registradas en las fichas del piloto. Es el
> equivalente en `wiki/piloto/` de lo que `CLAUDE.md` §5 pide a `wiki/erratas.md`. **No lo he
> escrito en `wiki/erratas.md`** porque el piloto no se promueve: cuando se promueva, esto se vuelca.
>
> **Las entradas completas viven en la ficha** (`CLAUDE.md` §5: *«la corrección vive donde se usa el
> concepto, no archivada lejos»*). Aquí solo el índice.
>
> ⛔ **Ninguna está resuelta.** Todas `PENDIENTE DE REVISIÓN HUMANA`. Ninguna se ha dictaminado por
> criterio propio (RD-1).

---

## Índice

| ID | Tipo | Ficha | Qué choca | Gravedad |
|---|---|---|---|---|
| **07-E1** | `T1` | [[roic]] | «empresas» (voz `07:00`) vs «**Industrias**» (título del gráfico, `p.5`) — unidad de análisis | 🔴 **Alta** — afecta a las tres cifras leídas sobre esa slide |
| **07-E2** | `T1` | [[roic]] | «detectar empresas de calidad» (voz `03:08`) vs «al menos **descartar empresas mediocres**» (`p.2`) | 🟠 Media — cambia la función del par en el método |
| **07-E3** | `T1` | [[roe]] | El deck llama al ROE «una **métrica muy buena**» (`p.2`); la voz dice «**no me gusta el ROE**» (`05:43`) y lo subordina | 🟠 Media — choque de **postura**, decide el rol del ROE |
| **07-E4** | `T1` | [[roe]] | El gráfico está filtrado a «**ROE > 15%**» (`p.6`) y la voz nunca enuncia ese umbral | 🟡 Baja — silencio sobre un criterio visible |
| **07-E5** ⭐ | `T2` | [[roic]] | «promedio de mercado» = **13-15%** (`03:49`) vs **8-10%** (`07:28`) | 🔴 **Alta** — **decide el sentido del único umbral operativo del vídeo** |
| **07-E6** | `T2` | [[roic]] | «estas dos primeras» (`02:18`) no son las dos primeras de su propia enumeración | 🟡 Baja — probablemente inocuo |
| **07-E7** | `T3` | [[roe]] | El deck define rentabilidad financiera y la reformula con la fórmula de la **económica** (`p.1`) | 🟠 Media — voz calla sobre el polo B |
| **07-E8** | `T4` | [[roic]] | «consistencia en el tiempo **y la rima**» (`11:21`) — cierre corrupto | 🟡 Baja |
| **07-E9** | `T4` | [[roic]] | «el **WAC**» ×2 (`07:12`, `10:54`) — sin ancla en el deck; no determinable | 🟠 Media — es el nombre de una métrica del método |
| **03-E1** | `T1`+`T3` | [[balance_general]] | Activos no corrientes: «más de un año» (voz `01:11`) vs «MÁS DE 1 AÑO **MENOS DE 12 MESES**» (`p.1`, contradictoria en sí misma) | 🟠 Media — definición nuclear del estado |
| **03-E2** | `T3` | [[balance_general]] | `p.1` incluye inventario, maquinaria y **goodwill**; `p.3` —la slide **de activos**— los omite | 🟡 Baja — atenuado por «Entre otros» |
| **10-E1** ⭐ | `T1` | [[moat]] | «activos **tangibles**» (voz `01:20`) vs «CON ACTIVOS **INTANGIBLES**» (`p.2`) | 🔴 **Alta** — rótulo y palabra son opuestos |
| **10-E2** ⭐ | `T4` | [[moat]] | Sin puntuación, «dos familias» vs «lista de efectos» no es decidible (`01:10`) | 🔴 **Alta** — **decide si existe o no la taxonomía de dos niveles** |
| **10-E3** | `T1` | [[moat]] | ASML: «**toda la producción** de máquinas de litografía» (voz `04:16`) vs «**la máquina más importante**, la EUV» (`p.3`) | 🟠 Media — es el ejemplar más rotundo del módulo |
| **10-E4** | `T3` | [[moat]] | «SECTOR LUJO» se desarrolla (`p.3`) y no está en la taxonomía (`p.2`); «PATENTES/LICENCIAS» está en la taxonomía y no se desarrolla | 🟠 Media — atenuado por «Algunas pueden ser éstas…» |
| **10-E5** | `T3` | [[moat]] | La cabecera «AUMENTO DE INGRESOS ó PROPUESTA DE VALOR» (`p.2`) no cubre «BAJOS COSTES» ni «ALTOS COSTES DE SUSTITUCIÓN», que contiene | 🟠 Media — **ya estaba en `log.md`; confirmada** |
| **10-E6** | `T4` | [[moat]] | «mejores retornos **a jugadores**» (`06:25`) — cierre corrupto | 🟡 Baja |

---

## Recuento

### Por tipo

| Tipo | Nº | ¿Existía sitio antes de v3? |
|---|---|---|
| `T1` · voz ↔ PDF | **7** | ✅ Sí |
| `T2` · voz ↔ voz | **2** | ⛔ **No** — se habrían perdido |
| `T3` · PDF ↔ PDF | **4** | ⛔ **No** — se habrían perdido |
| `T4` · ambigüedad de transcripción | **4** | ⛔ **No** — se habrían perdido |
| **TOTAL** | **17** | |

*(03-E1 es `T1` con `T3` secundario; se cuenta una sola vez, en `T1`.)*

### Por vídeo

| Vídeo | Duración | Erratas | Por minuto |
|---|---|---|---|
| **07** ROIC vs ROE | 11:31 | **9** | 0,78 |
| **03** Balance general | 9:17 | **2** | 0,22 |
| **10** El moat | 6:28 | **6** | 0,93 |
| **Total piloto** | 27:16 | **17** | 0,62 |

---

## ⚠️ Cómo NO leer estos números

**La «tasa de error de la fuente» todavía no mide la fuente. Mide la fuente Y el método.**

| Pasada | Método | Erratas registrables |
|---|---|---|
| **v1** | solo transcripción, sin bloque de erratas | **0** |
| **v2** | + PDF, bloque de 1 tipo | **9** |
| **v3** | + bloque de 4 tipos | **17** |

**La fuente no cambió. El instrumento sí.** Cada mejora del método casi dobló la cuenta. Por tanto:

1. **Los 17 son un SUELO**, no una medida. Con un método mejor saldrían más.
2. **Las cifras por vídeo NO son comparables entre sí.** El 07 tiene 9 y el 03 tiene 2, pero el 07 se
   escrutó mucho más (la pregunta de los tres promedios obligó a un contraste exhaustivo). **La
   diferencia mide atención, no calidad.**
3. **El único uso legítimo hoy** es cualitativo: **qué tipos de defecto tiene esta fuente** —
   contradicciones internas de la voz, deck internamente inconsistente, transcripciones que no
   determinan el contenido.
4. **La cuenta solo será comparable cuando el método esté congelado** y se aplique igual a los 19.
   Hasta entonces, no derivar de aquí ninguna conclusión sobre «cuánta autoridad merece el curso»
   (que es para lo que `CLAUDE.md` §5 la quiere).

> **Recomendación (no la ejecuto):** congelar el método antes de escalar, y **rehacer 07/03/10 con el
> método congelado** para que los 19 sean comparables. Si no, el piloto queda como una muestra
> medida con tres reglas distintas.

---

## Lo que desbloquearía varias de golpe

| Acción | Desbloquea |
|---|---|
| **Verificar el `.srt` del vídeo 10 contra el vídeo** (D-46) | **10-E2** ⭐ y **10-E6** — y con 10-E2 cerrada, **10-E5** gana testigo |
| **Verificar el `.srt` del vídeo 07** (D-46) | **07-E8** y **07-E9** |
| **Captura del balance de Meta** (vídeo 03) → `capturas_pendientes.md` | Nada de esta lista, pero cierra el hueco de cobertura del 03 |

⚠️ **4 de las 17 (`T4`) dependen de una sola acción: revisar transcripciones.** Y el vídeo 10 —el de
puntuación cero— concentra las dos `T4` más graves. *(Recordatorio: 14 y 16 tienen la misma pinta —
1 y 3 comas de texto respectivamente. **D-56 se resolvió con el 16**.)*
