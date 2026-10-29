---
title: JSON_PATH_QUERY (Lakehouse v1)
description: JSON_PATH_QUERY — obtiene todos los elementos JSON devueltos por la ruta JSON para el JSON especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query.md
---

Obtiene todos los elementos JSON devueltos por la ruta JSON para el valor JSON especificado.

## Sintaxis de Analyze

```python
func.json_path_query(<variant>, <path_name>)
```

## Ejemplos de Analyze

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

## Sintaxis SQL

```sql
JSON_PATH_QUERY(<variant>, '<path_name>')
```


## Tipo de retorno

VARIANT

## Ejemplos de SQL

**Crear una tabla e insertar datos de ejemplo**

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

**Demostración de consulta: extracción de todas las características de los detalles del producto**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features
FROM
    products;
```

**Resultado**

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
