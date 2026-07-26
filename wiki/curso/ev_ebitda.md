---
concepto: EV/EBITDA (Enterprise Value / EBITDA)
modulo: 15
molde: 4
estado: completo
fuentes: [VIDEO-15, VIDEO-14, VIDEO-16]
enlaces: [enterprise_value, ev_fcf, cuenta_de_resultados, deuda_neta, marco_multiplos]
transversal: true
---

# EV/EBITDA (Enterprise Value / EBITDA)

> ✅ **Ficha `completo`** (2026-07-19), tras el vídeo 16 — que **cierra el bloque de múltiplos**. Lo
> que aquí queda `AUSENTE` es **`AUSENTE EN LA FUENTE`** de verdad.
>
> ⭐ **El vídeo 16 lo llama «el múltiplo más elegante del humo»** y «**el múltiplo institucional**,
> el que adoran los gestores de traje» `[VÍDEO 16, 26:05–26:19]` — y ahí resuelve, con una regla de
> uso, la **contradicción del EBITDA** que `CLAUDE.md` §6.3 mandaba superficiar. Ver campo 8.

---

## 1 · Definición y qué mide

> «este es como **el primo del EV/FCF**, pero es un poco más corporativo. Porque lo que hace es
> comparar el **valor total de la empresa, el Enterprise Value** —como el anterior múltiplo— pero
> este lo compara **con su EBITDA**» `[VÍDEO 15, 10:10–10:23]`

> «muestra **cuántas veces los inversores están pagando el EBITDA anual** de una compañía» `[VÍDEO
> 15, 10:32–10:37]`

El EBITDA, definido en el propio vídeo: «aquellos beneficios **antes de intereses, impuestos,
depreciaciones y amortizaciones**» `[VÍDEO 15, 10:23–10:29]` → [[cuenta_de_resultados]] campo 3.

---

## 2 · Familia por numerador

**El numerador es el [[enterprise_value]]**, igual que [[ev_fcf]] — y el vídeo lo dice
explícitamente («como el anterior múltiplo»). Lo separa de [[per]], [[p_bv]] y [[p_fcf]], que usan el
precio.

> 🆕 ✅ **FAMILIA: VALOR DE EMPRESA (EV)** — aportado por el **vídeo 14** (D-76, 2026-07-19), que la
> declara **superior a la del precio**, y con el criterio explícito:
>
> > «los que se basan en el **valor de la empresa (EV)** —EV/EBITDA, EV/Ventas, EV/FCF—: aquí **ya
> > jugamos en otra liga**. Estos múltiplos ya **incluyen la deuda, el efectivo y todo lo que
> > realmente pesa** en una valoración, por eso suelen dar **una foto mucho más completa** de lo que
> > vale la empresa en su conjunto, **y no solo la parte visible en bolsa**» `[VÍDEO 14, 06:00–06:24]`
>
> Taxonomía completa → [[marco_multiplos]] §4.1.

**Grupo del experto:** *ratios de valoración*, el quinto y último de ese grupo →
[[mapa_tematico]] §1.

---

## 3 · Fórmula

```
EV/EBITDA = Enterprise Value / EBITDA
```

`[VÍDEO 15, 10:10–10:29]`. Los dos componentes ya tienen ficha: [[enterprise_value]] y el EBITDA en
[[cuenta_de_resultados]] campo 3.

---

## 4 · Bandas + caveat pegado

### 🆕 ✅ El valor de referencia — VERIFICADO contra la captura

| Banda | Lectura | ⭐ Caveat del experto |
|---|---|---|
| **EV/EBITDA < 10** | Valor de referencia para «detectar si existe un dato infravalorado» `[VÍDEO 14, 03:57–04:03]` · `[CAPTURA 14_tabla_referencias_multiplos]` | ✅ **Caveat pegado:** «**no son sagrados, son de referencia**… no lo toméis como niveles que marcan lo barato o lo caro» `[VÍDEO 14, 03:20–03:35]` · «**orientativo**… puede variar por completo» `[VÍDEO 14, 04:36–04:44]` |

