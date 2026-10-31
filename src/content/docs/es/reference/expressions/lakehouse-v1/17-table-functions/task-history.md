---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY muestra el historial de ejecución de tareas según las variables dadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Muestra el historial de ejecución de tareas según las variables dadas.

## Sintaxis de SQL
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## Argumentos

Todos los argumentos son opcionales.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

Intervalo de tiempo (en formato TIMESTAMP_LTZ), dentro de los últimos 7 días, en el que se programó la ejecución de la tarea. Si el intervalo de tiempo no está dentro de los últimos 7 días, se devuelve un error.

* Si no se especifica `SCHEDULED_TIME_RANGE_END`, la función devuelve las tareas que ya se completaron, que se están ejecutando actualmente o que están programadas para el futuro.
* Si `SCHEDULED_TIME_RANGE_END` es CURRENT_TIMESTAMP, la función devuelve las tareas que ya se completaron o que se están ejecutando actualmente. Tenga en cuenta que una tarea que se ejecuta justo antes de la hora actual aún podría identificarse como programada.
* Para consultar solo las tareas que ya se completaron o que se están ejecutando actualmente, incluya `WHERE query_id IS NOT NULL` como filtro. La columna QUERY_ID de la salida de TASK_HISTORY solo se rellena cuando una tarea ha comenzado a ejecutarse.

Si no se especifica una hora de inicio ni de fin, se devuelven las tareas más recientes, hasta el valor RESULT_LIMIT especificado.

`RESULT_LIMIT => <integer>`

Un número que especifica la cantidad máxima de filas que devuelve la función.

Si el número de filas coincidentes es mayor que este límite, se devuelven las ejecuciones de tareas con la marca de tiempo más reciente, hasta el límite especificado.

Intervalo: de `1` a `10000`

Valor predeterminado: `100`.

`TASK_NAME => <string>`

Una cadena que no distingue mayúsculas de minúsculas y que especifica una tarea. Solo se admiten nombres de tarea no calificados. Solo se devuelven las ejecuciones de la tarea especificada. Tenga en cuenta que, si varias tareas tienen el mismo nombre, la función devuelve el historial de cada una de ellas.

`ERROR_ONLY => { TRUE | FALSE }`

Si se establece en TRUE, esta función devuelve solo las ejecuciones de tareas que fallaron o se cancelaron.

`ROOT_TASK_ID => <string>`

Identificador único de la tarea raíz de un grafo de tareas. Este ID coincide con el valor de la columna ID en la salida de SHOW TASKS para la misma tarea. Especifique ROOT_TASK_ID para mostrar el historial de la tarea raíz y de las tareas secundarias que forman parte del grafo de tareas.

## Notas de uso
* Esta función devuelve un máximo de 10 000 filas, establecido en el valor del argumento RESULT_LIMIT. El valor predeterminado es 100.
* Esta función devuelve resultados solo para el rol ACCOUNTADMIN.


## Ejemplos de SQL

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
La consulta SQL anterior recupera todos los registros del historial de tareas de la función TASK_HISTORY, ordenados por la columna scheduled_time (máximo 10 000).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

La consulta SQL anterior recupera todos los registros del historial de tareas de la función TASK_HISTORY cuyo intervalo de tiempo programado comienza en '2022-01-02T01:12:00-07:00' y termina en '2022-01-02T01:12:30-07:00'. Esto significa que devolverá las tareas que estaban programadas para ejecutarse dentro de esa ventana específica de 30 segundos. El resultado incluirá los detalles de las tareas que cumplen estos criterios.
