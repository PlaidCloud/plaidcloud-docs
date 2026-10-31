---
title: DATE DIFF (Lakehouse v1)
description: DATE DIFF — o PlaidCloud Lakehouse ainda não disponibiliza uma função date_diff, mas suporta operações aritméticas diretas com datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

O PlaidCloud Lakehouse ainda não disponibiliza uma função `date_diff`, mas suporta operações aritméticas diretas com datas e horas. Por exemplo, pode utilizar a expressão `TO_DATE(NOW())-2` para obter a data de há dois dias.

Esta flexibilidade na manipulação direta de datas e horas no PlaidCloud Lakehouse torna-o prático e versátil para cálculos de data e hora. Veja um exemplo abaixo:

```sql
CREATE TABLE tasks (
  task_name VARCHAR(50),
  start_date DATE,
  end_date DATE
);

INSERT INTO tasks (task_name, start_date, end_date)
VALUES
  ('Task 1', '2023-06-15', '2023-06-20'),
  ('Task 2', '2023-06-18', '2023-06-25'),
  ('Task 3', '2023-06-20', '2023-06-23');

SELECT task_name, end_date - start_date AS duration
FROM tasks;

task_name|duration|
---------+--------+
Task 1   |       5|
Task 2   |       7|
Task 3   |       3|
```