> ✅ **Cifra VERIFICADA por Gerard contra la captura** (2026-07-19). ⚠️ **La voz solo nombra el ratio
> y NO pronuncia el valor**: vivía **únicamente en la imagen** (`CAUTELA`), y por eso se elevó en la
> ingesta del vídeo 14 en vez de escribirse a ciegas (RD-1 §2). Verificada, **ya entra como método**.

### 🆕 ⭐ La escala fina — aportada por el VÍDEO 16

| Banda | Lectura |
|---|---|
| **< 7** | «nos está indicando que **puede haber valor**, pero **cuidado que no haya gato encerrado**» |
| **≈ 10 o más** | «**probablemente estemos pagando caro**» |

`[VÍDEO 16, 28:05–28:16]` · `[CAPTURA 16_ev_ebitda]` — ✅ **voz y captura coinciden literalmente**.

> ✅ **Compatible con el `< 10` del vídeo 14** — mismo patrón que `14-E1`/`14-E2`: el 14 da el **corte
> grueso** de cribado (`<10`), el 16 **afina** (`<7` valor · zona media · `≥10` caro). **No se
> registra errata** (criterio del usuario: gradiente o atajo-vs-escala ⇒ compatibles).
>
> ⭐ **Y la banda barata trae su propio caveat interno**: «cuidado que no haya **gato encerrado**» —
> es decir, un EV/EBITDA bajo **no basta**, coherente con el punto ciego del campo 8.

**Lectura direccional del vídeo 15** — sin cifra, complementa a la banda de arriba:

| Banda | Lectura | Caveat |
|---|---|---|
| **EV/EBITDA bajo** | «suele indicar que la empresa está **barata en relación con su capacidad de generar beneficios operativos**» `[VÍDEO 15, 09:58–10:03]` | ⚠️ **Sin caveat pegado en esta frase.** El caveat sectorial del vídeo llega **antes y por separado**, aplicado al PER (campo 4 de [[per]]) |
| **EV/EBITDA alto** | `AUSENTE EN EL VÍDEO 15` | — |

> ⚠️ **Se registra que aquí el caveat NO va pegado.** `moldes.md` sostiene que en este corpus «no se
> encontró ni un umbral enunciado sin su matización» y que **una banda sin caveat sería en sí misma
> un hallazgo**. Aquí no hay banda numérica que matizar —solo dirección— así que **la cláusula no
> llega a activarse**, igual que en [[ev_fcf]]. **No es una excepción a la regla: es que la regla
> aún no se ha puesto a prueba en este múltiplo.**

---

## 5 · Ejes de comparación

⭐ **Un eje propio de este múltiplo, y es su razón de ser:**

> «este sirve sobre todo para poder **comparar empresas con estructuras de capital distintas**, ya
> que normalmente el EBITDA **limpia ese ruido contable** y te deja ver el **músculo operativo
> real**, quitándole el ruido de impuestos, de depreciaciones y demás» `[VÍDEO 15, 10:37–10:58]`

Es el mismo argumento que [[enterprise_value]] campo 4 registra del vídeo 06 («permite comparaciones
entre empresas con estructuras de capital distintas») — **coherente entre vídeos**, ahora aplicado al
múltiplo concreto.

Rigen además los tres ejes generales del bloque → [[per]] campo 5.

---

## 6 · Aplicabilidad: dónde SÍ

> «el EV/EBITDA es muy útil en **sectores donde la depreciación o la deuda distorsiona bastante los
> resultados. Por ejemplo, sectores de telecomunicación, de industria o de energía**» `[VÍDEO 15,
> 10:11–10:21]` *(numeración del `.srt`: bloques 182–186)*

> «te da una visión **rápida y algo más limpia** que el Free Cash Flow» `[VÍDEO 15, 10:21–10:28]`

⭐ **Tres sectores nombrados explícitamente** — es la asignación sectorial más concreta del corpus
ingerido hasta ahora.

---

## 7 · Aplicabilidad: dónde NO

`AUSENTE EN EL VÍDEO 15` — **ningún marcador de prohibición** para este múltiplo. *(Contrasta con
[[p_bv]] campo 7, del mismo vídeo, que sí trae un «no apliquéis» rotundo — así que la ausencia aquí
no es del vídeo entero, es de este múltiplo.)*

