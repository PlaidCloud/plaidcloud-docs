---
title: MAX_IF (Lakehouse v1)
description: "MAX_IF : le suffixe _IF peut être ajouté au nom de n'importe quelle fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

Le suffixe `_IF` peut être ajouté au nom de n'importe quelle fonction d'agrégation. Dans ce cas, la fonction d'agrégation accepte un argument supplémentaire : une condition.

## Syntaxe Analyze

```python
func.max_if(<column>, <cond>)
```

## Exemples Analyze

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## Exemple SQL

```sql
MAX_IF(<column>, <cond>)
```

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE sales (
  id INT,
  salesperson_id INT,
  product_id INT,
  revenue FLOAT
);

INSERT INTO sales (id, salesperson_id, product_id, revenue)
VALUES (1, 1, 1, 1000),
       (2, 1, 2, 2000),
       (3, 1, 3, 3000),
       (4, 2, 1, 1500),
       (5, 2, 2, 2500);
```

**Exemple de requête : trouver le chiffre d'affaires maximal du commercial dont l'ID est 1**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Résultat**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
