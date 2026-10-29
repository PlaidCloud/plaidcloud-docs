---
title: AVG_IF (Lakehouse v1)
description: AVG_IF — sufiks -If można dopisać do nazwy dowolnej funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

Sufiks -If można dopisać do nazwy dowolnej funkcji agregującej. W takim przypadku funkcja agregująca przyjmuje dodatkowy argument – warunek.

## Składnia Analyze

```python
func.avg_if(<column>, <cond>)
```

## Przykłady Analyze

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## Składnia SQL
```sql
AVG_IF(<column>, <cond>)
```

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
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

**Przykład zapytania: obliczenie średniego wynagrodzenia w dziale IT**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**Wynik**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
