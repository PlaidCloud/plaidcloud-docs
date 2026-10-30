---
title: AVG_IF (Lakehouse v1)
description: "AVG_IF : le suffixe -If peut être ajouté au nom de n'importe quelle fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

Le suffixe -If peut être ajouté au nom de n'importe quelle fonction d'agrégation. Dans ce cas, la fonction d'agrégation accepte un argument supplémentaire : une condition.

## Syntaxe Analyze

```python
func.avg_if(<column>, <cond>)
```

## Exemples Analyze

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## Syntaxe SQL
```sql
AVG_IF(<column>, <cond>)
```

## Exemples SQL

**Créer une table et insérer des données d'exemple**
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

**Exemple de requête : calculer le salaire moyen du service informatique**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**Résultat**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
