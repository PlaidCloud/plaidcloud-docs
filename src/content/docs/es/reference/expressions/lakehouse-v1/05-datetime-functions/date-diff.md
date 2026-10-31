---
title: DATE DIFF (Lakehouse v1)
description: DATE DIFF — PlaidCloud Lakehouse aún no ofrece una función date_diff, pero admite operaciones aritméticas directas con fechas y horas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse aún no ofrece una función `date_diff`, pero admite operaciones aritméticas directas con fechas y horas. Por ejemplo, puede usar la expresión `TO_DATE(NOW())-2` para obtener la fecha de hace dos días.

Esta flexibilidad para manipular fechas y horas directamente en PlaidCloud Lakehouse lo hace cómodo y versátil para los cálculos de fecha y hora. Vea un ejemplo a continuación:

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
