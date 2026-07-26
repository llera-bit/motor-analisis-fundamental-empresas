# registro_organizacion.md — Rastro de decisiones de organización

> **Qué es.** Log ligero de las decisiones de **organización** que he tomado con criterio propio bajo
> el método nuevo. **No es para pedir permiso: es para que quede rastro** y puedas revisarlas.
> Una línea por decisión no trivial.
>
> **Qué NO es.** No es `log.md` (que es APPEND-ONLY, gobernado por D-18, y **no lo he tocado**). Esto
> es un archivo de trabajo del piloto, descartable con el resto de `wiki/piloto/`.
>
> **Nada de lo de aquí cruza el rigor duro.** Todo lo que chocó contra RD-1/RD-2/no-rellenar/jerarquía
> está **registrado sin resolver**, no decidido por mí.

---

## Contenedores creados

| # | Decisión | Porque |
|---|---|---|
| **O-01** | Creé `moldes.md` *(sesión anterior)* | Los moldes 1/2/3 **no existían como archivo**: solo vivían en los mensajes de tarea. `CLAUDE.md` §4 tiene los **viejos** y está prohibido tocarlo. Los arreglos necesitaban un sitio. |
| **O-02** | Creé `erratas_piloto.md` como índice, y **no escribí en `wiki/erratas.md`** | El bloque de erratas no sirve de nada si nadie las cuenta (`CLAUDE.md` §5 quiere la **tasa de error**). Pero `wiki/erratas.md` es del proyecto, no del piloto: contaminarlo con material sin promover lo ensuciaría. Cuando se promueva, se vuelca. |
| **O-03** | Las entradas completas siguen **en la ficha**; el índice solo indexa | `CLAUDE.md` §5 es explícito: *«la corrección vive donde se usa el concepto, no archivada lejos»*. |
| **O-04** | Creé `capa_decision.md` | Destino del material procedimental. **Linaje:** `radiografia.md` §D induce «Capa de decisión / procedimiento» como molde 5. ⚠️ **Ver O-11.** |
| **O-05** | Creé `mapa_tematico.md` | Destino de lo que organiza los conceptos sin ser uno. **Linaje:** `radiografia.md` §C, «arquitectura temática macro». |
| **O-06** | Creé `capturas_pendientes.md` | Lo que falta de la capa visual es **accionable y tiene ciclo de vida** (abierto→hecho). No es un hallazgo de fricción; no cabía en `piloto_friccion.md`. |
| **O-07** | Frontera `capa_decision` / `mapa_tematico`: *orden de análisis* vs *orden de enseñanza* | Sin regla, el «segundo estado clave» y el «y después revisar la deuda» acaban en el mismo saco, y **son cosas distintas**: uno es cómo se enseña, el otro cómo se analiza. `radiografia.md` §C ya hace esa distinción (clasifica los punteros entre clases como **operativos**, no metodológicos). |

## Diseño del bloque de erratas ampliado

| # | Decisión | Porque |
|---|---|---|
| **O-08** | **`T4` cubre ambigüedad Y corrupción** del `.srt`, no solo la ambigüedad por falta de puntuación | El encargo definía `T4` como «ambigüedad de transcripción». Pero «y la rima» `[07, 11:21]` y «a jugadores» `[10, 06:25]` **no admiten dos lecturas: no admiten ninguna**. Son el mismo defecto (**la transcripción no determina qué dijo el experto**) y **se resuelven con la misma acción** (verificar el `.srt` contra el vídeo, D-46). Separarlos habría creado un tipo 5 con idéntico tratamiento. **Generalización mía del encargo — dímelo si no la quieres.** |
| **O-09** | Añadí al formato **«¿hay jerarquía que decida?»** por tipo | El punto que el piloto destapó: **voz > PDF solo aplica en `T1`**. En `T2` los dos polos son voz; en `T3`, los dos son PDF; en `T4` no hay polo B. Sin decirlo explícitamente, un escritor futuro aplicaría la jerarquía donde no toca **y creería estar obedeciendo la regla**. |
| **O-10** | Añadí **«Qué NO es una errata»** al molde | Con 4 tipos el bloque se puede convertir en un cajón y **inflar artificialmente la tasa de error**, que es justo lo que la tasa existe para medir bien. Excluidos: aportes de una sola capa, huecos de cobertura del deck, y `[HUECO]`. |
| **O-11** | Numeración: **correlativo por vídeo, continuando la de v2, sin renumerar** | Las fichas ya se referencian entre sí por ID (`07-E1`, `10-E2`…). Renumerar habría roto las referencias por estética. **Coste asumido:** los IDs no van agrupados por tipo — 07-E5 y 07-E6 son `T2` y caen entre `T1` y `T3`. El índice los ordena. |

