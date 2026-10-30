---
title: GROUP_ARRAY_MOVING_SUM (Lakehouse v1)
description: GROUP_ARRAY_MOVING_SUM — a função GROUP_ARRAY_MOVING_SUM calcula a soma móvel dos valores de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-sum.md
---

A função GROUP_ARRAY_MOVING_SUM calcula a soma móvel dos valores de entrada. A função pode receber a dimensão da janela como parâmetro. Se não for especificada, a função utiliza uma dimensão da janela igual ao número de valores de entrada.

## Sintaxe do Analyze

```python
func.group_array_moving_sum(<expr>)
```

## Exemplos do Analyze

```python
table.user_id, func.group_array_moving_sum(table.request_num)

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```

## Sintaxe SQL

```sql
GROUP_ARRAY_MOVING_SUM(<expr>)

GROUP_ARRAY_MOVING_SUM(<window_size>)(<expr>)
```

## Argumentos

| Argumentos       | Descrição                |
|------------------| ------------------------ |
| `<window_size>`  | Qualquer expressão numérica |
| `<expr>`         | Qualquer expressão numérica |

## Tipo de retorno

Devolve uma matriz com elementos do mesmo tipo que os dados originais.

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

SELECT user_id, GROUP_ARRAY_MOVING_SUM(2)(request_num) AS request_num
FROM hits
GROUP BY user_id;

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```
