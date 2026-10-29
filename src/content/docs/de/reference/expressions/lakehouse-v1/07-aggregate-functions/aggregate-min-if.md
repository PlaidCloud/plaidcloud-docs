---
title: MIN_IF (Lakehouse v1)
description: MIN_IF – das Suffix _IF kann an den Namen jeder Aggregatfunktion angehängt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

Das Suffix `_IF` kann an den Namen jeder Aggregatfunktion angehängt werden. In diesem Fall akzeptiert die Aggregatfunktion ein zusätzliches Argument – eine Bedingung.

## Analyze-Syntax

```python
func.min_if(<column>, <cond>)
```

## Analyze-Beispiele

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## SQL-Syntax

```sql
MIN_IF(<column>, <cond>)
```

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Minimales Budget für die IT-Abteilung ermitteln**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**Ergebnis**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
