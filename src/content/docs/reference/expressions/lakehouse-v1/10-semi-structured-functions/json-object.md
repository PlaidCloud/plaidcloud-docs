---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — Creates a JSON object from alternating keys and values; TRY_JSON_OBJECT returns NULL instead of an error.
---

Creates a JSON object from alternating key and value arguments. Keys must be strings; values can be constants, expressions, or columns. A pair whose key or value is NULL is left out of the result, unlike JSON_ARRAY, which keeps a NULL element; use [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/) to keep them.

`TRY_JSON_OBJECT` takes the same arguments and returns NULL instead of raising an error when an argument cannot be converted.

## Analyze Syntax

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Analyze Examples

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## SQL Syntax

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## Return Type

JSON object.

## SQL Examples

### SQL Examples 1: Creating a JSON Object With Constant Values

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### SQL Examples 2: Creating JSON Objects From Table Data

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

### SQL Examples 3: TRY_JSON_OBJECT Returns NULL on Error

An odd number of arguments leaves a key without a value, which JSON_OBJECT rejects:

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
