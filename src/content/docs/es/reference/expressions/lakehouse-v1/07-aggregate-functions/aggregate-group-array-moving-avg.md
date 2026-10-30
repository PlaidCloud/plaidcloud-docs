---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: "GROUP_ARRAY_MOVING_AVG: la función GROUP_ARRAY_MOVING_AVG calcula el promedio móvil de los valores de entrada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

La función GROUP_ARRAY_MOVING_AVG calcula el promedio móvil de los valores de entrada. La función puede recibir el tamaño de la ventana como parámetro. Si no se especifica, la función toma un tamaño de ventana igual al número de valores de entrada.

## Sintaxis de Analyze

```python
func.group_array_moving_avg(<expr1>)
```

## Ejemplos de Analyze

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## Sintaxis de SQL

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## Argumentos

| Argumentos        | Descripción              |
|------------------| ------------------------ |
| `<window_size>`  | Cualquier expresión numérica |
| `<expr>`         | Cualquier expresión numérica |

## Tipo de valor devuelto

Devuelve una matriz con elementos de tipo double o decimal, según el tipo de datos de origen.

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

SELECT user_id, GROUP_ARRAY_MOVING_AVG(2)(request_num) AS avg_request_num
FROM hits
GROUP BY user_id;

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```
