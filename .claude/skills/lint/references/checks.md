# Razonamiento detrás de cada chequeo

Este documento explica **por qué** cada chequeo está diseñado como está, con las decisiones de
alcance que tomé leyendo la estructura real del proyecto (no un patrón de wiki genérico). Si el
proyecto cambia de convención, este es el sitio para entender qué parte del script hay que tocar.

---

## Decisión de alcance previa a los ocho chequeos: qué es «el wiki vivo»

Casi todos los chequeos necesitan responder primero: ¿qué ficheros cuentan?

`CLAUDE.md` §2 y el índice raíz distinguen explícitamente entre contenido vigente y contenido
superado:

- **Vivo:** `wiki/curso/`, `wiki/ejemplos/`, `wiki/_estructura/`, más `wiki/erratas.md`,
  `wiki/capturas_pendientes.md` e `index.md`.
- **Superado, con traza:** `wiki/_provisional/` (fichas con molde viejo, «se rehacen en la
  ingesta», `CLAUDE.md` mismo) y `wiki/_archivo/` (documentos y el material del piloto).

Esto no es un matiz cosmético para el lint. Verificándolo encontré que
`wiki/_provisional/balance_general.md` y `wiki/_archivo/piloto/piloto_friccion.md` contienen
enlaces `[[ratio_liquidez_corriente]]`, `[[ratio_deuda_equity]]`, `[[ratio_solvencia]]` que
**no resuelven a ningún fichero** — y el propio texto ya lo marca con un `❌` y la frase «ninguna
existe» al lado. No es un bug: es la traza deliberada de una fricción del piloto, documentada por
quien la escribió. Si el chequeo de enlaces rotos barriera esas carpetas, cada ejecución
reportaría el mismo ruido histórico para siempre, y acabaría por enseñar a ignorar la salida del
lint — justo lo que `CLAUDE.md` §9 llama «sesgo de automatización».

Por eso `LIVE_SOURCE_FILES` (de dónde se leen los enlaces salientes, en `check_broken_wikilinks`
y `check_orphan_fichas`) excluye `_provisional/` y `_archivo/`. En cambio `VALID_TARGETS` (contra
qué se resuelve un enlace) **sí** incluye todo `wiki/**/*.md` — un enlace desde una ficha viva
hacia algo en `_archivo/` no está roto si el fichero existe ahí, solo es inusual.

## 1 · Wikilinks rotos

`[[destino]]` y `[[destino|texto a mostrar]]` son las dos formas en uso (verificado: la segunda
aparece en `per.md`, `ev_fcf.md`, `ev_ebitda.md`, `marco_analisis_fundamental.md`). El regex
captura solo la parte antes del `|`.

**Trampa que encontré y evité:** `moldes.md` tiene, dentro de su propia tabla de especificación
de frontmatter, la cadena literal `` `[[ ]]` `` como *ejemplo de sintaxis*, no como enlace real.
Un regex ingenuo la captura como un wikilink con destino en blanco. El script descarta cualquier
destino vacío tras `strip()` — no cuenta como enlace roto, cuenta como «no es un enlace».

## 2 · Fichas huérfanas

Cuenta como «incoming link» cualquier `[[destino]]` encontrado en **cualquier** fichero del
alcance vivo (no solo desde otras fichas de `curso/` — un enlace desde `index.md` o desde un
ejemplo también cuenta como llegada). La alternativa —exigir que el enlace entrante venga
específicamente de otra ficha de `curso/`— habría producido falsos positivos: varias fichas se
enlazan principalmente desde su ejemplo pedagógico o desde `index.md`, no desde otra ficha de
método.

`capa_decision.md` y `mapa_tematico.md` **sí** entran en este chequeo aunque `CLAUDE.md` los
llame «documentos que no son fichas» — la pregunta «¿llega tráfico a esta página?» es válida para
cualquier página del wiki, tenga molde o no.

## 3 y 5 · Frontmatter y estado

La spec vive en `moldes.md`, sección **«Frontmatter — común a los seis moldes»**: seis claves
obligatorias en toda ficha (`concepto`, `modulo`, `molde`, `estado`, `fuentes`, `enlaces`), más
`variante` obligatoria solo si `molde: 5` (los tres sistemas de decisión: FILTRO/SCORING/REGLAS).
**No hay claves adicionales por molde** — los seis moldes comparten un único frontmatter; lo que
cambia entre ellos es la estructura del cuerpo (número y nombre de campos), que este lint no
audita porque exigiría parsear secciones de contenido, no metadatos.

`capa_decision.md` y `mapa_tematico.md` se excluyen explícitamente (`NON_FICHA_DOCS`): no tienen
frontmatter por diseño — son documentos de la capa procedimental/temática, no fichas de molde.
Exigirles frontmatter sería inventar un requisito que el propio `CLAUDE.md` §4 no les pone.

