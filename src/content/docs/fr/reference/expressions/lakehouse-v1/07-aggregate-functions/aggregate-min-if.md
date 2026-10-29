---
title: MIN_IF (Lakehouse v1)
description: "MIN_IF : le suffixe _IF peut être ajouté au nom de n'importe quelle fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

Le suffixe `_IF` peut être ajouté au nom de n'importe quelle fonction d'agrégation. Dans ce cas, la fonction d'agrégation accepte un argument supplémentaire : une condition.

## Syntaxe Analyze

```python
func.min_if(<column>, <cond>)
```

## Exemples Analyze

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## Syntaxe SQL

```sql
MIN_IF(<column>, <cond>)
```

## Exemples SQL

**Créer une table et insérer des données d'exemple**
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

**Exemple de requête : trouver le budget minimal du service informatique**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**Résultat**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
