---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — insère une valeur dans un tableau JSON à l'index spécifié et renvoie le tableau JSON mis à jour.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

Insère une valeur dans un tableau JSON à l'index spécifié et renvoie le tableau JSON mis à jour.

## Syntaxe SQL

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| Paramètre      | Description                                                                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | Le tableau JSON à modifier.                                                                                                                                                                              |
| `<index>`      | La position à laquelle la valeur sera insérée. Un index positif insère à la position indiquée, ou ajoute à la fin s'il dépasse la taille du tableau ; un index négatif insère à partir de la fin, ou au début s'il dépasse la taille du tableau. |
| `<json_value>` | La valeur JSON à insérer dans le tableau.                                                                                                                                                                |

## Type de retour

Tableau JSON.

## Exemples SQL

Lorsque `<index>` est un entier positif ou nul, le nouvel élément est inséré à la position indiquée et les éléments existants sont décalés vers la droite.

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

Un `<index>` négatif se compte à partir de la fin du tableau : `-1` représente la position située avant le dernier élément, `-2` celle située avant l'avant-dernier, et ainsi de suite.

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
