---
title: Ejecución condicional de pasos
description: Configure la ejecución condicional de los pasos de un flujo de trabajo de PlaidCloud para controlar qué pasos se ejecutan según los valores de las variables y la lógica.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Descripción general

Los pasos de un flujo de trabajo normalmente se ejecutan en el orden definido para el flujo de trabajo.  Sin embargo, a menudo resulta útil que determinados pasos solo se ejecuten si se cumplen condiciones predefinidas.  Con la capacidad de condiciones de pasos puede controlar la ejecución según las siguientes opciones:
 - Valores de variables
 - La tabla tiene filas o está vacía
 - La tabla existe o no existe
 - Existe un archivo en Document
 - Falta un archivo en Document
 - Resultado de una consulta de tabla
 - Se cumplen condiciones de fecha y hora

Para las comparaciones de variables o de resultados de consultas de tabla puede usar las siguientes comparaciones:
 - Igual a
 - No es igual a
 - Contiene
 - No contiene
 - Empieza por
 - Termina en
 - Mayor que
 - Menor que
 - Mayor o igual que
 - Menor o igual que

También es importante tener en cuenta que puede tener varias condiciones que deben cumplirse para que el paso se ejecute.  Esto ofrece una herramienta potente para controlar con exactitud cuándo debe ejecutarse un paso.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Una condición de paso determina si un paso se ejecuta. Cuando termina el paso anterior, se comprueba la condición; si se cumple, el paso se ejecuta; de lo contrario, el paso se omite y el flujo de trabajo continúa con el paso siguiente." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">paso anterior</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">¿se cumple la condición?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">variable · filas · el doc. existe</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">sí</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">no</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">el paso se ejecuta</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">paso omitido</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">siguiente</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Una condición controla el paso: si se cumple, el paso se ejecuta; si no, se omite. En ambos casos el flujo de trabajo pasa al paso siguiente. Las condiciones comprueban variables, si una tabla tiene filas o si existe un documento.</figcaption>
</figure>

## Agregar y controlar condiciones

Para activar y agregar condiciones en un paso:
1) Busque el paso en el que desea agregar una condición
2) Haga clic con el botón derecho en el paso y elija **Editar detalles del paso**, o haga clic en su icono de engranaje y cambie a la pestaña **General**
3) Desplácese hasta la sección **Comprobaciones de condición**, al final de la pestaña **General**
4) Marque la casilla **Comprobar condiciones antes de ejecutar** para habilitar el cuadro de diálogo y agregar condiciones.
5) En la sección **Comprobaciones de condición** de la izquierda, seleccione el "+" para agregar una condición nueva
6) Agregue una condición desde la sección con pestañas de la derecha
7) Repita los pasos 5 y 6 según sea necesario para agregar todas sus condiciones

## Ver las condiciones en el lienzo visual

Las condiciones de un paso son visibles desde el lienzo visual sin abrir el paso. El conector que lleva a un paso condicional es **discontinuo** y lleva un pequeño **escudo** en la punta de la flecha. La línea discontinua es lo que se distingue cuando se aleja tanto el zoom que el escudo es demasiado pequeño para apreciarlo.

Haga clic en el escudo para abrir el paso con sus **Comprobaciones de condición** ya a la vista; también puede hacer clic con el botón derecho en el conector y elegir **Editar condiciones…**, que hace lo mismo. El escudo de la propia ficha del paso, abajo a la izquierda, sigue marcando el paso como condicional, como siempre.

Hay dos casos en los que, por diseño, no se muestra ningún escudo en una flecha:

- **Un paso sin conector de entrada.** Un paso condicionado por una fecha o una variable puede estar al inicio de un flujo de trabajo sin que nada conduzca a él. No hay ninguna flecha que marcar, así que solo aparece el escudo de la ficha.
- **Un paso dentro de un grupo contraído.** Su ficha queda plegada dentro de la del grupo y la flecha se ancla en el grupo en lugar de en el paso, por lo que marcarla atribuiría la condición a algo equivocado.

Un paso con varios conectores de entrada recibe un solo escudo, no uno por flecha.

:::note
Abrir las condiciones de esta manera lleva a las comprobaciones de condición en los tipos de paso que usan el formulario de paso nativo. Un tipo de paso que todavía abre la ventana de configuración anterior la abre por la parte superior: las condiciones están ahí, pero no se desplaza hasta ellas.
:::

### Qué indica el escudo que comprueba

La información sobre herramientas del escudo enumera lo que el paso comprueba realmente, en lugar de limitarse a decirle
que comprueba algo:

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

Se enumeran hasta tres comprobaciones, seguidas de un recuento de las restantes (*…y 2 comprobaciones más*), de modo que
la lista siga siendo legible en un paso con muchas condiciones. El mismo resumen aparece en el
escudo de la propia ficha del paso, que es el único que tiene un paso sin conector de entrada.

Al seleccionar el paso, la misma lista aparece en la sección **Condiciones** del panel
Inspector, que es el lugar más cómodo para leer una lista larga.

Conviene saber algunas cosas sobre la redacción:

