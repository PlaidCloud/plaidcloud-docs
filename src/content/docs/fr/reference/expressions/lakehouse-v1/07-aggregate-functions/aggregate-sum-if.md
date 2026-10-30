---
title: SUM_IF (Lakehouse v1)
description: "SUM_IF : le suffixe -If peut être ajouté au nom de n'importe quelle fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

Le suffixe -If peut être ajouté au nom de n'importe quelle fonction d'agrégation. Dans ce cas, la fonction d'agrégation accepte un argument supplémentaire : une condition.

## Syntaxe Analyze

```python
func.sum_if(<column>, <cond>)
```

## Exemples Analyze

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## Syntaxe SQL

```sql
SUM_IF(<column>, <cond>)
```

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**Exemple de requête : calculer le montant total des commandes terminées**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Résultat**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