---

## 8 · Punto ciego

🆕 ⭐ **Aportado por el VÍDEO 16 — tercera vez que la inferencia resistida resulta ser suya.**

> «pero atención, porque **no mide la caja real, ni las necesidades de inversión, ni tampoco la
> calidad de los beneficios**» `[VÍDEO 16, 27:59–28:05]`

**El porqué, y es una crítica al EBITDA como magnitud, no al ratio:**
> «el EBITDA en el fondo es como **un beneficio de fantasía**: viene a decir *esto es lo que
> ganaríamos si no tuviéramos que pagar impuestos, ni intereses, ni mantener las máquinas, ni
> renovar nada* — o sea, **un mundo ideal donde todo suma y nada cuesta**» `[VÍDEO 16, 26:50–27:06]`

> «si una empresa **necesita invertir constantemente solo para seguir funcionando**, el EBITDA **te
> va a ocultar esa parte**, que es **la parte fea de la historia**. Y si ignoras eso, es como
> **mirar el coche por fuera sin abrir el capó**» `[VÍDEO 16, 27:15–27:32]`

> ⭐ **Nota de método:** al ingerir el vídeo 15 este campo quedó vacío con una nota — «el experto dice
> que el EBITDA limpia el ruido de depreciaciones; de ahí a *no ve la intensidad de capital* hay un
> paso **que él no da**» (RD-4). **El 16 lo da, y va más lejos**: no solo las necesidades de
> inversión, también **la caja real y la calidad de los beneficios**.

### ⭐ La cita de Buffett — y la contradicción del EBITDA, ya explícita

> «me acuerdo que **Warren Buffett** decía en una de sus charlas que **quien usa el EBITDA, o te está
> intentando vender humo, o se lo está vendiendo a sí mismo** — y en parte tenía toda la razón»
> `[VÍDEO 16, 27:06–27:15]` · `[CAPTURA 16_ev_ebitda]`

> ⭐ **Aquí se cierra el asunto que `CLAUDE.md` §6.3 mandaba superficiar** («el experto usa EBITDA
> como métrica central; otras escuelas lo desprecian»). **No es una contradicción del corpus: el
> experto ASUME la crítica y la resuelve con una regla de uso**, no descartando la herramienta:
>
> > «el EV/EBITDA **no es que debamos descartarlo, ni mucho menos, pero tampoco lo tengamos en un
> > pedestal**. **Úsalo como una lupa, no como un espejo**: te va a ayudar a ver esos detalles
> > operativos, pero **si lo miras demasiado tiempo acabará devolviéndote una versión muy maquillada
> > de la realidad**» `[VÍDEO 16, 28:42–29:02]`
>
> Encaja en el supuesto 4 de «qué NO es errata» (`moldes.md`): **crítica matizada de una herramienta
> que se sigue usando**. La cuarta atribución externa del corpus, y otra vez a un inversor →
> [[mapa_tematico]] §Genealogía.

---

## 9 · Combinación obligatoria

⭐ **El vídeo empareja explícitamente este múltiplo con [[ev_fcf]], y declara para qué sirve cada
uno:**

> «un EV/EBITDA va bien para **comparaciones rápidas**, y un EV/Free Cash Flow te da una **visión más
> realista y conservadora**. Por lo que son **dos herramientas distintas pero las dos
> imprescindibles** si quieres valorar empresas como un profesional» `[VÍDEO 15, 10:28–10:42]`

> ⚠️ **Matiz importante frente al vídeo 12.** Allí el experto declara el EV/FCF «quizás el mejor
> múltiplo» y dice que la caja es «más exacta que el EBITDA». Aquí **no se retracta**: mantiene que
> el EV/FCF es más realista, **pero eleva el EV/EBITDA a «imprescindible»** por su velocidad y por
> los sectores del campo 6. **Las dos afirmaciones conviven** — no es errata (supuesto 4 de «qué NO
> es errata»: crítica matizada de una herramienta que se sigue usando).

---

## 10 · Truco de cálculo

`AUSENTE EN EL VÍDEO 15`.

## 11 · Advertencia de manipulación