- **Las comprobaciones de día y mes se leen como nombres**, no como los números con que se almacenan:
  *Día de la semana = lunes*, no *Día de la semana = 3*.
- **La zona horaria aparece solo cuando no es UTC**, como en *(UTC+2)* arriba.
- **Se muestra el filtro de una comprobación de tabla** después de `where`, abreviado si es largo.
- **Una comparación agregada lo indica**: *Valor de consulta (agregado sales_2026.amount) >=
  100* compara un total de la tabla, mientras que *Valor de consulta (sales_2026.amount) >= 100*
  compara el valor de una sola fila.
- **Una comprobación de documento muestra la ruta, pero no la cuenta.** Dos condiciones que comprueban la
  misma ruta en cuentas de Document distintas se leen igual; abra el paso para distinguirlas.
- **Una tabla elegida en el explorador de árbol muestra su nombre** cuando el flujo de trabajo lee o
  escribe esa tabla en algún punto. Si no lo hace, la comprobación se enumera sin el nombre de la tabla
  en lugar de con un identificador interno.


### Qué le costaría la compuerta

Pase el cursor sobre el escudo sin hacer clic y el lienzo resalta con un contorno discontinuo el paso condicional y todo lo que hay a continuación de él: los pasos que no se ejecutarían si esa condición los bloqueara. No cambia nada; aparte el puntero y el resaltado desaparece. Los pasos *anteriores* nunca se resaltan: se ejecutan de todos modos.

Es la misma vista previa que ofrece la etiqueta **deshabilitado** de un grupo deshabilitado, con una diferencia de redacción que importa. Un grupo deshabilitado está realmente apagado, así que su etiqueta indica cuántos pasos se *omitirán*. Una condición solo se evalúa cuando la ejecución llega a ella, así que el escudo indica cuántos pasos *no se ejecutarían* **si** la condición bloquea. Es muy posible que deje pasar todo.

### Qué indica el escudo sobre la última ejecución

El escudo también informa de lo que ocurrió en la ejecución más reciente, de modo que pueda seguir el rastro de un flujo terminado y ver dónde se detuvo:

| Escudo | Significado |
| --- | --- |
| Escudo liso | El paso es condicional. Aún no se ha ejecutado o se está ejecutando ahora. |
| Escudo con un **+** | El paso se ejecutó en la última ejecución. |
| Escudo con un **−** | El paso no se ejecutó en la última ejecución. |

Los tres se distinguen por su forma, no por el color, y la información sobre herramientas del escudo explica el estado con palabras. Se actualiza en directo mientras se ejecuta un flujo de trabajo, así que no necesita volver a cargar el lienzo para ver cómo una ejecución llega a una compuerta.

:::caution
Un escudo con un **−** le indica que el paso no se ejecutó. No le indica *por qué*, y no debe interpretarlo como "la condición lo bloqueó". Un paso también se registra como no ejecutado cuando está deshabilitado, cuando su grupo está deshabilitado, cuando falló un paso anterior a él o cuando quedó fuera del alcance de una ejecución parcial. El botón **Ver registros** de la barra de herramientas abre el [registro de ejecución](/es/guides/workflows/viewing-workflow-log/), que indica el motivo de cada paso omitido. Un paso detenido en un punto de interrupción es el único caso excluido deliberadamente: conserva el escudo liso, porque detenerse ahí fue decisión suya y no un resultado de la ejecución.
:::


## Administrar condiciones

Puede agregar tantas condiciones como necesite en la sección **Comprobaciones de condición**.  Al agregarlas, conviene darles un nombre útil para poder encontrarlas fácilmente en el futuro.

Una vez que agregue una condición, selecciónela a la izquierda y los criterios de evaluación de la condición se podrán editar a la derecha.

Para cambiar el nombre de una condición, selecciónela y edite el campo **Nombre** situado en la parte superior del panel Configuración de la derecha, o haga doble clic en la condición de la lista. También puede hacer clic con el botón derecho en una condición para ver **Cambiar nombre** y **Eliminar**; **Eliminar** también está disponible en el botón "−" situado sobre la lista.

Una condición sin ningún tipo de condición seleccionado (por ejemplo, una procedente de un flujo de trabajo anterior o importado) no se puede evaluar. Se trata como no cumplida, por lo que el paso se omite, y el mensaje del paso indica que la condición no dice qué debe comprobar. Abra la condición y elija qué debe comprobar.


## Condiciones de variables

Al comprobar condiciones de variables, debe completarse la sección **Value Check Parameters** para poder hacer una comparación.

En **Variable or Table Field** escriba el nombre de la variable.  Seleccione un tipo de comparación e introduzca un valor de comparación.


## Condiciones básicas de tabla

Si la condición comprueba si una tabla tiene filas o está vacía, también deberá definir la tabla en la pestaña **Selección de datos de la tabla**.


## Condiciones de existencia de tabla

