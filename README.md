# Cerebro de Análisis Fundamental

**Una base de conocimiento que destila, de forma auditable, la metodología de un experto en
análisis fundamental de empresas a partir de las 19 clases en vídeo de su curso.**

El objetivo no era resumir el curso. Era construir algo capaz de **razonar sobre una empresa
aplicando el método del experto**, con la propiedad de que **cada afirmación se puede rastrear
hasta el segundo exacto del vídeo del que salió**.

Está inspirado en el patrón **LLM Wiki** de Andrej Karpathy: una base de conocimiento mantenida
incrementalmente por un modelo de lenguaje, donde el valor no está en el volumen almacenado sino en
la disciplina con que se decide **qué entra, qué no, y con qué respaldo**.

---

## El problema

Cuando le pides a un modelo de lenguaje que resuma un material extenso, obtienes algo plausible.
Plausible es exactamente el problema: **un resumen bueno y un resumen inventado se parecen mucho**,
y el segundo es indistinguible del primero hasta que alguien va a la fuente a comprobarlo.

En análisis financiero esto no es un defecto cosmético. Si el sistema dice *«busca un ROIC por
encima del 15 %»* y el experto en realidad dijo *«13-15 % es el promedio»*, la diferencia cambia una
decisión de inversión — y nadie lo detectaría, porque ambas frases suenan igual de razonables.

Este proyecto está construido entero alrededor de evitar eso.

---

## Cómo se resuelve

### 1 · Fidelidad auditable: nada entra sin procedencia

Cada campo de cada ficha lleva su origen citado. Una afirmación hablada se cita con timestamp
(`[VÍDEO 06, 14:32]`); una del material escrito, con página (`[PDF 06, p.4]`). **Sin fuente
identificable, no entra.**

Y cuando algo falta, se marca como hueco visible en lugar de rellenarse:

> **Un hueco visible vale más que un relleno plausible.**

Esa regla resultó ser la más productiva del proyecto. En tres ocasiones se resistió la tentación de
deducir el punto ciego de una métrica a partir del contexto; cuando el vídeo que lo trataba se
ingirió de verdad, **lo que el experto decía era más amplio y más preciso que la deducción**. No
inventar no costó información: solo la retrasó hasta que hubo fuente.

También se distingue con qué grado de confianza se lee cada cosa. El texto de una transcripción o
de un documento es **fuente plena**. Una cifra dentro de una imagen es **fuente con cautela**, y
ninguna se transcribe a ciegas: se marca y se eleva para verificación humana. La razón es concreta
— un dato mal leído de una imagen no falla ruidosamente, **sale plausible**.

### 2 · Seis moldes inducidos del material, no impuestos a priori

Las fichas no siguen una plantilla genérica. Siguen **seis moldes distintos**, cada uno con sus
campos propios, porque el material tiene seis naturalezas distintas:

| Molde | Para qué sirve |
|---|---|
| **1 · Métrica cuantitativa** | Deuda, ROIC/ROE, capex, flujo de caja libre |
| **2 · Estado financiero** | Cuenta de resultados, balance, flujo de caja |
| **3 · Cualitativo** | Ventaja competitiva, equipo directivo |
| **4 · Múltiplo de valoración** | PER, PEG, EV/EBITDA, P/S… |
| **5 · Sistema de decisión** | Filtros, sistemas de puntuación, reglas condicionales |
| **6 · Marco / arquitectura** | Vocabulario y mapas del método |

**El orden importa:** los moldes se diseñaron *después* de leer el corpus completo, no antes. Y se
corrigieron cuando la ingesta real los contradijo — el molde 2 tuvo que pasar de un desenlace a
tres porque tres vídeos se comportaron de tres formas distintas y ninguna encajaba.

Un molde equivocado no es un problema de formato: **fuerza a rellenar casillas que el experto nunca
llenó**, que es una forma elegante de inventar.

### 3 · Un aparato para detectar contradicciones de la fuente

