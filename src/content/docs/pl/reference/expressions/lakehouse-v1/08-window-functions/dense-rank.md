---
title: DENSE_RANK (Lakehouse v1)
description: DENSE_RANK — zwraca pozycję wartości w grupie wartości, bez luk w pozycjach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/dense-rank.md
---

Zwraca pozycję wartości w grupie wartości, bez luk w pozycjach.

Pozycja zaczyna się od 1 i rośnie kolejno.

Jeśli dwie wartości są takie same, mają tę samą pozycję.

## Składnia Analyze

```python
func.dense_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Przykłady Analyze

```python
table.department, func.sum(salary), func.dense_rank().over(order_by=func.sum(table.salary).desc()).alias('dense_rank')

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
```

## Składnia SQL

```sql
DENSE_RANK() OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ ASC | DESC ] [ <window_frame> ] )
```

## Przykłady SQL

**Tworzenie tabeli**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Wstawianie danych**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**Obliczanie łącznego wynagrodzenia w każdym dziale za pomocą DENSE_RANK**

```sql
SELECT
    department,
    SUM(salary) AS total_salary,
    DENSE_RANK() OVER (ORDER BY SUM(salary) DESC) AS dense_rank
FROM
    employees
GROUP BY
    department;
```

Wynik:

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
