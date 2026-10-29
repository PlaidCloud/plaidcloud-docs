---
title: JSON_PATH_QUERY_FIRST (Lakehouse v1)
description: JSON_PATH_QUERY_FIRST — obtém o primeiro item JSON devolvido pelo caminho JSON para o valor JSON especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query-first.md
---

Obtém o primeiro item JSON devolvido pelo caminho JSON para o valor JSON especificado. 


## Sintaxe do Analyze

```python
func.json_path_query_first(<variant>, <path_name>)
```

## Exemplos do Analyze

```python
table.name, func.json_path_query_first(table.details, '$.features.*').alias('first_feature')

┌────────────┬───────────────┐
│ name       │ first_feature │
├────────────┼───────────────┤
│ Laptop     │ "16GB"        │
│ Laptop     │ "16GB"        │
│ Smartphone │ "4GB"         │
│ Smartphone │ "4GB"         │
│ Headphones │ "20h"         │
│ Headphones │ "20h"         │
└────────────┴───────────────┘
```

## Sintaxe SQL

```sql
JSON_PATH_QUERY_FIRST(<variant>, '<path_name>')
```


## Tipo de retorno

VARIANT

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**

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

**Demonstração de consulta: extrair a primeira funcionalidade dos detalhes do produto**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features,
    JSON_PATH_QUERY_FIRST(details, '$.features.*') AS first_feature
FROM
    products;
```

**Resultado**

```sql
┌────────────┬──────────────┬───────────────┐
│ name       │ all_features │ first_feature │
├────────────┼──────────────┼───────────────┤
│ Laptop     │ "16GB"       │ "16GB"        │
│ Laptop     │ "512GB"      │ "16GB"        │
│ Smartphone │ "4GB"        │ "4GB"         │
│ Smartphone │ "128GB"      │ "4GB"         │
│ Headphones │ "20h"        │ "20h"         │
│ Headphones │ "5.0"        │ "20h"         │
└────────────┴──────────────┴───────────────┘
```