Cada clase tiene dos capas —lo que el experto **dice** y lo que **muestra en pantalla**— y no
siempre coinciden. El sistema clasifica cada choque en cuatro tipos:

| Tipo | Qué choca |
|---|---|
| **T1** | La voz contradice al material escrito |
| **T2** | El experto se contradice a sí mismo |
| **T3** | El material escrito es internamente inconsistente |
| **T4** | La transcripción no determina qué se dijo |

**59 contradicciones registradas** en los 19 vídeos, **58 resueltas**. La que queda abierta lo está
por decisión explícita, no por descuido.

La regla central es que **el sistema registra, no arbitra**. Cuando una contradicción depende del
criterio del inversor o de volver a escuchar el audio, se eleva a una persona. Solo se resuelve
sola cuando otra parte del propio material la desambigua sin margen de duda — y entonces queda
anotado *qué* evidencia la resolvió.

---

## Decisiones de arquitectura

Cuatro que explican por qué el resultado es fiable, más allá de que esté bien organizado:

**Una radiografía del material antes de diseñar nada.** Antes de escribir la primera ficha se leyó
el corpus entero para responder: ¿este curso tiene un procedimiento secuencial, o es un inventario
de conceptos? La respuesta —**es un inventario, el protocolo es mínimo**— cambió el diseño por
completo. Sin esa lectura previa se habría construido un sistema de pasos ordenados que el material
no sostiene, y las casillas vacías se habrían rellenado por deducción.

**Separación estricta entre construir y usar.** Durante la construcción el origen es cerrado: todo
sale del material del curso, sin búsquedas externas ni conocimiento aportado por el modelo. Eso
hace que la pregunta *«¿esto lo dijo el experto o lo puso el sistema?»* tenga siempre respuesta.
Consultar fuentes externas es una fase distinta, con reglas distintas.

**Gobernanza tipo ADR, versionada en git.** Las decisiones de diseño no se editan: se registran, y
cuando cambian, la nueva **supersede** a la anterior dejando ambas visibles. **78 decisiones
registradas** a lo largo del proyecto. El motivo es práctico — dentro de seis meses hay que poder
responder *«¿por qué decidimos X y luego lo cambiamos?»*, y **un registro que se reescribe es un
registro que miente**.

**El dictamen final es humano, y está marcado como tal.** Las contradicciones se acumulan sin
resolver hasta que una persona las revisa. En el cierre del proyecto se revisaron las 33 pendientes
volviendo al audio original de cada vídeo — y **cuatro resultaron no ser errores en absoluto**: dos
lecturas correctas mal comparadas, un criterio confundido con un umbral, y un vídeo que se corta a
mitad de palabra. El recuento bajó de 63 a 59 **por depuración, no por descuido**.

---

## Lo que el método encontró

Un sistema así se justifica si produce cosas que una lectura normal no vería. Tres ejemplos reales:

**Una transcripción defectuosa acusó al experto de un error que nunca cometió.** El sistema había
registrado que el experto dijo «activos tangibles» donde su propio material decía «intangibles» —
un fallo suyo, aparentemente. Al corregir la transcripción contra el audio resultó que **siempre
dijo «intangibles»**: quien se equivocó fue la herramienta de transcripción. La lección quedó
escrita en el proyecto: *ante una contradicción en un vídeo cuya transcripción no esté verificada,
sospechar primero del instrumento y solo después de la persona.*

**El múltiplo favorito del experto es el único sin punto ciego declarado.** Los siete múltiplos que
enseña vienen cada uno con su limitación explícita… salvo uno, el que él llama «quizás el mejor»,
al que dedica cuatro minutos sin una sola frase crítica. Eso no es un hueco de la ficha: es un
**rasgo del método y de su sesgo**, y solo se ve cuando los siete están fichados con el mismo molde
y se pueden comparar.

