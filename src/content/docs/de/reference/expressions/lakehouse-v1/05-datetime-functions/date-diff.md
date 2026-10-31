---
title: DATE DIFF (Lakehouse v1)
description: DATE DIFF – PlaidCloud Lakehouse bietet noch keine Funktion date_diff, unterstützt aber direkte Arithmetik mit Datums- und Zeitwerten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse bietet noch keine Funktion `date_diff`, unterstützt aber direkte arithmetische Operationen mit Datums- und Zeitwerten. Mit dem Ausdruck `TO_DATE(NOW())-2` erhalten Sie beispielsweise das Datum von vor zwei Tagen.

Diese Möglichkeit, Datums- und Zeitwerte in PlaidCloud Lakehouse direkt zu bearbeiten, macht Datums- und Zeitberechnungen bequem und vielseitig. Ein Beispiel:

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