## Enrutado del material (PARTE 3.2)

| # | Material | Va a | Porque |
|---|---|---|---|
| **O-12** | «¿está esta empresa creando valor con el capital que gestiona?» `[07, 10:20]` | **`mapa_tematico.md`** §2 | No dice qué hacer ni en qué orden: dice **con qué pregunta leer** el resto del temario. Es marco, no procedimiento. |
| **O-13** | Lectura del balance `[03, 06:54–07:37]` | **`capa_decision.md`** §1 | Es orden de **análisis**. ⚠️ **Ver O-17.** |
| **O-14** | «cuatro cosas / un simple vistazo» `[03, 06:09 / 08:35 / 09:05]` | **`capa_decision.md`** §2 | Es una instrucción sobre **cuánto esfuerzo** merece el estado. Procedimental, aunque no sea un orden. |
| **O-15** | «el segundo estado clave» `[03, 00:08]` · «la siguiente clase» `[03, 09:10]` | **`mapa_tematico.md`** §3 | Orden de **enseñanza**, no de análisis (O-07). |
| **O-16** | ⭐ El concepto paraguas **«la rentabilidad»** `[07, 01:47–02:24]` + `[PDF 07, p.1]` | **`mapa_tematico.md`** §1 | **Resuelve un huérfano que el piloto arrastraba desde v1.** Partir el vídeo 07 en [[roic]] + [[roe]] fue correcto, pero dejó sin dueño el nivel superior — **que tiene una slide entera**. Ahora la tiene. |

## Correcciones a trabajo propio

| # | Qué | Porque |
|---|---|---|
| **O-17** | ⚠️ **Retiré «el orden de lectura del balance en cinco pasos»** → es **una** transición ordenada, no cinco pasos | `piloto_friccion.md` v2 lo llamó «la única secuencia real de los tres vídeos». **Falso.** El único marcador de orden en `[03, 06:54–07:37]` es **un «y después»**; lo demás llega con «también» y «y si». **Numerar una enumeración es ordenarla** → viola la regla de oro de D-51. Corregido en `capa_decision.md` §1. |
| **O-18** | ⚠️ **Eliminé `03-E2` (cobertura del deck) del bloque de erratas** | **No es una errata: es un hueco de material.** No hay dos polos que choquen. Estaba inflando la cuenta con algo que no es un defecto de la fuente sino una ausencia de la nuestra. → movido a [[balance_general]] §7 y a `capturas_pendientes.md`. El ID `03-E2` se **reutilizó** para una errata `T3` real. |
| **O-19** | Re-partí `10-E2`: la mitad **PDF↔PDF** salió a `10-E5` | En v2, `10-E2` mezclaba dos defectos distintos en una entrada («choque doble»). Con 4 tipos cada uno tiene su casilla: la ambigüedad es `T4`, la cabecera que no cubre sus contenidos es `T3`. |
| **O-20** | *(v2, ya registrado)* Retiré «el experto divide los moats en dos familias» | Se apoyaba en puntuación que el `.srt` no tiene. Es el caso que originó `T4`. |

## Consolidación de la capa procedimental (D-60 / D-61)