**El curso da reglas locales y nunca un árbitro entre reglas.** Sus tres sistemas de decisión tienen
el mismo vacío, en el mismo sitio: definen bien cada criterio por separado y **no dicen qué prevalece
cuando varios apuntan a la vez en direcciones distintas**. Uno sería un olvido; tres, siempre en el
punto de arbitraje, es una característica del método — enseña qué mirar, y delega el conflicto en el
juicio del inversor. Ese hallazgo solo existe porque los tres se ficharon con la misma estructura.

---

## Estructura del repositorio

```
├── CLAUDE.md          # Las reglas del sistema: qué entra, cómo se cita, cómo se
│                      #   tratan las contradicciones. Es la capa operativa para IA.
├── index.md           # Catálogo de todo el contenido y estado del proyecto
├── log.md             # Registro histórico de decisiones (solo se añade, nunca se edita)
├── decisiones.md      # Índice derivado: el estado vigente de cada decisión
├── fuentes.md         # Inventario del material fuente y su fiabilidad de lectura
│                      #   (documenta las fuentes; los ficheros en sí no están aquí — ver nota abajo)
│
└── wiki/
    ├── _estructura/   # Los seis moldes y la radiografía previa del material
    ├── curso/         # ⭐ El cerebro: 28 fichas de método
    ├── ejemplos/      # Los casos concretos, separados del método a propósito
    ├── complemento/   # Reservado para aportaciones externas (vacío por decisión)
    ├── erratas.md     # Índice de las contradicciones de la fuente
    ├── _provisional/  # Fichas de un piloto temprano, superadas
    └── _archivo/      # Documentos superados, conservados con su traza
```

**Por qué los ejemplos viven aparte:** el curso enseña con casos reales (ASML, Ferrari, Meta…). Una
cifra concreta de una empresa entra al método solo si el concepto no se entiende sin ella —
comprobado sobre el corpus completo, **ninguna lo era**. Todas ilustran. Separarlas evita que el
sistema confunda *«así se calcula el ROIC»* con *«el ROIC de Novo Nordisk era este»*.

**Las citas siguen ahí, aunque los ficheros no.** Cada afirmación del wiki lleva su procedencia
—`[VÍDEO 06, 14:32]`, `[PDF 06, p.4]`— exactamente como se describe arriba. Esas citas apuntan a
ficheros que **no viven en este repositorio** (ver nota siguiente); se conservan tal cual porque son
la prueba de que el sistema cita su fuente, no una promesa de que el fichero esté un clic más allá.

---

## Estado

La ingesta está **completa**: los 19 vídeos leídos, fichados y cerrados. 28 fichas de método, 15
casos de ejemplo, 59 contradicciones de la fuente documentadas y 58 resueltas, y 78 decisiones de
diseño registradas a lo largo del proyecto.

Lo que queda no es construcción: es mantenimiento y las fases de uso, que son otro proyecto.

---

## ⚠️ Sobre el material fuente

**Este repositorio es una copia de presentación.** El trabajo real se hizo en un repositorio de
trabajo privado que además contiene `raw/`: las transcripciones, los PDF de cada clase y las
capturas de pantalla — el material original del curso, de pago y de terceros, sobre el que se citó
cada afirmación.

**Esa carpeta no se incluye aquí, a propósito.** Los derechos del curso son de sus autores; este
proyecto no lo reproduce ni lo sustituye — extrae y estructura una metodología para uso propio, del
mismo modo que lo harían unos apuntes, y esos apuntes no llevan el curso pegado detrás.

Lo que sí viaja intacto a esta copia son **las citas**: cada `[VÍDEO NN, mm:ss]` y `[PDF NN, p.X]`
del wiki sigue apuntando al mismo timestamp y a la misma página que en el repositorio de trabajo.
No apuntan a nada dentro de este repositorio — son la prueba de que la metodología se construyó
citando su fuente, no una invitación a abrir un fichero que no está aquí.

---

*Las decisiones de inversión son siempre de la persona. Este sistema estructura conocimiento; no
recomienda comprar ni vender nada.*
