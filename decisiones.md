# decisiones.md — Estado VIGENTE de las decisiones

> Índice derivado de `log.md`. Aquí solo el estado actual.
> Para el histórico completo (incluidas las decisiones muertas), ver `log.md`.

| # | Decisión | Estado |
|---|---|---|
| D-01 | Metodología antes que arquitectura | RATIFICADA |
| D-02 | Plantilla de dos capas (Ficha + Inventario Atómico) | RATIFICADA — ⚠️ su **2ª capa SIN OBJETO por D-69** (nada alimenta el inventario atómico); la ficha sigue viva como los **seis moldes** |
| D-03 | Separación Fase A (transcripción) / Fase B (crítica) | ⛔ **SUPERSEDIDA por D-69** — vocabulario muerto; ya disuelta de facto por D-04 |
| D-04 | Capa de errata y estado epistémico en la ficha | RATIFICADA |
| D-05 | Las notas personales no son insumo del inventario | 🔀 **FUSIONADA en D-24 por D-69** (D-24 la superó en alcance) |
| D-06 | Hallazgo: TIKR es el proveedor del experto | REGISTRO |
| D-07 | Adoptar el patrón LLM Wiki (Karpathy) | RATIFICADA |
| D-08 | Frontera dura cerebro / embudo | RATIFICADA |
| D-09 | Clases de procedencia ampliadas | RATIFICADA |
| D-10 | Arquitectura escalonada B → A (copiloto primero) | RATIFICADA |
| D-11 | Separación física curso/ y complemento/ | RATIFICADA |
| D-12 | Alcance = Módulo 3 completo (19 vídeos) | RATIFICADA |
| D-13 | Hallazgo: vídeos 13–19 sin PDF | REGISTRO |
| D-14 | Reformulación de RD-1 (numérico vs narrativo) | RATIFICADA |
| D-15 | Benchmark sectorial (Damodaran) como parte del método | ⚠️ **SUPERSEDIDA por D-56** |
| D-16 | Tratamiento de erratas | RATIFICADA |
| D-17 | Whisper solo para 13–19 | ⚠️ **SUPERSEDIDA por D-23** |
| D-18 | Gobernanza ADR (log append-only) | RATIFICADA |
| D-19 | Desfase de numeración interna de las slides | ⚠️ **RESUELTA por D-65** — el desfase **NO** indica PDFs desactualizados |
| D-20 | Dos perfiles de ficha (cuantitativo / cualitativo) | ⚠️ **SUPERSEDIDA por D-63** (tres moldes, en `moldes.md`) |
| D-21 | Sesgo de supervivencia — contraejemplos obligatorios | RATIFICADA |
| D-22 | Hallazgo: puente cualitativo→cuantitativo latente | REGISTRO |
| D-23 | Whisper para los 19 vídeos, con timestamps | ⚠️ **SUPERSEDIDA por D-45** |
| D-24 | Las notas del usuario dejan de ser insumo del cerebro | RATIFICADA |
| D-25 | Secuencia: ficha primero, plantilla después | RATIFICADA — ⚠️ la **plantilla** que indujo está **SUPERSEDIDA por D-63**; el método (inducir, no diseñar a priori) sigue vigente |
| D-26 | Claude Code como entorno de construcción | RATIFICADA |
| D-27 | Obsidian como capa de lectura, no dependencia | RATIFICADA |
| D-28 | Política de modelos (Sonnet escribe, Opus piensa) | RATIFICADA |
| D-29 | Modelo de transcripción del lote = large-v3 (int8) | ⚠️ **SUPERSEDIDA por D-45** |
| D-30 | Lote en TANDAS de 4–5 (verificación + commit entre tandas) | ⚠️ **SUPERSEDIDA por D-45** |
| D-31 | initial_prompt v2 probado y RECHAZADO; el lote usa v1 | ⚠️ **SIN OBJETO (Whisper descartado, D-45)** |
| D-32 | Acciones autónomas largas (>~10–15 min) requieren preguntar antes | RATIFICADA |
| D-33 | El lote se ejecuta en máquina secundaria (i5-8400), fuera de Claude Code | ⚠️ **SUPERSEDIDA por D-45** |
| D-45 | Whisper DESCARTADO como herramienta de transcripción | RATIFICADA (supersede D-23/29/30/33) |
| D-46 | Transcripción con Subtitle Edit + corrección manual del usuario | RATIFICADA |
| D-47 | `raw/video/` sustituido por `raw/audio/` (.mp3) | RATIFICADA |
| D-48 | Capturas como tercera fuente (`raw/capturas/`, versionada) | ⚠️ **SUPERSEDIDA EN PARTE por D-64**: el PDF es la capa visual; la captura **solo** cubre lo que el deck no alcanza. Sigue vigente el versionado y `NN_descripcion.png` |
| D-49 | Separación estricta EJEMPLOS vs REGLAS en la ficha | RATIFICADA |
| D-51 | Capa PROCEDIMENTAL (`protocolo_analisis.md`, a derivar de 13–19) | RATIFICADA — ⚠️ **contenedor SUPERSEDIDO por D-61** (ahora `capa_decision.md`) y **sus 16 campos por D-63**; **la regla de oro sigue vigente** |
| D-53 | El bloque procedimental es 13–19 (no 17–19) | RATIFICADA — ⚠️ **matizada por D-61**: no es un «bloque»; hay material procedimental en 03, 05, 06, 07 y 10 |
| D-54 | Dependencia circular protocolo↔fichas: no escribir protocolo sin vocabulario ingerido | RATIFICADA — ⚠️ su rama «**si no existe, construirlo en `complemento/`**» **CERRADA sin activarse por D-60** |
| D-55 | Apertura de etapa post-radiografía (`radiografia.md` documento fundacional) | RATIFICADA |
| D-56 | [CORREGIDO] Resolución de D-15: benchmark sectorial confirmado (fuente: Damodaran, vía enlace en descripción del vídeo 16) | RATIFICADA |
| D-57 | [HALLAZGO] Nueva clase de fuente: enlaces en descripción de vídeo | REGISTRO — ítem abierto |
| D-58 | Función del proyecto: copiloto de consulta interpretativa (no ejecución autónoma) | RATIFICADA |
| D-59 | Arquitectura de tres capas: cerebro (construcción) vs datos + contexto (uso, aparcadas) | RATIFICADA |
| D-60 | El protocolo se **DESTILA** tal como aparece (mínimo); NO se construye en `complemento/`. Su minimalidad es un **hallazgo**, no un hueco | RATIFICADA — **cierra la cuestión abierta nº7**; cierra la rama «construir» de D-54 |
| D-61 | `capa_decision.md` **supersede** a `wiki/curso/protocolo_analisis.md` (contenedor único de la capa procedimental) | RATIFICADA (supersede el contenedor de D-51; matiza D-53) |
| D-62 | El orden de **ENSEÑANZA** («en la siguiente clase…») va a `mapa_tematico.md`, **NO** a la capa procedimental | RATIFICADA — **cierra la cuestión abierta nº8**; corrige `CLAUDE.md` §6.2 |
| D-63 | `moldes.md` es la **FUENTE ÚNICA** de los moldes vigentes (1 cuantitativo · 2 estado financiero · 3 cualitativo); `CLAUDE.md` §4 **remite**, no copia | RATIFICADA (supersede D-20, D-25-plantilla y los 16 campos de D-51) |
| D-64 | Modelo de fuente: el **PDF es la CAPA VISUAL del vídeo** (01–12), no un documento aparte; captura **solo** donde el deck no cubre lo operativo. Jerarquía **voz > PDF** intacta | RATIFICADA (supersede D-48 en su parte de «tercera fuente») |
| D-65 | [CORREGIDO] Resolución de D-19: el desfase de numeración **NO** indica PDFs desactualizados — el deck es **un único documento de 10 secciones repartido en 12 vídeos** (02+03 comparten la sección 2; 04+05 la 3) | RATIFICADA — **cierra D-19**; refuerza D-64; **la jerarquía voz > PDF NO cambia** |
| D-66 | Reorganización del repositorio en **cuatro clases** (`_estructura` · `curso` · `ejemplos` · `_provisional` · `_archivo`) + **fiabilidad de lectura** declarada por fuente | RATIFICADA — supersede la **cláusula de ubicación** de D-63 |
| D-67 | [CORREGIDO] **RD-1 reescrita**: origen cerrado (nunca internet ni conocimiento propio) · **texto legible = FUENTE PLENA / imagen = CON CAUTELA** · datos de empresa solo si son definicionales · rige la **construcción**, no el uso | RATIFICADA — supersede la **REDACCIÓN** de RD-1 y D-14, **no su intención** |
| D-68 | Separación método / ejemplo: **`wiki/ejemplos/`**. Punteros desde los moldes 1/2/4/6; **el molde 3 conserva sus Ejemplares dentro de la ficha** | RATIFICADA — amplía D-49, que no ubicaba la separación |
| D-69 | Descontaminación aplicada y **revalidada contra el corpus completo**: `inventario_atomico.md` congelado · `sondeo_procedimental.md` archivado pero **CONSULTABLE** · §6.0 archivada | RATIFICADA — supersede **D-02** (2ª capa), **D-03** y **D-05** |
| D-70 | Un campo **OPCIONAL nunca significa descartar información**: si el material lo trae, se añade siempre | RATIFICADA — **complemento simétrico de RD-4** |
| D-71 | **Regla de arrastre para erratas**, formalizada en `CLAUDE.md` §5: una errata `ARRASTRA` (se eleva de inmediato) si (a) el experto la cita explícitamente hacia adelante, **o** (b) afecta a una definición que otros conceptos del corpus dan por cimiento, aunque nadie la cite | RATIFICADA — formaliza el criterio informal usado desde `08-E1`; añade el criterio (b) tras `09-E1` |
| D-72 | **Campo *Equivalencia técnica*** (`moldes.md` **v6**, moldes 1/2/3/4): el **cuerpo** usa las palabras del experto; **un bloque aparte y marcado** registra el término estándar de la industria como `[COMPLETADO-EST]`, **nunca atribuido al experto**. Motivo: el copiloto (D-58) recibe datos reales **en terminología estándar** | RATIFICADA — supersede la parte de **borrado total** de FCFF/FCFE ordenada al cerrar `09-E1` (su parte de **atribución** sigue vigente). ⚠️ **Reformula la prueba de fuego de RD-3**: borrar todos los bloques `## Equivalencia técnica` debe devolver el curso íntegro |
| D-73 | ⚖️ **Regla afinada de elevación de erratas** (`CLAUDE.md` §5, `moldes.md` **v7**): el umbral para elevar **no es «hay una errata»** sino **«hay una errata que no puedo resolver sin el usuario»**. Si otra parte del corpus la desambigua **sin margen de duda** → el escritor **corrige** y registra el estado nuevo `DICTAMINADO POR EVIDENCIA`, citando el localizador de la evidencia. **Eleva** si depende del criterio del usuario, si **toca método y no ejemplo**, o ante cualquier duda real | RATIFICADA — **matiza** el «SE REGISTRAN, NO SE RESUELVEN» de D-16 sin derogarlo. ⛔ **RD-1 intacta**: corregir con el corpus ≠ corregir con conocimiento del LLM. Motivada por `12-E1` |
| D-74 | **Campo *Grado de formalización declarado* en el molde 6** (`moldes.md` **v8**, campo 10, opcional): **cuánta autoridad se atribuye el experto a sí mismo y a su disciplina**. Es el mismo campo que el molde 5 lleva como campo 7. Lo llevan **solo los moldes que describen «el continente» (5 y 6)**, no los que describen un objeto concreto (1-4) | RATIFICADA — lo destapó el vídeo 13 («*es igual de subjetivo que el trading*»), cuyo pasaje central **no cabía en ninguna casilla**. Ubicado como última casilla de contenido (precedente de D-72) **para no renumerar campos ya referenciados** |
| D-75 | **Cuarto eje de comparación en el molde 4** (`moldes.md` **v9**, campo 5): *divergencia múltiplo ↔ cotización → oportunidad*, junto a los tres canónicos (histórico · competidoras · sector). **Longitudinal**, frente a los tres transversales. **Aporte solo-verbal** | RATIFICADA — **formalizado con N=2** (`ev_fcf` vídeo 12 + `p_fcf` vídeo 15), tras dejarse como observación con N=1. Se aplica **solo donde el experto lo enuncia**. ⚖️ Misma disciplina que mantiene «dos umbrales» del ROIC **sin formalizar**, por seguir en N=1 |
| D-76 | **Política de enriquecimiento de fichas `completo`**: una ficha `completo` lo está **respecto a los vídeos ingeridos**, no para siempre. Si un vídeo posterior **aporta** → se **añade citándolo**; si **contradice** → es errata T2, no se sobrescribe | RATIFICADA — el corpus reparte un concepto entre varios vídeos (PER en 12/15/16; ratios del balance en 03/15). ⚠️ **No relaja RD-3**: enriquecer `curso/` sigue exigiendo aprobación. ⭐ Hace que declarar `completo` deje de ser una apuesta |
| D-77 | **Campo *Demostración del experto* en el molde 5** (`moldes.md` **v10**, campo 12, opcional): puntero a `ejemplos/`, igual que en los moldes 1/2/4/6. El molde 5 era el único de los seis sin dónde apuntar un caso concreto | RATIFICADA — lo destapó el vídeo 17 (recorrido por Alphabet con dos cifras reales), colgado provisionalmente del campo 3. Inaugura con [[ejemplo_17_alphabet]]. En el mismo bump v10 se **corrige la predicción de agregación** de la variante `FILTRO` (era «Conjunción»; la ingesta la desmiente) |
| D-78 | `moldes.md` pasa de **`PILOTO, SIN RATIFICAR`** a **`RATIFICADO`** | RATIFICADA — con los 19 vídeos ingeridos, los seis moldes y las tres variantes del molde 5 tienen material real, y ninguno necesitó un campo nuevo tras v10. **D-63 sigue vigente sin cambios**: ratifica el contenido, no la arquitectura — sigue siendo documento vivo |

