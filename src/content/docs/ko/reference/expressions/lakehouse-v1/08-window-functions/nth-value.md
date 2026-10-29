---
title: NTH_VALUE (Lakehouse v1)
description: NTH_VALUE — 정렬된 값 그룹에서 N번째 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/nth-value.md
---

정렬된 값 그룹에서 N번째 값을 반환합니다.

참고:

- [FIRST_VALUE](../first-value)
- [LAST_VALUE](../last-value)

## Analyze 구문

```python
func.nth_value(<expr>, <n>).over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 예제

```python
table.employee_id, table.first_name, table.last_name, table.salary, func.nth_value(table.first_name, 2).over(order_by=table.salary.desc()).alias('second_highest_salary_first_name')

employee_id | first_name | last_name | salary  | second_highest_salary_first_name
------------+------------+-----------+---------+----------------------------------
4           | Mary       | Williams  | 7000.00 | Jane
2           | Jane       | Smith     | 6000.00 | Jane
3           | David      | Johnson   | 5500.00 | Jane
1           | John       | Doe       | 5000.00 | Jane
5           | Michael    | Brown     | 4500.00 | Jane
```

## SQL 구문

```sql
NTH_VALUE(expression, n) OVER ([PARTITION BY partition_expression] ORDER BY order_expression [window_frame])
```

윈도 프레임 구문은 [윈도 프레임 구문](..#윈도우-프레임-구문)을 참조하십시오.

## SQL 예제

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

-- Use NTH_VALUE to retrieve the first name of the employee with the second highest salary
SELECT employee_id, first_name, last_name, salary,
       NTH_VALUE(first_name, 2) OVER (ORDER BY salary DESC) AS second_highest_salary_first_name
FROM employees;

employee_id | first_name | last_name | salary  | second_highest_salary_first_name
------------+------------+-----------+---------+----------------------------------
4           | Mary       | Williams  | 7000.00 | Jane
2           | Jane       | Smith     | 6000.00 | Jane
3           | David      | Johnson   | 5500.00 | Jane
1           | John       | Doe       | 5000.00 | Jane
5           | Michael    | Brown     | 4500.00 | Jane
```
