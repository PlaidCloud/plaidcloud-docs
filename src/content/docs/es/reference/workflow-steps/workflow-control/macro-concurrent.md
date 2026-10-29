---
title: Macro Concurrent (paso)
description: Ejecute una invocación aislada de una macro por cada fila de la tabla de inductores, con un límite de simultaneidad configurable.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Descripción

Ejecuta una [macro](/es/guides/workflows/create-a-macro/) una vez por cada fila seleccionada de una tabla de inductores del llamador. Cada invocación secundaria se comporta como un paso [Macro Run](/es/reference/workflow-steps/workflow-control/run-macro/):

- Recibe un `run_id` nuevo.
- Se ejecuta en su propio esquema temporal (`macrorun_<run_id>`).
- Recibe del llamador vinculaciones de tablas, escalares y dimensiones.
- Copia las tablas de salida declaradas a los destinos del llamador cuando la invocación secundaria termina con `done` o `warn`.
- Elimina el esquema temporal cuando la invocación secundaria termina, falla o se detiene.

Use Macro Concurrent cuando el mismo proceso reutilizable deba ejecutarse para muchas filas, por ejemplo un período, una entidad, un cliente, un lote de archivos o una región por cada fila de la tabla de inductores.

## Inductor

- **Tabla**: la tabla del llamador que contiene una fila por cada invocación de la macro.
- **Ejecuciones simultáneas**: el número máximo de invocaciones secundarias de la macro que se mantienen activas a la vez.

## Selección de datos de la tabla

Seleccione las columnas de la tabla de inductores que necesita cada invocación secundaria. Estas columnas pueden usarse en las vinculaciones de la macro y en el filtro de inductor.

## Filtro de inductor

Opcionalmente, agregue reglas de filtro para la tabla de inductores. Solo las filas que coinciden inician invocaciones secundarias de la macro.

## Macro

- **Proyecto**: el proyecto que contiene la macro. En la v1 debe ser el mismo proyecto que el del llamador.
- **Macro**: el flujo de trabajo de macro que se invoca por cada fila de inductor seleccionada.

## Vínculos de entrada

Los vínculos de entrada conectan los datos del llamador con las entradas declaradas de la macro.

**Vinculaciones de entrada de tablas:**

- **Tabla de origen del llamador**: la tabla que se copia en el esquema temporal de la invocación secundaria.
- **Puerto de destino de la macro**: el nombre de la tabla de entrada o el puerto de la macro que recibe la tabla copiada.
- **Filtro de copia de entrada**: cláusula `WHERE` opcional que se aplica durante la copia de entrada.
- **Columnas JSON**: proyección opcional de columnas en JSON, cuando solo deban copiarse columnas seleccionadas.

**Vinculaciones de entrada escalares y de dimensiones:**

- **Variable de la macro**: la variable del lado de la macro que se establece para la invocación secundaria.
- **Valor**: el valor literal, la referencia a una variable del llamador o el valor de la columna del inductor que se vincula.

Las entradas escalares y de dimensiones se establecen antes de la copia de entrada de las tablas, por lo que los filtros de tabla pueden referenciar esas variables.

## Vínculos de salida

Los vínculos de salida copian las tablas de resultado de la macro a los destinos del llamador.

- **Puerto de origen de la macro**: el nombre de la tabla de salida o el puerto de la macro desde el que se copia.
- **Tabla de destino del llamador**: la tabla del llamador en la que se copia.
- **Columnas JSON**: proyección opcional de columnas en JSON para la copia de salida.

Cada fila del inductor debe resolverse en una tabla de destino distinta, así que incluya una columna del inductor en el nombre del destino; por ejemplo, `results_{region}`. La copia de salida reemplaza el destino en lugar de agregar datos, de modo que si dos filas se resolvieran en el mismo destino solo quedaría el resultado de la segunda; el paso rechaza esa configuración antes de iniciar nada. Para combinar los resultados en una sola tabla, agregue un paso posterior que una las tablas de cada fila.

La copia de salida se omite en una invocación secundaria detenida para que no se escriban resultados parciales en tablas duraderas del llamador.

## Cuando una invocación secundaria deja de responder

Una invocación secundaria informa de su propio resultado cuando termina, por lo que una invocación cuya máquina se detiene sin aviso nunca informa de nada. En lugar de esperarla indefinidamente, el paso comprueba que cada invocación secundaria que sigue esperando esté activa.

- Una invocación secundaria que ya se inició se comprueba aproximadamente una vez por minuto, y solo mientras no muestre señales de progreso. Una invocación que trabaja en un único paso de larga duración no muestra progreso mientras dure ese paso, y se deja en paz mientras siga ejecutándose realmente.
- Una invocación secundaria que fue aceptada pero no se inició en 15 minutos se trata como si nunca se hubiera iniciado. Ese margen cubre la programación y la descarga de la imagen, no el trabajo propio de la macro.

Una invocación secundaria tratada de cualquiera de estas dos formas se detiene, su esquema temporal se elimina y el paso falla al final indicando esa invocación, el último estado que informó y cuándo lo informó.

**Las demás invocaciones secundarias no se ven afectadas.** Se ejecutan hasta el final y sus tablas de salida se escriben con normalidad, de modo que una invocación que no responde entre muchas no descarta el resto. Solo se nombran en el error las invocaciones que no pudieron completarse.

Si no se puede obtener respuesta a la propia comprobación (por ejemplo, mientras la plataforma no está disponible durante un breve período), la invocación secundaria se trata como si siguiera ejecutándose y se vuelve a comprobar en la pasada siguiente.

## Comportamiento al detener

Al detener el paso Macro Concurrent principal, se detienen todas las invocaciones secundarias activas de la macro y se elimina el esquema de cada ejecución activa. Las invocaciones secundarias que no se han iniciado no se inician después de detener el paso principal.

## Elementos relacionados

- [Crear una macro](/es/guides/workflows/create-a-macro/): declare un flujo de trabajo como macro y defina su contrato de puertos.
- [Macro Run](/es/reference/workflow-steps/workflow-control/run-macro/): invoque una macro una sola vez.
