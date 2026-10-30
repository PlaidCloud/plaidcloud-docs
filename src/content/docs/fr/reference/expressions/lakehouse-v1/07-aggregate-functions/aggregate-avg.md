---
title: AVG (Lakehouse v1)
description: "AVG : renvoie la valeur moyenne d'une expression, en ignorant les valeurs NULL."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

Fonction d'agrégation.

La fonction AVG() renvoie la valeur moyenne d'une expression.

**Remarque :** les valeurs NULL ne sont pas prises en compte.


## Syntaxe Analyze

```python
func.avg(<column>)
```

## Exemples Analyze

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## Syntaxe SQL

```sql
AVG(<expr>)
```

## Arguments

| Arguments | Description              |
|-----------|--------------------------|
| `<expr>`  | Toute expression numérique |

## Type de retour

double

## Exemples SQL

**Créer une table et insérer des données d'exemple**

Créons une table nommée « sales » et insérons-y quelques données d'exemple :
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**Requête : utiliser la fonction AVG()**

Utilisons maintenant la fonction AVG() pour calculer le prix moyen de tous les produits de la table « sales » :
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

Le résultat doit ressembler à ceci :
```sql
| avg_price |
| --------- |
| 20.4      |
```
