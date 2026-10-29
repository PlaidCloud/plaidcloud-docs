---
title: AVG_IF (Lakehouse v1)
description: AVG_IF：后缀 -If 可以附加到任何聚合函数的名称之后。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

后缀 -If 可以附加到任何聚合函数的名称之后。此时，聚合函数会接受一个额外的参数，即条件。

## Analyze 语法

```python
func.avg_if(<column>, <cond>)
```

## Analyze 示例

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## SQL 语法
```sql
AVG_IF(<column>, <cond>)
```

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE employees (
  id INT,
  salary INT,
  department VARCHAR
);

INSERT INTO employees (id, salary, department)
VALUES (1, 50000, 'HR'),
       (2, 60000, 'IT'),
       (3, 55000, 'HR'),
       (4, 70000, 'IT'),
       (5, 65000, 'IT');
```

**查询演示：计算 IT 部门的平均薪资**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**结果**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
