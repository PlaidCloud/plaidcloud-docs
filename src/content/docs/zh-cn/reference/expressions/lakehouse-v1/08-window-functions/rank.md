---
title: RANK（Lakehouse v1）
description: RANK — 为有序值组中的每个值分配排名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/rank.md
---

RANK() 函数为有序值组中的每个值分配一个排名。

排名从 1 开始依次递增。如果两个值相同，则它们的排名相同。

## Analyze 语法

```python
func.rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 示例

```python
table.employee_id, table.first_name, table.last_name, table.department, table.salary, func.rank().over(order_by=table.salary).alias('rank')

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 1           | John       | Doe       | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 3           | Mike       | Johnson   | IT         | 82000  | 3    |
| 4           | Sara       | Williams  | Sales      | 77000  | 4    |
| 5           | Tom        | Brown     | HR         | 75000  | 5    |
```

## SQL 语法

```sql
RANK() OVER (
  [ PARTITION BY <expr1> ]
  ORDER BY <expr2> [ { ASC | DESC } ]
  [ <window_frame> ]
)
```

## SQL 示例

**创建表**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**插入数据**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**按薪资对员工排名**
```sql
SELECT
  employee_id,
  first_name,
  last_name,
  department,
  salary,
  RANK() OVER (ORDER BY salary DESC) AS rank
FROM
  employees;
```

结果：

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 1           | John       | Doe       | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 3           | Mike       | Johnson   | IT         | 82000  | 3    |
| 4           | Sara       | Williams  | Sales      | 77000  | 4    |
| 5           | Tom        | Brown     | HR         | 75000  | 5    |
