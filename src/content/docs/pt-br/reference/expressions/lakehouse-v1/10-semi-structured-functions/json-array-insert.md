---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — insere um valor em um array JSON no índice especificado e retorna o array JSON atualizado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

Insere um valor em um array JSON no índice especificado e retorna o array JSON atualizado.

## Sintaxe SQL

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| Parâmetro      | Descrição                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | O array JSON a ser modificado.                                                                                                                                                                           |
| `<index>`      | A posição em que o valor será inserido. Índices positivos inserem na posição especificada ou acrescentam ao final se estiverem fora do intervalo; índices negativos inserem a partir do final ou no início se estiverem fora do intervalo. |
| `<json_value>` | O valor JSON a ser inserido no array.                                                                                                                                                                    |

## Tipo de retorno

Array JSON.

## Exemplos de SQL

Quando `<index>` é um inteiro não negativo, o novo elemento é inserido na posição especificada e os elementos existentes são deslocados para a direita.

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

Um `<index>` negativo conta a partir do final do array, em que `-1` representa a posição antes do último elemento, `-2` antes do penúltimo, e assim por diante.

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
