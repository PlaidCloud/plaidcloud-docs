---
title: DENSE_RANK (Lakehouse v1)
description: "DENSE_RANK: devuelve la posición de un valor dentro de un grupo de valores, sin saltos en las posiciones."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/dense-rank.md
---

Devuelve la posición de un valor dentro de un grupo de valores, sin saltos en las posiciones.

El valor de posición comienza en 1 y continúa de forma secuencial.

Si dos valores son iguales, tienen la misma posición.

## Sintaxis de Analyze

```python
func.dense_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Ejemplos de Analyze

```python
table.department, func.sum(salary), func.dense_rank().over(order_by=func.sum(table.salary).desc()).alias('dense_rank')

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
```

## Sintaxis de SQL

```sql
DENSE_RANK() OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ ASC | DESC ] [ <window_frame> ] )
```

## Ejemplos de SQL

**Cree la tabla**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Inserte los datos**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**Cálculo del salario total por departamento con DENSE_RANK**

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

Resultado:

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
