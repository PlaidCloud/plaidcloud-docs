---
title: Paso Agent Remote Execution of SQL
description: Ejecute consultas SQL de forma remota mediante un agente PlaidLink en los flujos de trabajo de PlaidCloud para realizar operaciones seguras en bases de datos protegidas por cortafuegos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Descripción

Ejecuta SQL en una base de datos a la que PlaidCloud solo puede llegar a través de un agente PlaidLink, normalmente porque la base de datos está detrás de un cortafuegos, en una red privada o en un centro de datos local. El agente ejecuta el SQL localmente e informa a PlaidCloud del éxito o el fallo.

Úselo para activar procedimientos almacenados remotos, rutinas de actualización o trabajos de mantenimiento como parte de un flujo de trabajo de PlaidCloud sin exponer la base de datos de origen a internet público.

## Vista previa de la consulta

En el paso **Ejecución remota: SQL**, **Vista previa** en la pestaña **Origen** muestra hasta 100 filas sin ejecutar la instrucción, de modo que pueda comprobar un `SELECT` antes de ejecutarlo. La vista previa rellena las variables de la misma manera que una ejecución, pero no admite formatos de variable como `{x:>9}`. Solo lee datos: una instrucción que escribe, o una función que la vista previa no puede comprobar como de solo lectura, se rechaza con *La vista previa solo admite funciones SQL estándar. Ejecute el paso para ver los resultados.* La vista previa no está disponible en un proyecto bloqueado ni para instrucciones que usan marcadores de posición `:name` con una tabla de inductores. No está disponible para el paso basado en agente que describe esta página, porque solo el agente puede llegar a esas bases de datos.

## Ejecutar una instrucción una vez por fila

El paso **Ejecución remota: SQL**, que se conecta a la base de datos directamente en lugar de a través de un agente, puede ejecutar su instrucción una vez por cada fila de una tabla, por ejemplo para llamar a un procedimiento almacenado por cada fila de entrada. Establezca **Ejecutar el SQL** en **Una vez por fila**, elija una **Tabla de inductores** y complete **Parámetros**. Escriba cada valor de la instrucción como un marcador de posición `:name`, como `CALL load_region(:region, :period)`, y asigne cada marcador de posición en **Parámetro** a la **Columna de inductor** que lo proporciona. Cada valor se envía a la base de datos como un parámetro enlazado, nunca pegado en el texto de la instrucción.

Cada parámetro necesita un nombre y una columna de inductor, y un parámetro no puede aparecer dos veces en la lista. El formulario avisa cuando un `:name` de la instrucción no tiene asignación o cuando una asignación no está en la instrucción. La tabla de inductores debe ser una tabla, no una vista. Una tabla de inductores sin filas termina con una advertencia y no ejecuta nada, y una con más de 100 000 filas hace fallar el paso sin ejecutar ninguna de ellas, así que fíltrela primero.

## Ejecutar un script en una sola transacción

En el paso **Ejecución remota: SQL**, marque **Ejecutar el SQL como un script de instrucciones en una transacción: se aplican todas o ninguna** (`transaction`) para ejecutar el SQL como un script de instrucciones, una tras otra, en una única transacción, de modo que se aplican todas las instrucciones o ninguna.
