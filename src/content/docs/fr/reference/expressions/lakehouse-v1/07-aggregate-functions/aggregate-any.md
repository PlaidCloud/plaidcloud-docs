---
title: ANY (Lakehouse v1)
description: "ANY : renvoie la première valeur non NULL rencontrée dans un ensemble ; le résultat est indéterminé lorsque l'ordre d'exécution varie."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

Fonction d'agrégation.

La fonction ANY() sélectionne la première valeur (non NULL) rencontrée, sauf si toutes les lignes ont des valeurs NULL dans cette colonne. La requête peut s'exécuter dans n'importe quel ordre, et même dans un ordre différent à chaque fois ; le résultat de cette fonction est donc indéterminé. Pour obtenir un résultat déterminé, vous pouvez utiliser la fonction « min » ou « max » à la place de « any ».

## Syntaxe Analyze

```python
func.any(<expr>)
```

## Exemples Analyze

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## Syntaxe SQL

```sql
ANY(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | Toute expression |

## Type de retour

La première valeur (non NULL) rencontrée, dans le type de cette valeur. Si toutes les valeurs sont NULL, la valeur renvoyée est NULL.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**Exemple de requête : récupérer le premier nom de produit non NULL rencontré**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**Résultat**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
