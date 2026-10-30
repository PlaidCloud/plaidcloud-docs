---
title: FIRST_VALUE (Lakehouse v1)
description: FIRST_VALUE：返回一组有序值中的第一个值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/first-value.md
---

返回一组有序值中的第一个值。

另请参阅：

- [LAST_VALUE](../last-value)
- [NTH_VALUE](../nth-value)

## Analyze 语法

```python
func.first_value(<expr>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 示例

```python
table.employee_id, table.first_name, table.last_name, table.salary, func.first_value(table.first_name).over(order_by=table.salary.desc()).alias('highest_salary_first_name')

employee_id | first_name | last_name | salary  | highest_salary_first_name
------------+------------+-----------+---------+--------------------------
4           | Mary       | Williams  | 7000.00 | Mary
2           | Jane       | Smith     | 6000.00 | Mary
3           | David      | Johnson   | 5500.00 | Mary
1           | John       | Doe       | 5000.00 | Mary
5           | Michael    | Brown     | 4500.00 | Mary
```

## SQL 语法

```sql
FIRST_VALUE(expression) OVER ([PARTITION BY partition_expression] ORDER BY order_expression [window_frame])
```

窗口框架的语法请参阅[窗口框架语法](..#窗口框架语法)。

## SQL 示例

```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  salary DECIMAL(10,2)
);

INSERT INTO employees (employee_id, first_name, last_name, salary)
VALUES
  (1, 'John', 'Doe', 5000.00),
  (2, 'Jane', 'Smith', 6000.00),
  (3, 'David', 'Johnson', 5500.00),
  (4, 'Mary', 'Williams', 7000.00),
  (5, 'Michael', 'Brown', 4500.00);

-- Use FIRST_VALUE to retrieve the first name of the employee with the highest salary
SELECT employee_id, first_name, last_name, salary,
       FIRST_VALUE(first_name) OVER (ORDER BY salary DESC) AS highest_salary_first_name
FROM employees;


employee_id | first_name | last_name | salary  | highest_salary_first_name
------------+------------+-----------+---------+--------------------------
4           | Mary       | Williams  | 7000.00 | Mary
2           | Jane       | Smith     | 6000.00 | Mary
3           | David      | Johnson   | 5500.00 | Mary
1           | John       | Doe       | 5000.00 | Mary
5           | Michael    | Brown     | 4500.00 | Mary
```