---

## Cuestiones abiertas

1. **D-15** — ¿usa el experto benchmarks sectoriales en lugar de umbrales absolutos? → SUPERSEDIDA por D-56
2. ~~**D-19** — ¿están los PDFs desactualizados respecto a los vídeos?~~ → ✅ **RESUELTA por D-65.**
   **No lo están.** El desfase se explica porque el corte en vídeos no coincide con el corte en
   secciones del deck. La hipótesis original («2 vídeos añadidos al inicio») **falla en los vídeos
   02, 03 y 04**: el desfase no es constante, es **0, −1, −1, −2, −2…**. D-19 solo muestreó el 6 y
   el 10, ambos en la cola plana.
3. **Puente completo del EV** — ¿de dónde salen los ~5.762M que faltan en Intel? ¿Fuente canónica
   del EV: cálculo propio o proveedor?
4. **Arquitectura A (embudo cuantitativo)** — diferida hasta tener el Inventario Atómico (D-10).
5. ~~**Plantilla de ficha CUALITATIVA**~~ → ✅ **RESUELTA por D-63.** Es el **Molde 3** de `moldes.md`,
   inducido y pilotado contra el **módulo 10 (moat)**. Los dos perfiles de D-20 y los 16 campos de
   D-51 quedan supersedidos por los **tres moldes**. Fuente única: `moldes.md`.
