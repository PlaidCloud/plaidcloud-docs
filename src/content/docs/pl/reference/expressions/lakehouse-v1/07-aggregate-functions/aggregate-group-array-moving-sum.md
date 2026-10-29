---
title: GROUP_ARRAY_MOVING_SUM (Lakehouse v1)
description: GROUP_ARRAY_MOVING_SUM — funkcja GROUP_ARRAY_MOVING_SUM oblicza sumę kroczącą wartości wejściowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-sum.md
---

Funkcja GROUP_ARRAY_MOVING_SUM oblicza sumę kroczącą wartości wejściowych. Funkcja może przyjąć rozmiar okna jako parametr. Jeśli go nie podano, rozmiar okna jest równy liczbie wartości wejściowych.

## Składnia Analyze

```python
func.group_array_moving_sum(<expr>)
```

## Przykłady Analyze

```python
table.user_id, func.group_array_moving_sum(table.request_num)

| user_id | request_num |
|---------|-------------|
|       1 | [10,23,43]  |
|       2 | [20,45,70]  |
|       3 | [15,36,62]  |
```

## Składnia SQL

```sql
GROUP_ARRAY_MOVING_SUM(<expr>)

GROUP_ARRAY_MOVING_SUM(<window_size>)(<expr>)
```

## Argumenty

| Argumenty        | Opis                     |
|------------------| ------------------------ |
| `<window_size>`  | Dowolne wyrażenie liczbowe |
| `<expr>`         | Dowolne wyrażenie liczbowe |

## Typ zwracany

Zwraca tablicę z elementami tego samego typu co dane oryginalne.

## Przykłady SQL

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
