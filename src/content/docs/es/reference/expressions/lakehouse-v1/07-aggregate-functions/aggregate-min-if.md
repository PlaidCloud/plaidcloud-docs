---
title: MIN_IF (Lakehouse v1)
description: "MIN_IF: el sufijo _IF se puede añadir al nombre de cualquier función de agregado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

El sufijo `_IF` se puede añadir al nombre de cualquier función de agregado. En ese caso, la función de agregado acepta un argumento adicional: una condición.

## Sintaxis de Analyze

```python
func.min_if(<column>, <cond>)
```

## Ejemplos de Analyze

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## Sintaxis de SQL

```sql
MIN_IF(<column>, <cond>)
```

## Ejemplos de SQL

**Cree una tabla e inserte datos de ejemplo**
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

**Consulta de demostración: encontrar el presupuesto mínimo del departamento de TI**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**Resultado**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
