---
title: COVAR_POP (Lakehouse v1)
description: "COVAR_POP : COVAR_POP renvoie la covariance de population d'un ensemble de paires de nombres."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP renvoie la covariance de population d'un ensemble de paires de nombres. 

## Syntaxe Analyze

```python
func.covar_pop(<expr1>, <expr2>)
```

## Exemples Analyze

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## Syntaxe SQL

```sql
COVAR_POP(<expr1>, <expr2>)
```

## Arguments

| Arguments |        Description       |
|-----------| ------------------------ |
| `<expr1>` | Toute expression numérique |
| `<expr2>` | Toute expression numérique |

## Type de retour

float64

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE product_sales (
  id INT,
  product_id INT,
  units_sold INT,
  revenue FLOAT
);

INSERT INTO product_sales (id, product_id, units_sold, revenue)
VALUES (1, 1, 10, 1000),
       (2, 2, 20, 2000),
       (3, 3, 30, 3000),
       (4, 4, 40, 4000),
       (5, 5, 50, 5000);
```

**Exemple de requête : calculer la covariance de population entre les unités vendues et le chiffre d'affaires**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**Résultat**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
