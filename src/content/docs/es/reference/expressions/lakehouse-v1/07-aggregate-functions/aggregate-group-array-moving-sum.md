---
title: GROUP_ARRAY_MOVING_SUM (Lakehouse v1)
description: "GROUP_ARRAY_MOVING_SUM: la función GROUP_ARRAY_MOVING_SUM calcula la suma móvil de los valores de entrada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-sum.md
---

La función GROUP_ARRAY_MOVING_SUM calcula la suma móvil de los valores de entrada. La función puede recibir el tamaño de la ventana como parámetro. Si no se especifica, la función toma un tamaño de ventana igual al número de valores de entrada.

## Sintaxis de Analyze

```python
func.group_array_moving_sum(<expr>)
```

## Ejemplos de Analyze

```python
table.user_id, func.group_array_moving_sum(table.request_num)

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```

## Sintaxis de SQL

```sql
GROUP_ARRAY_MOVING_SUM(<expr>)

GROUP_ARRAY_MOVING_SUM(<window_size>)(<expr>)
```

## Argumentos

| Argumentos        | Descripción              |
|------------------| ------------------------ |
| `<window_size>`  | Cualquier expresión numérica |
| `<expr>`         | Cualquier expresión numérica |

## Tipo de valor devuelto

Devuelve una matriz con elementos del mismo tipo que los datos originales.

## Ejemplos de SQL

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