`estado: parcial` fue la convención del bloque de múltiplos (12–16) **mientras estuvo abierto**
— nacían `parcial` a propósito porque el molde 4 se diseñó leyendo los cinco vídeos de golpe pero
la ingesta iba de uno en uno. Con el corpus cerrado (19/19), no debería quedar ninguna. Verificado
en esta primera ejecución: las 28 fichas están en `completo`. Si alguna vez aparece `parcial` de
nuevo, este chequeo la marcará `WARNING`, no `ERROR` — podría ser el inicio legítimo de un nuevo
bloque transversal, no necesariamente un descuido.

## 4 · Estados de errata válidos

La lista **no está inventada por el script**: sale de la línea de `erratas.md` que los declara
(«Estados: `PENDIENTE DE REVISIÓN HUMANA` · `CANDIDATO A LAPSUS` · `DICTAMINADO` · …»). Un estado
se considera válido si la celda **contiene** alguno de esos siete textos como subcadena, no si
coincide exactamente — en la práctica casi todas las filas llevan sufijo libre después del
guion largo (`DICTAMINADO — GRADIENTE COMPATIBLE`, `DICTAMINADO — GANA LA VOZ`...), y exigir
coincidencia exacta habría marcado como inválidas decenas de filas legítimas.

## 6 · Recuento de `erratas.md`

Este chequeo no estaba en el encargo original — lo añadí porque el proyecto **ya tuvo este bug
exacto una vez**: en una sesión de cierre se descubrió que la tabla de Recuento decía «32
pendientes» cuando había 33 en realidad, un desfase acumulado a lo largo de varias rondas de
edición manual. El chequeo recuenta las filas activas (excluyendo las marcadas `NO ES ERRATA`,
que por regla del propio proyecto «salen del cómputo») por tipo primario (T1–T4, tomando el
primero de una entrada doble como `T1+T3`) y por si están dictaminadas (`SIN DICTAMEN` es el
único estado activo que no cuenta como dictaminado), y compara contra lo que la tabla
`## Recuento` declara. En la primera ejecución real esto **sí** encontró un fallo — ver más abajo.

## 7 · Cruce de IDs de errata

Dos direcciones, con severidad distinta a propósito:

- **Ficha cita un `NN-EXX` que no existe en `erratas.md`** → `ERROR`. Es una referencia
  colgando: alguien puede seguir esa cita y no encontrar nada.
- **`erratas.md` indexa un `NN-EXX` que ninguna ficha cita por número** → `INFO`, no error. Es
  común y esperable: varias erratas (sobre todo T4 triviales, nombres mal transcritos) viven
  enteras dentro de su propia tabla de módulo sin que la ficha del concepto necesite mencionarlas
  por número — la ficha simplemente usa la lectura ya corregida. Marcarlo como error habría sido
  exigir una convención que el proyecto nunca declaró.

## 8 · Consistencia de `transversal`

`moldes.md` define `transversal: true` como «si el concepto se alimenta de varios módulos y no de
uno». El chequeo cuenta cuántos `VIDEO-NN` distintos aparecen en `fuentes:` y avisa si son más de
uno sin la marca — pero **como `INFO`, nunca como error**, y esto es deliberado: la política D-76
(«una ficha completo puede enriquecerse con un vídeo posterior sin dejar de ser completo») produce
legítimamente fichas con varias fuentes que no son «transversales» en el sentido fundacional del
bloque de múltiplos, solo fichas que recibieron una aportación tardía. Decidir cuál es cuál exige
leer qué aportó cada vídeo — el script solo puede señalar el candidato.

---

## Resultado de la primera ejecución (2026-07-26)

Antes de arreglar un bug de regex propio (`**10-E7** 🆕` — el emoji después del ID rompía el
patrón que esperaba que a `**ID**` le siguiera directamente un espacio y un `|`), el chequeo 6
reportó tres discrepancias y el 7 un falso «huérfano»: los cuatro señalaban exactamente la misma
fila, `10-E7`, que el parser se saltaba entera. Corregido el regex (`[^|]*` en vez de `\s*` entre
el ID y el siguiente `|`), las cuatro desaparecieron — no eran un problema del wiki, eran un
problema del script. Quedó como caso de prueba real de que el propio lint necesita verificarse
contra el material real antes de confiar en un «sin hallazgos».

## Qué se quedó fuera, a propósito

- **Contradicciones de contenido entre fichas** (`CLAUDE.md` §6.3): exige comparar significado,
  no forma. Fuera del alcance de un script sin LLM.
- **«Claims obsoletos»**: mismo motivo — ya se han encontrado varios a mano (afirmaciones de
  `mapa_tematico.md` sobre cuántos vídeos estaban ingeridos, quedadas atrás según avanzaba el
  proyecto). Detectarlos exige leer con criterio, no solo parsear.
- **Reciprocidad de enlaces** (si A enlaza a B, ¿enlaza B a A?): evaluado y descartado. No todos
  los enlaces del corpus son conceptualmente simétricos — una ficha puede apuntar a su marco
  general sin que el marco necesite apuntar de vuelta a cada ficha que lo usa. Automatizarlo
  habría producido más ruido que señal.
