---
title: ARG_MAX (Lakehouse v1)
description: "ARG_MAX : calcule la valeur arg correspondant à la valeur val maximale."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

Calcule la valeur `arg` correspondant à la valeur `val` maximale. Si plusieurs valeurs de `arg` correspondent aux valeurs maximales de `val`, renvoie la première de ces valeurs rencontrée.

## Syntaxe Analyze

```python
func.arg_max(<expr>)
```

## Exemples Analyze

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## Syntaxe SQL

```sql
ARG_MAX(<arg>, <val>)
```

## Arguments

| Arguments | Description                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument de n'importe quel type de données pris en charge par PlaidCloud Lakehouse |
| `<val>`   | Valeur de n'importe quel type de données pris en charge par PlaidCloud Lakehouse    |

## Type de retour

Valeur `arg` correspondant à la valeur `val` maximale.

 correspond au type de `arg`.

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

**Requête : utiliser la fonction ARG_MAX()**

Utilisons maintenant la fonction ARG_MAX() pour trouver le produit dont le prix est le plus élevé :
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

Le résultat doit ressembler à ceci :
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
