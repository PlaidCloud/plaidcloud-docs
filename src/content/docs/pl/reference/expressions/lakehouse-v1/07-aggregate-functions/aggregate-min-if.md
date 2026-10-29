---
title: MIN_IF (Lakehouse v1)
description: MIN_IF — sufiks _IF można dopisać do nazwy dowolnej funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

Sufiks `_IF` można dopisać do nazwy dowolnej funkcji agregującej. W takim przypadku funkcja agregująca przyjmuje dodatkowy argument – warunek.

## Składnia Analyze

```python
func.min_if(<column>, <cond>)
```

## Przykłady Analyze

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## Składnia SQL

```sql
MIN_IF(<column>, <cond>)
```

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE project_budgets (
  id INT,
  project_id INT,
  department VARCHAR,
  budget FLOAT
);

INSERT INTO project_budgets (id, project_id, department, budget)
VALUES (1, 1, 'HR', 1000),
       (2, 1, 'IT', 2000),
       (3, 1, 'Marketing', 3000),
       (4, 2, 'HR', 1500),
       (5, 2, 'IT', 2500);
```

**Przykład zapytania: znalezienie minimalnego budżetu działu IT**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**Wynik**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
