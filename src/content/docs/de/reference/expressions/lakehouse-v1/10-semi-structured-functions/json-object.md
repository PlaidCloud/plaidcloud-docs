---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — Erstellt ein JSON-Objekt aus abwechselnden Schlüsseln und Werten; TRY_JSON_OBJECT gibt statt eines Fehlers NULL zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

Erstellt ein JSON-Objekt aus abwechselnden Schlüssel- und Wertargumenten. Schlüssel müssen Zeichenfolgen sein; Werte können Konstanten, Ausdrücke oder Spalten sein. Ein Paar, dessen Schlüssel oder Wert NULL ist, wird im Ergebnis weggelassen. Das unterscheidet sich von JSON_ARRAY, das ein NULL-Element beibehält; um solche Paare beizubehalten, verwenden Sie [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/).

`TRY_JSON_OBJECT` akzeptiert dieselben Argumente und gibt NULL zurück, anstatt einen Fehler auszulösen, wenn ein Argument nicht umgewandelt werden kann.

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

JSON-Objekt.

## SQL Examples

### SQL-Beispiele 1: JSON-Objekt mit konstanten Werten erstellen

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### SQL-Beispiele 2: JSON-Objekte aus Tabellendaten erstellen

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

### SQL-Beispiele 3: TRY_JSON_OBJECT gibt bei einem Fehler NULL zurück

Bei einer ungeraden Anzahl von Argumenten bleibt ein Schlüssel ohne Wert, was JSON_OBJECT ablehnt:

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