Una condición de existencia de tabla ejecuta el paso solo cuando la tabla se ha creado en el warehouse, o solo cuando no se ha creado. Nunca lee las filas de la tabla, y una tabla escrita con cero filas existe. Un nombre de tabla que no coincide con ninguna tabla del proyecto se considera inexistente. Úsela para construir una tabla en la primera ejecución y dejarla intacta después, o para omitir un paso que lee una tabla que un paso anterior pudo no haber creado.

Los dos tipos de comprobación son `radio_table_exists` y `radio_table_not_exists`. Elija la tabla de la misma manera que en una condición básica de tabla. Establezca la condición con un asistente de IA o la API REST; la pestaña **Comprobaciones de condición** todavía no la muestra.

## Condiciones avanzadas de tabla

Al usar condiciones avanzadas de tabla, debe completarse la sección **Value Check Parameters** para poder hacer una comparación.

En **Variable or Table Field** escriba el nombre del campo de la selección de tabla.  Seleccione un tipo de comparación e introduzca un valor de comparación.

En la pestaña **Selección de datos de la tabla**, seleccione la tabla y complete la sección de asignación de datos con al menos el campo al que hace referencia la comparación de la condición.

## Condiciones de ruta de documento

Si la condición comprueba si existe un archivo, es necesario elegir la cuenta de documentos y especificar la ruta del documento que se va a comprobar en la pestaña **Ruta del documento**. Una carpeta en esa ruta se considera inexistente, porque la comprobación es de un archivo.

## Condiciones de fecha y hora

Para las selecciones de fecha u hora puede agregar varias condiciones si es necesaria una combinación de ellas.  Por ejemplo, si solo quisiera que un paso se ejecutara los lunes a las 2:05, crearía tres condiciones:
 - Condición de día de la semana establecida en lunes (1)
 - Hora del día establecida en 2
 - Minuto de la hora establecido en 5

### Desfase de zona horaria

Cada condición de fecha y hora tiene su propio **Desfase de zona horaria**, que se muestra como un desfase de horas completas con el nombre de una zona representativa, por ejemplo *Eastern Time (US & Canada) (UTC -5)* o *Asia/Tokyo (UTC +9)*. Las horas que introduce se comparan con el reloj de esa zona.

Una condición nueva empieza con el desfase que informa su navegador, así que en la mayoría de los casos puede dejarlo como está. Establézcalo deliberadamente cuando la programación pertenezca a un lugar distinto de aquel donde usted se encuentra, por ejemplo un cierre que se ejecuta con el reloj del equipo de finanzas. Solo están disponibles horas completas, así que una zona de media hora, como India (UTC +5:30), debe redondearse a la hora completa más cercana.

Una condición guardada antes de que este ajuste entrara en vigor sigue evaluándose con UTC hasta que elija una zona para ella, de modo que las condiciones existentes siguen comportándose exactamente como antes.

:::caution
Las condiciones de **día de la semana** actualmente se comparan con UTC sea cual sea el desfase que elija. Si necesita que una condición de día de la semana caiga en un día concreto en una zona alejada de UTC, tenga en cuenta que puede diferir de su día local durante varias horas a ambos lados de la medianoche.
:::

### Día hábil del cierre financiero

En **Use Financial Close Workday**, la cuenta empieza en **0 para el día 1 del mes**, como indica la sugerencia junto al campo. Así, un cierre que se produce el quinto día del mes es `4`, no `5`.

:::caution
Actualmente esta condición nunca coincide, por lo que un paso protegido por ella no se ejecutará. Use una condición de **día del mes** hasta que se resuelva. Los valores negativos, pensados para contar hacia atrás desde el final del mes, tampoco funcionan.
:::

## Establecer condiciones con un asistente de IA

Un asistente de IA conectado a su espacio de trabajo puede agregar y cambiar las condiciones de un paso por usted, ya sea al crear el paso o al editar uno que ya tenga. Tiene a su disposición todos los tipos de condición descritos anteriormente, excepto **Comprobar cierre financiero de Workday**: un asistente puede escribir esa, pero nunca coincide, por lo que el asistente le avisa en lugar de dejar que pase inadvertida. Establezca esa usted mismo en la pestaña **Condiciones**.

Tres cosas funcionan de forma distinta a la edición manual de condiciones:

- **Toda la lista se reemplaza cada vez.** Si pide que se agregue o cambie una condición, el asistente envía la lista completa, de modo que cualquier condición que omita se elimina. Si no está seguro de que las tenga todas, pídale que enumere las condiciones actuales del paso antes de escribir.
- **Se rechaza una condición que no se puede evaluar.** Una condición que no dice qué comprueba se rechaza en lugar de guardarse, y el paso conserva las condiciones que ya tenía. Corrija la solicitud y vuelva a pedirlo.
- **Una condición incompleta se guarda, con una advertencia.** Una condición a la que le falta el valor con el que comparar, o condiciones agregadas sin marcar **Comprobar condiciones antes de ejecutar**, se almacenan y se notifican como una advertencia. Abra la pestaña **Condiciones** y complételas, o el paso no se comportará como usted pidió.

Un asistente también puede establecer el bloqueo del paso, su visibilidad en las vistas de Gerente y Explorador, su configuración de reintentos y el paso al que ir en caso de error.
