---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — Crée un objet JSON à partir de clés et de valeurs alternées ; TRY_JSON_OBJECT renvoie NULL au lieu d'une erreur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

Crée un objet JSON à partir d'arguments alternant clés et valeurs. Les clés doivent être des chaînes ; les valeurs peuvent être des constantes, des expressions ou des colonnes. Une paire dont la clé ou la valeur est NULL est omise du résultat, contrairement à JSON_ARRAY, qui conserve un élément NULL ; utilisez [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/) pour les conserver.

`TRY_JSON_OBJECT` prend les mêmes arguments et renvoie NULL au lieu de lever une erreur lorsqu'un argument ne peut pas être converti.

## Syntaxe Analyze

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Exemples Analyze

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## Syntaxe SQL

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## Type de retour

Objet JSON.

## Exemples SQL

### Exemples SQL 1 : création d'un objet JSON à partir de valeurs constantes

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### Exemples SQL 2 : création d'objets JSON à partir des données de la table

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

### Exemples SQL 3 : TRY_JSON_OBJECT renvoie NULL en cas d'erreur

Un nombre impair d'arguments laisse une clé sans valeur, ce que JSON_OBJECT rejette :

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