6. **Capa procedimental** → **RESUELTA la ubicación (D-61)**: contenedor único = `capa_decision.md`
   (hoy en `wiki/piloto/`; su reubicación física es parte de la promoción del piloto).
   `wiki/curso/protocolo_analisis.md` queda SUPERSEDIDO, con su traza conservada. **No se destila solo
   de 13–19** (D-61 matiza D-53): hay material en 03, 05, 06, 07 y 10. Pendiente: ingerir los módulos
   **15** (P-1, negocio→ratios), **05** (P-2, lectura del 10-K) y **18** (P-3, riesgo→peso). Sigue
   rigiendo: **no rellenar por deducción**.
7. ~~⭐ **¿EXISTE el protocolo de análisis en el curso?**~~ → ✅ **RESUELTA por D-60.** **Existe, y es
   mínimo**: un orden global (negocio→ratios) + dos procedimientos locales. **Se destila tal como
   está**; NO se construye en `complemento/`. **La naturaleza del proyecto NO cambia**: sigue siendo
   destilar. La minimalidad es un **hallazgo sobre el curso**, no un hueco a rellenar.

---

## Cuestiones abiertas nuevas

8. ~~**`CLAUDE.md` §6.2 contra `radiografia.md` §C**~~ → ✅ **RESUELTA por D-62.** El schema mandaba
   enviar las frases *«en la siguiente clase…»* a la capa procedimental; `radiografia.md` §C las
   clasifica como **operativas** («logística, no interpretación»). **§6.2 corregido:** orden de
   **análisis** → `capa_decision.md`; orden de **ENSEÑANZA** → `mapa_tematico.md`.

9. **Los 3 campos procedimentales de D-51 no tienen casa por-ficha** — *Rol en el análisis* ·
   *Momento de evaluación* · *Criterio de parada* no existen en los moldes nuevos (D-63). El material
   procedimental tiene destino (`capa_decision.md`, D-61), pero es **un documento único y el rol es
   por-ficha**: un `[HUECO]` como *«¿el ROIC >15% es eliminatorio o condicionante?»* no tiene dónde
   vivir. Consecuencia conocida de sacar el procedimiento de las fichas. **APARCADA por decisión del
   usuario — no se resuelve ahora.**
10. **La «tasa de error de la fuente» no calibra la autoridad del curso** — `CLAUDE.md` §5 la quiere
   como *«evidencia dura para calibrar cuánta autoridad merece el curso»*, pero **mide la fuente Y el
   método**: con la misma fuente dio **0 → 9 → 17** según el instrumento (v1 · v2 · v3), y **no hay
   clase de comparación**. Lo que sí hace es decir **qué tipos de defecto** tiene la fuente.
   **APARCADA: corrección conceptual válida pero no bloquea. §5 NO se reformula.**
