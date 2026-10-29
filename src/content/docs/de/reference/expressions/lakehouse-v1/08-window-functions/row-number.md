---
title: ROW_NUMBER (Lakehouse v1)
description: ROW_NUMBER — weist jeder Zeile innerhalb einer Partition eines Ergebnisses eine temporäre fortlaufende Nummer zu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/row-number.md
---

Weist jeder Zeile innerhalb einer Partition einer Ergebnismenge eine temporäre fortlaufende Nummer zu, beginnend bei 1 für die erste Zeile jeder Partition.

## Analyze-Syntax

```python
func.row_number().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
ROW_NUMBER() 
  OVER ( [ PARTITION BY <expr1> [, <expr2> ... ] ]
  ORDER BY <expr3> [ , <expr4> ... ] [ { ASC | DESC } ] )
```

| Parameter    | Erforderlich? | Beschreibung                                                                                               |
|--------------|---------------|------------------------------------------------------------------------------------------------------------|
| ORDER BY     | Ja            | Legt die Reihenfolge der Zeilen innerhalb jeder Partition fest.                                            |
| ASC / DESC   | Nein          | Legt die Sortierreihenfolge innerhalb jeder Partition fest. ASC (aufsteigend) ist der Standard.            |
| QUALIFY      | Nein          | Filtert Zeilen anhand von Bedingungen.                                                                     |

## SQL-Beispiele

Dieses Beispiel zeigt die Verwendung von ROW_NUMBER(), um Mitarbeitern innerhalb ihrer Abteilungen fortlaufende Nummern zuzuweisen, absteigend nach Gehalt geordnet.

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
