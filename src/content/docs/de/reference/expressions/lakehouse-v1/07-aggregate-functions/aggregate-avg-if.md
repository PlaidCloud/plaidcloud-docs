---
title: AVG_IF (Lakehouse v1)
description: AVG_IF – das Suffix -If kann an den Namen jeder Aggregatfunktion angehängt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

Das Suffix -If kann an den Namen jeder Aggregatfunktion angehängt werden. In diesem Fall akzeptiert die Aggregatfunktion ein zusätzliches Argument – eine Bedingung.

## Analyze-Syntax

```python
func.avg_if(<column>, <cond>)
```

## Analyze-Beispiele

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## SQL-Syntax
```sql
AVG_IF(<column>, <cond>)
```

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Durchschnittsgehalt der IT-Abteilung berechnen**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**Ergebnis**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
