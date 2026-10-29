---
title: GROUP_ARRAY_MOVING_AVG (Lakehouse v1)
description: GROUP_ARRAY_MOVING_AVG – die Funktion GROUP_ARRAY_MOVING_AVG berechnet den gleitenden Durchschnitt von Eingabewerten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-group-array-moving-avg.md
---

Die Funktion GROUP_ARRAY_MOVING_AVG berechnet den gleitenden Durchschnitt von Eingabewerten. Die Funktion kann die Fenstergröße als Parameter annehmen. Wird sie nicht angegeben, entspricht die Fenstergröße der Anzahl der Eingabewerte.

## Analyze-Syntax

```python
func.group_array_moving_avg(<expr1>)
```

## Analyze-Beispiele

```python
table.user_id, func.group_array_moving_avg(table.request_num).alias('avg_request_num')

| user_id | avg_request_num  |
|---------|------------------|
|       1 | [5.0,11.5,21.5]  |
|       3 | [10.0,22.5,35.0] |
|       2 | [7.5,18.0,31.0]  |
```

## SQL-Syntax

```sql
GROUP_ARRAY_MOVING_AVG(<expr>)

GROUP_ARRAY_MOVING_AVG(<window_size>)(<expr>)
```

## Argumente

| Argumente        | Beschreibung             |
|------------------| ------------------------ |
| `<window_size>`  | Beliebiger numerischer Ausdruck |
| `<expr>`         | Beliebiger numerischer Ausdruck |

## Rückgabetyp

Gibt ein Array mit Elementen vom Typ double oder decimal zurück, abhängig vom Datentyp der Quelle.

## SQL-Beispiele

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