| # | Decisión | Porque |
|---|---|---|
| **O-21** | **`capa_decision.md` es el contenedor único**; `protocolo_analisis.md` recibe cabecera de superado y **conserva su contenido íntegro** | Instrucción explícita del usuario + **D-55** («las decisiones estructurales pre-radiografía se supersederán **una a una cuando su reemplazo se diseñe**») + **D-18** (no se reescribe historia). **Es el único archivo de `curso/` que he tocado** — RD-3 cubierto por la instrucción explícita. |
| **O-22** | ⭐ **Re-verifiqué los 3 fragmentos del módulo 06 contra el `.srt` antes de moverlos** | No era el encargo, pero mover una cita sin comprobarla es propagar lo que el proyecto existe para impedir. **Mereció la pena: uno estaba mal citado** (ver O-24). |
| **O-23** | **Repartí los 3 fragmentos por tipo**, en vez de volcarlos todos en `capa_decision.md` | Dos llevan marcador explícito de **clase** («ya lo miramos», «en la siguiente clase») → orden de **enseñanza** → `mapa_tematico.md` (regla O-07). Solo uno habla de la **fase del análisis** → `capa_decision.md`. **Razón de fondo, no estética:** el antiguo los anotaba como *«tras Deuda/Caja viene el bloque de ratios»* — leyendo orden de clases como orden de análisis. Dejarlos ahí **haría que el protocolo pareciera secuencial**, que es justo lo que **D-60 niega**. El archivo que existe para registrar que *el protocolo es mínimo* no puede ir inflado con orden de temario. **Nada se pierde: cambia de estante, y cada destino queda mapeado en los dos archivos.** |
| **O-24** | ❌ **Corregí una cita nuestra mal ubicada**: `[06, 08:44]` → **`[06, 08:18–08:34]`** | A los 08:44 el experto habla de la **caja neta de AMD**, no del EV. La cita apuntaba a un sitio donde no está lo citado → defecto de **RD-2**. Corregida en el destino; **en el antiguo se deja como estaba** (no se reescribe historia). Registrada en `log.md` como **errata de nuestro material, no del curso**. |
| **O-25** | Añadí a `capa_decision.md` §1 el **inventario del protocolo mínimo** (P-1/P-2/P-3), marcado `PENDIENTE DE INGESTA` | Sin él, el archivo eran 5 retales del piloto y no **respondía a la pregunta que D-60 cierra** («¿cuál es el protocolo?»). Los cité desde `radiografia.md` §C e hice **spot-check de existencia** contra los `.srt`; **no los he destilado** — D-54: *transcrito ≠ ingerido*. |
| **O-26** | Registré en `capa_decision.md` §4 las **hipótesis heredadas muertas**, en vez de borrarlas | Tres venían de D-51 y ya no se sostienen (la más grave: *«el cerebro EJECUTA el protocolo»*, que **contradice de frente a D-58**). Borrarlas dejaría el mismo error listo para volver. |

---

## Pendientes de decisión HUMANA (no las tomo yo)

| # | Cuestión | Por qué no es mía |
|---|---|---|
| ~~**H-01**~~ | ✅ **RESUELTA** — `capa_decision.md` vs `protocolo_analisis.md` | Resuelta por instrucción explícita del usuario → **D-61**. El antiguo queda superado, con traza. Ver O-21…O-25. |
| **H-02** | Si **D-19 queda resuelto** por el mapa deck↔vídeos (`mapa_tematico.md` §4) | Cambiar el estado de una decisión es `decisiones.md` + `log.md`, prohibidos. **Dejo la evidencia, no el veredicto.** |
| **H-03** | Si se **rehacen 07/03/10** con el método congelado antes de escalar | Los 17 erratas se midieron con **tres instrumentos distintos** (v1: 0 · v2: 9 · v3: 17). Si no se rehacen, el piloto queda como una muestra no comparable con los 16 restantes. Ver `erratas_piloto.md`. |
| **H-04** | Si **`T4` debe cubrir la corrupción** además de la ambigüedad (O-08) | Es una ampliación mía del encargo. |
| **H-05** | *(abierta desde v2)* Si **ARREGLO 2** significa «no fabriques la recíproca» o «no registres la que el experto dice» | Lo leí como lo primero. Lo segundo obligaría a **tirar [[moat]] §4 entero**. |
| **H-06** ⭐ | ⚠️ **`CLAUDE.md` §6.2 instruye lo contrario que `radiografia.md` §C** | §6.2 manda enviar las frases *«en la siguiente clase…»* a la capa procedimental. §C las clasifica como **operativas** — *«es logística, no interpretación»*. **Seguir §6.2 al escalar inflaría la capa procedimental con orden de temario y haría que el protocolo pareciera secuencial**, que es exactamente lo que **D-60 niega**. Lo he destapado al aplicar D-61 y he seguido a §C (ver O-23). **`CLAUDE.md` es la capa schema: actualizarla no es una decisión de organización mía.** Registrada también como cuestión abierta nº8 en `decisiones.md`. |
| **H-07** | Dónde queda `wiki/curso/protocolo_analisis.md` a largo plazo | Hoy: superado con traza, dentro de `curso/`. Al promover el piloto, `capa_decision.md` se reubica y habrá que decidir si el superado **se queda como lápida** en `curso/` o se mueve a un `_archivo/`. Precedente: ya existe `_archivo/whisper/` (D-45). **No lo he movido**: mover un archivo de `curso/` va más allá de la instrucción que me diste. |
