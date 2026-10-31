---
title: Optimizar un flujo de trabajo
description: Haga que un flujo de trabajo avanzado se ejecute más rápido reconstruyendo sus dependencias a partir del linaje de datos y combinando cadenas de pasos de extracción, con cada combinación verificada con sus datos antes de aplicarse.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

**Optimizar** revisa un flujo de trabajo avanzado y propone cambios que lo hacen ejecutarse más rápido. Usted ve cada cambio antes de que ocurra nada, elige los que desea y puede deshacer el resultado más adelante.

Optimizar funciona con flujos de trabajo avanzados (DAG). Para un flujo de trabajo estándar, elija primero **Convertir a avanzado...**; consulte [Flujos de trabajo avanzados](/es/guides/workflows/advanced-workflows/#elegir-el-tipo-de-flujo-de-trabajo).

## Optimizar un flujo de trabajo

1. En la lista **Flujos de trabajo**, haga clic con el botón derecho en un flujo de trabajo avanzado y elija **Optimizar…**. El flujo de trabajo no debe estar en ejecución ni en pausa, y usted necesita acceso de escritura a él.
2. La ventana **Optimizar flujo de trabajo** muestra un titular como *34 pasos → 30 pasos · 12 pasos pueden ejecutarse en paralelo*. Cuando el flujo de trabajo tiene historial de ejecuciones, añade *~11 s más rápido por ejecución*.
3. Debajo del titular hay una fila por cada cambio, cada una con una casilla, los pasos que afecta, lo que significa para el flujo de trabajo y el tiempo que ahorra, medido como la variación del tiempo real de ejecución. Todas están marcadas; desmarque las que no desee.
4. Una lista **No se puede optimizar** nombra los pasos que Optimizar dejó sin tocar y el motivo concreto de cada uno; consulte [Por qué un paso no se puede optimizar](#por-qué-un-paso-no-se-puede-optimizar).
5. Elija **Aplicar N cambios**.

Si el flujo de trabajo ya no tiene nada que mejorar, la ventana lo indica.

## Los dos tipos de cambio

### Reconstruir las dependencias a partir del linaje de datos

Optimizar lee qué tablas lee y escribe cada paso, y vuelve a trazar las conexiones para que un paso espere solo a los pasos cuyas tablas utiliza. Los pasos que no comparten tablas se ejecutan en paralelo.

- Un paso ya no espera a pasos no relacionados, por lo que ya no se detiene cuando falla un paso no relacionado. Un error se propaga a lo largo de las nuevas dependencias.
- Una ejecución parcial por rango de pasos, como **Ejecutar desde aquí**, sigue las nuevas dependencias.
- El servidor sigue limitando cuántos pasos se ejecutan a la vez.
- Los pasos que nombran sus tablas por nombre o ruta se interpretan igual que los pasos que usan ids de tabla. Un nombre debe coincidir con exactamente una tabla del proyecto; no se puede rastrear un nombre que coincide con varias tablas, una referencia que usa una variable ni una tabla de otro proyecto.
- Un paso deshabilitado nunca impone un orden y no cuenta entre los pasos que pueden ejecutarse en paralelo.
- Optimizar omite este cambio mientras una programación u otro flujo de trabajo ejecuta un rango de pasos de este flujo de trabajo.

### Combinar una cadena de pasos de extracción en uno

Una cadena de pasos Extract Data, cada uno de los cuales lee la tabla que escribió el anterior, se convierte en un único paso que lee el primer origen y escribe el último resultado.

Cada combinación se verifica antes de aplicarse. Optimizar ejecuta los pasos originales y el paso combinado con sus datos actuales en tablas temporales de prueba, y compara ambos resultados fila por fila. Solo aplica la combinación cuando son idénticos. Su flujo de trabajo y sus tablas no se tocan durante la verificación.

- Un cambio de nombre seguido de un filtro, como un paso Select seguido de un filtro, puede combinarse en un solo paso.
- Cuando una cadena completa no puede combinarse, Optimizar ofrece la parte más larga que sí puede.
- Las tablas intermedias de una cadena combinada dejan de ser escritas por el flujo de trabajo. Se conservan, no se eliminan, y el cambio las nombra.
- Una combinación cuyos resultados difieren, o que no se puede verificar, no se aplica, y los resultados indican el motivo. Las combinaciones requieren una tabla de origen con datos.

## Por qué un paso no se puede optimizar

Cada fila de **No se puede optimizar** nombra su propia causa:

| Causa | Qué significa |
|---|---|
| Agregaciones | El paso resume filas, por lo que no puede integrarse en un paso vecino. |
| Dos filtros | Una cadena con dos filtros no puede convertirse en un solo paso. |
| Filtro sobre un valor flotante que puede redondearse | La combinación podría cambiar qué filas pasan, por lo que el filtro se queda donde está. |
| Un paso que ejecuta código del usuario | No se puede verificar la equivalencia de expresiones, scripts y pasos similares. |
| Una tabla leída por más de un paso | La tabla intermedia de la cadena se necesita en otro lugar. |
| Paso deshabilitado | Un paso deshabilitado no se combina y no impone un orden. |
| Miembro de un contenedor de ejecución | Los pasos de un contenedor de ejecución se ejecutan como una unidad. |
| Recuento de filas no disponible | No se puede leer el recuento de filas de la tabla de origen, ni siquiera en vivo, por lo que no se puede dimensionar la combinación para la verificación. |
| No se puede identificar la tabla | El nombre de tabla del paso no coincide con ninguna tabla o coincide con más de una, usa una variable o apunta a otro proyecto. |
| Seguridad a nivel de fila o demasiado grande | La tabla está regida por seguridad a nivel de fila, o es demasiado grande para verificarse automáticamente. |

Los contenedores visuales, que solo agrupan pasos en el lienzo, no impiden una combinación. Cuando una combinación quita pasos de uno, el paso combinado ocupa su lugar y se elimina el contenedor que queda vacío. Deshacer restaura la disposición exactamente.

## Seguir el progreso

Después de aplicar, **Optimizando flujo de trabajo** muestra la fase: *Verificando (3 de 6 ejecuciones)...*, *Comparando resultados...* y *Aplicando...*. Cuando termina, los resultados enumeran lo que se marcó como **Aplicado**, incluido en cuántas filas se verificó cada combinación, y lo que quedó como **No aplicado**, con un motivo para cada caso.

Si el flujo de trabajo cambió mientras Optimizar verificaba, los cambios afectados se omiten y la ventana indica cuántos. Si falla una aplicación, el flujo de trabajo se restaura al estado en que estaba antes.

Una ejecución que se inicia mientras se confirman los cambios se retrasa un momento, no se descarta.

## Deshacer una optimización

Haga clic con el botón derecho en el flujo de trabajo y elija **Deshacer optimización...**, o use **Deshacer optimización** en los resultados. Confirme, y los pasos, la configuración y la disposición del flujo de trabajo vuelven al estado en que estaban antes de la optimización. Se pierden los cambios que haya hecho en el flujo de trabajo desde entonces.

Deshacer necesita puntos de restauración, que no están disponibles en todos los inquilinos. Un inquilino sin ellos no puede aplicar una optimización.

## Optimizar mediante la API y los asistentes de IA

Optimizar también está disponible mediante la API REST y mediante la herramienta `workflow_optimize` para asistentes de IA, con los mismos pasos de vista previa, aplicación y deshacer.

## Pasos siguientes

- [Flujos de trabajo avanzados](/es/guides/workflows/advanced-workflows/): el lienzo, las conexiones y los controles de ejecución
- [Control de la ejecución en paralelo](/es/guides/workflows/controlling-parallel-execution/): ejecute pasos al mismo tiempo
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/): ejecución de un flujo de trabajo de principio a fin
