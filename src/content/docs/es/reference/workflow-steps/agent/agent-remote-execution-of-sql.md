---
title: Agent Remote Execution of SQL
description: Ejecute consultas SQL de forma remota mediante un agente de PlaidLink en los flujos de trabajo de PlaidCloud para realizar operaciones de base de datos seguras detrás de cortafuegos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Descripción

Ejecuta SQL en una base de datos a la que PlaidCloud solo puede acceder mediante un agente de PlaidLink, normalmente porque la base de datos está detrás de un cortafuegos, en una red privada o en un centro de datos local. El agente ejecuta el SQL localmente e informa a PlaidCloud del éxito o del fallo.

Úselo para activar procedimientos almacenados remotos, rutinas de actualización o trabajos de mantenimiento como parte de un flujo de trabajo de PlaidCloud sin exponer la base de datos de origen a Internet.

## Ejecutar una instrucción una vez por fila

El paso **Ejecución remota: SQL**, que se conecta directamente a la base de datos en lugar de hacerlo mediante un agente, puede ejecutar su instrucción una vez por cada fila de una tabla, por ejemplo para llamar a un procedimiento almacenado por cada fila de entrada. Establezca **Ejecutar el SQL** en **Una vez por fila**, elija una **Tabla de inductores** y complete **Parámetros**. Escriba cada valor de la instrucción como un marcador de posición `:name`, como `CALL load_region(:region, :period)`, y asigne cada marcador de posición en **Parámetro** a la **Columna de inductor** que lo proporciona. Cada valor se envía a la base de datos como un parámetro enlazado, nunca pegado en el texto de la instrucción.

Cada parámetro necesita un nombre y una columna de inductor, y un parámetro no puede aparecer dos veces en la lista. El formulario muestra una advertencia cuando un `:name` de la instrucción no tiene asignación o cuando una asignación no figura en la instrucción. La tabla de inductores debe ser una tabla, no una vista. Una tabla de inductores sin filas termina con una advertencia y no ejecuta nada, y una con más de 100 000 filas hace fallar el paso sin ejecutar ninguna de ellas, así que fíltrela primero.

## Ejecutar un script en una transacción

En el paso **Ejecución remota: SQL**, marque **Ejecutar el SQL como un script de instrucciones en una transacción: se aplican todas o ninguna** (`transaction`) para ejecutar el SQL como un script de instrucciones, una tras otra, en una sola transacción, de modo que se aplican todas las instrucciones o ninguna.