🆕 ⭐ **Aportada por el VÍDEO 16, y es la más concreta del bloque** — apunta a una variante del ratio,
no al ratio:

> «**cuidado con el EV/EBITDA *ajustado***: ahí las empresas **se ponen muy creativas**, porque
> **meten ajustes, quitan gastos, inflan ingresos** y te lo sirven **con un lacito muy bonito**. Es
> su forma de decirte que todo va bien **mientras esconden el polvo bajo la alfombra**» `[VÍDEO 16,
> 28:16–28:33]`

⭐ **Y el contraste que lo cierra:** «el **beneficio neto contable**, en cambio, **no da tanto margen
para el maquillaje**, porque **es lo que es: se ve en el informe y a tragar**» `[VÍDEO 16,
28:33–28:42]` → [[cuenta_de_resultados]]

> ⚠️ **Matiz que conviene tener presente al consultar:** aquí el experto defiende el **beneficio
> neto** frente al EBITDA ajustado, mientras que en [[free_cash_flow]] campo 9 (vídeo 09) prefiere
> **el FCF frente al beneficio neto**. **No es contradicción**: son comparaciones distintas —
> beneficio neto es **menos manipulable que un EBITDA ajustado**, y a la vez **más manipulable que la
> caja**. La jerarquía completa del experto es **caja > beneficio neto > EBITDA ajustado**.

## 12 · Referencia sectorial externa

`AUSENTE EN EL VÍDEO 15` — nombra sectores (campo 6) pero **no enlaza ni reparte ninguna fuente**
sectorial con cifras.

## 13 · Demostración del experto

`AUSENTE EN EL VÍDEO 15` — ninguna empresa concreta. El vídeo es de amplitud, no de aplicación.

---

## 14 · Equivalencia técnica

> ⚠️ **APORTACIÓN EXTERNA — `[COMPLETADO-EST]`, pilar (b).** Nada de este bloque es palabra del
> experto. Borrar este bloque debe dejar la ficha íntegra.

| Término del experto | Término estándar | Dónde aparece · matiz |
|---|---|---|
| **EV/EBITDA** | **EV/EBITDA** | ✅ **Ya es el término estándar** — no hay traducción que registrar |
| ⭐ **El matiz que sí importa** | — | **El denominador NO es una línea del 10-K.** El EBITDA es una medida ***non-GAAP*** (ver [[cuenta_de_resultados]] campo 9): **cada fuente lo calcula a su manera**, y algunas publican «EBITDA ajustado», que es otra cifra distinta. **Dos screeners pueden dar EV/EBITDA diferentes para la misma empresa.** El experto no lo advierte y no se le atribuye — pero es la comprobación obligada antes de comparar entre fuentes |

---

## Errata de la fuente

✅ **Sin erratas detectadas en el material propio de este múltiplo.** El tramo `[VÍDEO 15,
09:44–10:42]` es internamente consistente.

⚠️ **Salvo una de transcripción que le afecta de refilón:** al enumerar el grupo de valoración la voz
dice «el **EV/BITDA**» `[VÍDEO 15, 02:44]` → errata `15-E1`, **corregida por evidencia** (el propio
vídeo lo escribe y lo pronuncia bien varias veces después, y `[CAPTURA 15_ratios_de_valoracion]` lo
rotula «EV/EBITDA»). Registro en `erratas.md`.

---

## Fuente

| Capa | Cobertura | Fiabilidad |
|---|---|---|
| `raw/transcript/15_ratios_fundamentales.srt` | Tramo 09:44–10:42 | ✅ **PLENA** (D-46) |
| Deck | ⛔ **NO EXISTE** (D-13) | — |
| `raw/capturas/15_ratios_de_valoracion.jpg` | Lista de los 5 múltiplos del grupo 1 | ⚠️ **CAUTELA** por ser imagen — **sin ninguna cifra**, solo nombres, coincidentes con la voz |

⭐ **Verificación de MÉTODO: ninguna pendiente.** Ni una cifra en ninguna capa.

**Clase de procedencia:** `[VÍDEO]` y `[CAPTURA]`, más el bloque 14 marcado `[COMPLETADO-EST]`.
