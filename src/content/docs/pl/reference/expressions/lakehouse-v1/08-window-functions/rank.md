---
title: RANK (Lakehouse v1)
description: RANK — przypisuje rangę każdej wartości w uporządkowanej grupie wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/rank.md
---

Funkcja RANK() przypisuje rangę każdej wartości w uporządkowanej grupie wartości.

Ranga zaczyna się od 1 i rośnie kolejno. Jeśli dwie wartości są takie same, mają tę samą rangę.

## Składnia Analyze

```python
func.rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

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

## Składnia SQL

```sql
RANK() OVER (
  [ PARTITION BY <expr1> ]
  ORDER BY <expr2> [ { ASC | DESC } ]
  [ <window_frame> ]
)
```

## Przykłady SQL

**Utwórz tabelę**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Wstaw dane**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**Ranking pracowników według wynagrodzenia**
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

Wynik:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 1           | John       | Doe       | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 3           | Mike       | Johnson   | IT         | 82000  | 3    |
| 4           | Sara       | Williams  | Sales      | 77000  | 4    |
| 5           | Tom        | Brown     | HR         | 75000  | 5    |
