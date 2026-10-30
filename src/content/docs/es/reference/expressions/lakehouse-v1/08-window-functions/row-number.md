---
title: ROW_NUMBER (Lakehouse v1)
description: ROW_NUMBER — asigna un número secuencial temporal a cada fila dentro de una partición de un resultado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/row-number.md
---

Asigna un número secuencial temporal a cada fila dentro de una partición de un conjunto de resultados, empezando en 1 para la primera fila de cada partición. 

## Sintaxis de Analyze

```python
func.row_number().over(partition_by=[<columns>], order_by=[<columns>])
```

## Ejemplos de Analyze

```python
table.employee_id, table.first_name, table.last_name, table.department, table.salary, func.row_number().over(partition=table.department, order_by=table.salary).alias('row_num')

┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   employee_id   │    first_name    │     last_name    │    department    │      salary     │ row_num │
├─────────────────┼──────────────────┼──────────────────┼──────────────────┼─────────────────┼─────────┤
│               2 │ Jane             │ Smith            │ HR               │           85000 │       1 │
│               5 │ Tom              │ Brown            │ HR               │           75000 │       2 │
│               1 │ John             │ Doe              │ IT               │           90000 │       1 │
│               3 │ Mike             │ Johnson          │ IT               │           82000 │       2 │
│               4 │ Sara             │ Williams         │ Sales            │           77000 │       1 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ROW_NUMBER() 
  OVER ( [ PARTITION BY <expr1> [, <expr2> ... ] ]
  ORDER BY <expr3> [ , <expr4> ... ] [ { ASC | DESC } ] )
```

| Parámetro    | ¿Obligatorio? | Descripción                                                                                                |
|--------------|-----------|------------------------------------------------------------------------------------------------------------|
| ORDER BY     | Sí       | Especifica el orden de las filas dentro de cada partición.                                                         |
| ASC / DESC   | No        | Especifica el orden de clasificación dentro de cada partición. ASC (ascendente) es el valor predeterminado.                         |
| QUALIFY      | No        | Filtra las filas según condiciones.                                                                          |

## Ejemplos de SQL

Este ejemplo muestra el uso de ROW_NUMBER() para asignar números secuenciales a los empleados dentro de sus departamentos, ordenados por salario descendente.

```sql
-- Prepare the data
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);

INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);

-- Select employee details along with the row number partitioned by department and ordered by salary in descending order.
SELECT
    employee_id,
    first_name,
    last_name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM
    employees;

┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   employee_id   │    first_name    │     last_name    │    department    │      salary     │ row_num │
├─────────────────┼──────────────────┼──────────────────┼──────────────────┼─────────────────┼─────────┤
│               2 │ Jane             │ Smith            │ HR               │           85000 │       1 │
│               5 │ Tom              │ Brown            │ HR               │           75000 │       2 │
│               1 │ John             │ Doe              │ IT               │           90000 │       1 │
│               3 │ Mike             │ Johnson          │ IT               │           82000 │       2 │
│               4 │ Sara             │ Williams         │ Sales            │           77000 │       1 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
