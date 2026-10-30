---
title: GROUP_ARRAY_MOVING_SUM (Lakehouse v1)
description: "GROUP_ARRAY_MOVING_SUM : la fonction GROUP_ARRAY_MOVING_SUM calcule la somme mobile des valeurs d'entrée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-sum.md
---

La fonction GROUP_ARRAY_MOVING_SUM calcule la somme mobile des valeurs d'entrée. La fonction peut prendre la taille de la fenêtre en paramètre. Si elle n'est pas spécifiée, la taille de la fenêtre est égale au nombre de valeurs d'entrée.

## Syntaxe Analyze

```python
func.group_array_moving_sum(<expr>)
```

## Exemples Analyze

```python
table.user_id, func.group_array_moving_sum(table.request_num)

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```

## Syntaxe SQL

```sql
GROUP_ARRAY_MOVING_SUM(<expr>)

GROUP_ARRAY_MOVING_SUM(<window_size>)(<expr>)
```

## Arguments

| Arguments        | Description              |
|------------------| ------------------------ |
| `<window_size>`  | Toute expression numérique |
| `<expr>`         | Toute expression numérique |

## Type de retour

Renvoie un tableau dont les éléments sont du même type que les données d'origine.

## Exemples SQL

```sql
-- Create a table and insert sample data
CREATE TABLE hits (
  user_id INT,
  request_num INT
);

INSERT INTO hits (user_id, request_num)
VALUES (1, 10),
       (2, 15),
       (3, 20),
       (1, 13),
       (2, 21),
       (3, 25),
       (1, 30),
       (2, 41),
       (3, 45);

SELECT user_id, GROUP_ARRAY_MOVING_SUM(2)(request_num) AS request_num
FROM hits
GROUP BY user_id;

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```
