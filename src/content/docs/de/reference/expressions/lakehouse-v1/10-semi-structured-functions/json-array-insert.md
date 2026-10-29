---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — Fügt einen Wert am angegebenen Index in ein JSON-Array ein und gibt das aktualisierte JSON-Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

Fügt einen Wert am angegebenen Index in ein JSON-Array ein und gibt das aktualisierte JSON-Array zurück.

## SQL Syntax

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| Parameter      | Beschreibung |
|----------------|--------------|
| `<json_array>` | Das JSON-Array, das geändert werden soll. |
| `<index>`      | Die Position, an der der Wert eingefügt wird. Positive Indizes fügen an der angegebenen Position ein oder hängen an, wenn der Index außerhalb des Bereichs liegt. Negative Indizes fügen vom Ende aus gezählt ein oder am Anfang, wenn der Index außerhalb des Bereichs liegt. |
| `<json_value>` | Der JSON-Wert, der in das Array eingefügt wird. |

## Return Type

JSON-Array.

## SQL Examples

Ist `<index>` eine nicht negative Ganzzahl, wird das neue Element an der angegebenen Position eingefügt, und die vorhandenen Elemente rücken nach rechts.

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

Ein negativer `<index>` zählt vom Ende des Arrays aus: `-1` steht für die Position vor dem letzten Element, `-2` für die Position vor dem vorletzten Element und so weiter.

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
