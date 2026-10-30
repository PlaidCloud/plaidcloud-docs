---
title: LAST_VALUE (Lakehouse v1)
description: LAST_VALUE — zwraca ostatnią wartość z uporządkowanej grupy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/last-value.md
---

Zwraca ostatnią wartość z uporządkowanej grupy wartości.

Zobacz też:

- [FIRST_VALUE](../first-value)
- [NTH_VALUE](../nth-value)

## Składnia Analyze

```python
func.last_value(<expr>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

```python
table.employee_id, table.first_name, table.last_name, table.salary, func.last_value(table.first_name).over(order_by=table.salary.desc()).alias('lowest_salary_first_name')

employee_id | first_name | last_name | salary  | lowest_salary_first_name
------------+------------+-----------+---------+------------------------
4           | Mary       | Williams  | 7000.00 | Michael
2           | Jane       | Smith     | 6000.00 | Michael
3           | David      | Johnson   | 5500.00 | Michael
1           | John       | Doe       | 5000.00 | Michael
5           | Michael    | Brown     | 4500.00 | Michael
```

## Składnia SQL

```sql
LAST_VALUE(expression) OVER ([PARTITION BY partition_expression] ORDER BY order_expression [window_frame])
```

Składnię ramki okna znajdziesz w sekcji [Składnia ramki okna](..#składnia-ramki-okna).

## Przykłady SQL

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

-- Use LAST_VALUE to retrieve the first name of the employee with the lowest salary
SELECT employee_id, first_name, last_name, salary,
       LAST_VALUE(first_name) OVER (ORDER BY salary DESC) AS lowest_salary_first_name
FROM employees;

employee_id | first_name | last_name | salary  | lowest_salary_first_name
------------+------------+-----------+---------+------------------------
4           | Mary       | Williams  | 7000.00 | Michael
2           | Jane       | Smith     | 6000.00 | Michael
3           | David      | Johnson   | 5500.00 | Michael
1           | John       | Doe       | 5000.00 | Michael
5           | Michael    | Brown     | 4500.00 | Michael
```
