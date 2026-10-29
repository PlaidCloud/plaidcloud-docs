---
title: MIN_IF (Lakehouse v1)
description: MIN_IF：后缀 _IF 可以附加到任何聚合函数的名称之后。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

后缀 `_IF` 可以附加到任何聚合函数的名称之后。此时，聚合函数会接受一个额外的参数，即条件。

## Analyze 语法

```python
func.min_if(<column>, <cond>)
```

## Analyze 示例

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## SQL 语法

```sql
MIN_IF(<column>, <cond>)
```

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE project_budgets (
  id INT,
  project_id INT,
  department VARCHAR,
  budget FLOAT
);

INSERT INTO project_budgets (id, project_id, department, budget)
VALUES (1, 1, 'HR', 1000),
       (2, 1, 'IT', 2000),
       (3, 1, 'Marketing', 3000),
       (4, 2, 'HR', 1500),
       (5, 2, 'IT', 2500);
```

**查询演示：查找 IT 部门的最低预算**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**结果**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
