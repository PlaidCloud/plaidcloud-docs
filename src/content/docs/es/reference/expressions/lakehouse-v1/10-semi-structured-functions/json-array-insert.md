---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — inserta un valor en un arreglo JSON en el índice especificado y devuelve el arreglo JSON actualizado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

Inserta un valor en un arreglo JSON en el índice especificado y devuelve el arreglo JSON actualizado.

## Sintaxis SQL

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| Parámetro      | Descripción                                                                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | El arreglo JSON que se modificará.                                                                                                                                                                       |
| `<index>`      | La posición en la que se insertará el valor. Los índices positivos insertan en la posición especificada o agregan al final si están fuera de rango; los índices negativos insertan desde el final o al principio si están fuera de rango. |
| `<json_value>` | El valor JSON que se insertará en el arreglo.                                                                                                                                                            |

## Tipo de retorno

Arreglo JSON.

## Ejemplos de SQL

Cuando `<index>` es un entero no negativo, el nuevo elemento se inserta en la posición especificada y los elementos existentes se desplazan hacia la derecha.

```sql
-- The new element is inserted at position 0 (the beginning of the array), shifting all original elements to the right
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]

-- The new element is inserted at position 1, between task1 and task2
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT): ["task1","new_task","task2","task3"]

-- If the index exceeds the length of the array, the new element is appended at the end of the array
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT): ["task1","task2","task3","new_task"]
```

Un `<index>` negativo cuenta desde el final del arreglo: `-1` representa la posición anterior al último elemento, `-2` la anterior al penúltimo, y así sucesivamente.

```sql
-- The new element is inserted just before the last element (task3)
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 1, '"new_task"'::VARIANT): ["task1","task2","new_task","task3"]

-- Since the negative index exceeds the array’s length, the new element is inserted at the beginning
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 6, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]
```
