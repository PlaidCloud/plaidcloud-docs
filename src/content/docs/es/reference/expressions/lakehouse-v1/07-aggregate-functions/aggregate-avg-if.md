---
title: AVG_IF (Lakehouse v1)
description: "AVG_IF: el sufijo -If se puede añadir al nombre de cualquier función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

El sufijo -If se puede añadir al nombre de cualquier función de agregado. En ese caso, la función de agregado acepta un argumento adicional: una condición.

## Sintaxis de Analyze

```python
func.avg_if(<column>, <cond>)
```

## Ejemplos de Analyze

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## Sintaxis de SQL
```sql
AVG_IF(<column>, <cond>)
```

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
```sql
CREATE TABLE employees (
  id INT,
  salary INT,
  department VARCHAR
);

INSERT INTO employees (id, salary, department)
VALUES (1, 50000, 'HR'),
       (2, 60000, 'IT'),
       (3, 55000, 'HR'),
       (4, 70000, 'IT'),
       (5, 65000, 'IT');
```

**Consulta de demostración: calcular el salario promedio del departamento de TI**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**Resultado**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
