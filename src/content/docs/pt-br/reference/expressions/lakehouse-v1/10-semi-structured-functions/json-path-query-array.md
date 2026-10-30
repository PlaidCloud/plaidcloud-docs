---
title: JSON_PATH_QUERY_ARRAY (Lakehouse v1)
description: JSON_PATH_QUERY_ARRAY — obtém todos os itens JSON retornados pelo caminho JSON para o valor JSON especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query-array.md
---

Obtém todos os itens JSON retornados pelo caminho JSON para o valor JSON especificado e encapsula o resultado em um array.

## Sintaxe do Analyze

```python
func.json_path_query_array(<variant>, <path_name>)
```

## Exemplos do Analyze

```python
table.name, func.json_path_query_array(table.details, '$.features.*').alias('all_features')

   name     |     all_features
------------+-----------------------
 Laptop     | ["16GB", "512GB"]
 Smartphone | ["4GB", "128GB"]
 Headphones | ["20h", "5.0"]
```

## Sintaxe SQL

```sql
JSON_PATH_QUERY_ARRAY(<variant>, '<path_name>')
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

**Demonstração de consulta: extração de todos os recursos dos detalhes do produto como um array**

```sql
SELECT
    name,
    JSON_PATH_QUERY_ARRAY(details, '$.features.*') AS all_features
FROM
    products;
```

**Resultado**

```text
   name    |         all_features
-----------+-----------------------
 Laptop    | ["16GB", "512GB"]
 Smartphone | ["4GB", "128GB"]
 Headphones | ["20h", "5.0"]
```
