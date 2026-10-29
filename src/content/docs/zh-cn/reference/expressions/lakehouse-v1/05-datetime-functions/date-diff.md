---
title: DATE DIFF（Lakehouse v1）
description: DATE DIFF——PlaidCloud Lakehouse 暂未提供 date_diff 函数，但支持对日期和时间直接进行算术运算。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse 暂未提供 `date_diff` 函数，但支持对日期和时间直接进行算术运算。例如，可以使用表达式 `TO_DATE(NOW())-2` 获得两天前的日期。

PlaidCloud Lakehouse 可直接操作日期和时间，使日期和时间计算既方便又灵活。示例如下：

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
