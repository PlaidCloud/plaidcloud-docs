---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: GROUP_ARRAY_MOVING_AVG — funkcja GROUP_ARRAY_MOVING_AVG oblicza średnią kroczącą wartości wejściowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

Funkcja GROUP_ARRAY_MOVING_AVG oblicza średnią kroczącą wartości wejściowych. Funkcja może przyjąć rozmiar okna jako parametr. Jeśli go nie podano, rozmiar okna jest równy liczbie wartości wejściowych.

## Składnia Analyze

```python
func.group_array_moving_avg(<expr1>)
```

## Przykłady Analyze

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## Składnia SQL

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## Argumenty

| Argumenty        | Opis                     |
|------------------| ------------------------ |
| `<window_size>`  | Dowolne wyrażenie liczbowe |
| `<expr>`         | Dowolne wyrażenie liczbowe |

## Typ zwracany

Zwraca tablicę z elementami typu double lub decimal, w zależności od typu danych źródłowych.

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

SELECT user_id, GROUP_ARRAY_MOVING_AVG(2)(request_num) AS avg_request_num
FROM hits
GROUP BY user_id;

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```
