---
title: COUNT_IF (Lakehouse v1)
description: "COUNT_IF : le suffixe _IF peut être ajouté au nom de n'importe quelle fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

Le suffixe `_IF` peut être ajouté au nom de n'importe quelle fonction d'agrégation. Dans ce cas, la fonction d'agrégation accepte un argument supplémentaire : une condition.

## Syntaxe Analyze

```python
func.count_if(<column>, <cond>)
```

## Exemples Analyze

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## Exemple SQL
```sql
COUNT_IF(<column>, <cond>)
```

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**Exemple de requête : compter les commandes terminées**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**Résultat**
```sql
| completed_orders |
|------------------|
|        3         |
```
