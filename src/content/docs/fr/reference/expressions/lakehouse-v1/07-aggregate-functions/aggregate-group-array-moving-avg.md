---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: "GROUP_ARRAY_MOVING_AVG : la fonction GROUP_ARRAY_MOVING_AVG calcule la moyenne mobile des valeurs d'entrée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

La fonction GROUP_ARRAY_MOVING_AVG calcule la moyenne mobile des valeurs d'entrée. La fonction peut prendre la taille de la fenêtre en paramètre. Si elle n'est pas spécifiée, la taille de la fenêtre est égale au nombre de valeurs d'entrée.

## Syntaxe Analyze

```python
func.group_array_moving_avg(<expr1>)
```

## Exemples Analyze

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## Syntaxe SQL

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## Arguments

| Arguments        | Description              |
|------------------| ------------------------ |
| `<window_size>`  | Toute expression numérique |
| `<expr>`         | Toute expression numérique |

## Type de retour

Renvoie un tableau dont les éléments sont de type double ou decimal selon le type des données sources.

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

SELECT user_id, GROUP_ARRAY_MOVING_AVG(2)(request_num) AS avg_request_num
FROM hits
GROUP BY user_id;

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```
