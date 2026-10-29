---
title: RANK (Lakehouse v1)
description: RANK — atribui uma classificação a cada valor dentro de um grupo ordenado de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/rank.md
---

A função RANK() atribui uma classificação a cada valor dentro de um grupo ordenado de valores.

O valor da classificação começa em 1 e continua sequencialmente. Se dois valores forem iguais, têm a mesma classificação.

## Sintaxe do Analyze

```python
func.rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
RANK() OVER (
  [ PARTITION BY <expr1> ]
  ORDER BY <expr2> [ { ASC | DESC } ]
  [ <window_frame> ]
)
```

## Exemplos de SQL

**Criar a tabela**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Inserir dados**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**Classificar os funcionários por salário**
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

Resultado:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 1           | John       | Doe       | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 3           | Mike       | Johnson   | IT         | 82000  | 3    |
| 4           | Sara       | Williams  | Sales      | 77000  | 4    |
| 5           | Tom        | Brown     | HR         | 75000  | 5    |
