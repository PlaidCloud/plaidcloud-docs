---
title: DATE DIFF（Lakehouse v1）
description: DATE DIFF — PlaidCloud Lakehouse には date_diff 関数はまだありませんが、日付と時刻に対する直接的な算術演算をサポートしています。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse には `date_diff` 関数はまだありませんが、日付と時刻に対する直接的な算術演算をサポートしています。たとえば、式 `TO_DATE(NOW())-2` を使用すると、2 日前の日付を取得できます。

PlaidCloud Lakehouse では日付と時刻を直接操作できるため、日付と時刻の計算を便利かつ柔軟に扱えます。例を次に示します。

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
