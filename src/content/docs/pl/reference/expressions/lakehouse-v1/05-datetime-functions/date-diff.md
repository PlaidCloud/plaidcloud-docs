---
title: DATE DIFF (Lakehouse v1)
description: DATE DIFF — PlaidCloud Lakehouse nie udostępnia jeszcze funkcji date_diff, ale obsługuje bezpośrednie operacje arytmetyczne na datach i czasie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse nie udostępnia jeszcze funkcji `date_diff`, ale obsługuje bezpośrednie operacje arytmetyczne na datach i czasie. Na przykład możesz użyć wyrażenia `TO_DATE(NOW())-2`, aby uzyskać datę sprzed dwóch dni.

Możliwość bezpośredniego operowania na datach i czasie w PlaidCloud Lakehouse sprawia, że obliczenia na datach i czasie są wygodne i elastyczne. Poniżej znajduje się przykład:

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
