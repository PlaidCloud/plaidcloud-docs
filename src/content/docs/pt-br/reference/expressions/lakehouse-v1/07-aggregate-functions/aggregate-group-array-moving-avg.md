---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: GROUP_ARRAY_MOVING_AVG — a função GROUP_ARRAY_MOVING_AVG calcula a média móvel dos valores de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

A função GROUP_ARRAY_MOVING_AVG calcula a média móvel dos valores de entrada. A função pode receber o tamanho da janela como parâmetro. Se ele não for especificado, a função usa um tamanho de janela igual ao número de valores de entrada.

## Sintaxe do Analyze

```python
func.group_array_moving_avg(<expr1>)
```

## Exemplos do Analyze

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## Sintaxe SQL

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## Argumentos

| Argumentos       | Descrição                  |
|------------------| -------------------------- |
| `<window_size>`  | Qualquer expressão numérica |
| `<expr>`         | Qualquer expressão numérica |

## Tipo de retorno

Retorna um array com elementos do tipo double ou decimal, dependendo do tipo de dados de origem.

## Exemplos de SQL

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
