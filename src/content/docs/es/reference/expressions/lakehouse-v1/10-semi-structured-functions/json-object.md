---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — Crea un objeto JSON a partir de claves y valores alternados; TRY_JSON_OBJECT devuelve NULL en lugar de un error.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

Crea un objeto JSON a partir de argumentos alternados de clave y valor. Las claves deben ser cadenas; los valores pueden ser constantes, expresiones o columnas. Un par cuya clave o valor sea NULL se omite del resultado, a diferencia de JSON_ARRAY, que conserva un elemento NULL; utilice [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/) para conservarlos.

`TRY_JSON_OBJECT` acepta los mismos argumentos y devuelve NULL en lugar de generar un error cuando un argumento no se puede convertir.

## Sintaxis de Analyze

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Ejemplos de Analyze

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## Sintaxis SQL

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## Tipo de retorno

Objeto JSON.

## Ejemplos de SQL

### Ejemplos de SQL 1: creación de un objeto JSON con valores constantes

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### Ejemplos de SQL 2: creación de objetos JSON a partir de datos de una tabla

```sql
CREATE TABLE products (
    ProductName VARCHAR(255),
    Price DECIMAL(10, 2)
);

INSERT INTO products (ProductName, Price)
VALUES
    ('Apple', 1.2),
    ('Banana', 0.5),
    ('Orange', 0.8);

SELECT JSON_OBJECT('name', ProductName, 'price', Price) FROM products;

json_object('name', productname, 'price', price)|
------------------------------------------------+
{"name":"Apple","price":1.2}                    |
{"name":"Banana","price":0.5}                   |
{"name":"Orange","price":0.8}                   |
```

### Ejemplos de SQL 3: TRY_JSON_OBJECT devuelve NULL en caso de error

Un número impar de argumentos deja una clave sin valor, lo que JSON_OBJECT rechaza:

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
