---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — tworzy obiekt JSON z naprzemiennych kluczy i wartości; TRY_JSON_OBJECT zwraca NULL zamiast błędu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

Tworzy obiekt JSON z naprzemiennych argumentów klucza i wartości. Klucze muszą być ciągami znaków; wartościami mogą być stałe, wyrażenia lub kolumny. Para, w której klucz lub wartość ma wartość NULL, jest pomijana w wyniku, w odróżnieniu od JSON_ARRAY, która zachowuje element NULL; aby je zachować, użyj [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/).

`TRY_JSON_OBJECT` przyjmuje te same argumenty i zwraca NULL zamiast zgłaszać błąd, gdy argumentu nie można przekonwertować.

## Składnia Analyze

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Przykłady Analyze

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## Składnia SQL

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## Typ zwracany

Obiekt JSON.

## Przykłady SQL

### Przykłady SQL 1: tworzenie obiektu JSON ze stałych wartości

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### Przykłady SQL 2: tworzenie obiektów JSON z danych tabeli

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

### Przykłady SQL 3: TRY_JSON_OBJECT zwraca NULL w razie błędu

Nieparzysta liczba argumentów pozostawia klucz bez wartości, co JSON_OBJECT odrzuca:

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
