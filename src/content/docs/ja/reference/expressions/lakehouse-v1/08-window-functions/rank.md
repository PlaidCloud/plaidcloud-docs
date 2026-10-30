---
title: RANK（Lakehouse v1）
description: RANK — 順序付けされた値のグループ内の各値に順位を割り当てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/rank.md
---

RANK()関数は、順序付けされた値のグループ内の各値に順位を割り当てます。

順位の値は1から始まり、順番に増えていきます。2つの値が同じ場合は、同じ順位になります。

## Analyze Syntax

```python
func.rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze Examples

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

## SQL Syntax

```sql
RANK() OVER (
  [ PARTITION BY <expr1> ]
  ORDER BY <expr2> [ { ASC | DESC } ]
  [ <window_frame> ]
)
```

## SQL Examples

**テーブルを作成する**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**データを挿入する**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**給与で従業員の順位を付ける**
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

結果:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 1           | John       | Doe       | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 3           | Mike       | Johnson   | IT         | 82000  | 3    |
| 4           | Sara       | Williams  | Sales      | 77000  | 4    |
| 5           | Tom        | Brown     | HR         | 75000  | 5    |
