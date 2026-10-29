---
title: JSON_PATH_QUERY (Lakehouse v1)
description: JSON_PATH_QUERY — récupère tous les éléments JSON renvoyés par un chemin JSON pour le JSON spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query.md
---

Récupère tous les éléments JSON renvoyés par un chemin JSON pour la valeur JSON spécifiée.

## Syntaxe Analyze

```python
func.json_path_query(<variant>, <path_name>)
```

## Exemples Analyze

```python
table.name, func.json_path_query(table.details, '$.features.*').alias('all_features')

┌────────────┬──────────────┐
│ name       │ all_features │
├────────────┼──────────────┤
│ Laptop     │ "16GB"       │
│ Laptop     │ "512GB"      │
│ Smartphone │ "4GB"        │
│ Smartphone │ "128GB"      │
│ Headphones │ "20h"        │
│ Headphones │ "5.0"        │
└────────────┴──────────────┘
```

## Syntaxe SQL

```sql
JSON_PATH_QUERY(<variant>, '<path_name>')
```


## Type de retour

VARIANT

## Exemples SQL

**Créer une table et insérer des données d'exemple**

```sql
CREATE TABLE products (
    name VARCHAR,
    details VARIANT
);

INSERT INTO products (name, details)
VALUES ('Laptop', '{"brand": "Dell", "colors": ["Black", "Silver"], "price": 1200, "features": {"ram": "16GB", "storage": "512GB"}}'),
       ('Smartphone', '{"brand": "Apple", "colors": ["White", "Black"], "price": 999, "features": {"ram": "4GB", "storage": "128GB"}}'),
       ('Headphones', '{"brand": "Sony", "colors": ["Black", "Blue", "Red"], "price": 150, "features": {"battery": "20h", "bluetooth": "5.0"}}');
```

**Démonstration de requête : extraire toutes les caractéristiques des détails d'un produit**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features
FROM
    products;
```

**Résultat**

```sql
┌────────────┬──────────────┐
│ name       │ all_features │
├────────────┼──────────────┤
│ Laptop     │ "16GB"       │
│ Laptop     │ "512GB"      │
│ Smartphone │ "4GB"        │
│ Smartphone │ "128GB"      │
│ Headphones │ "20h"        │
│ Headphones │ "5.0"        │
└────────────┴──────────────┘
```
