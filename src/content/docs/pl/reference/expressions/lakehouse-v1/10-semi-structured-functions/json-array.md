---
title: JSON_ARRAY (Lakehouse v1)
description: JSON_ARRAY — tworzy tablicę JSON z podanych wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array.md
---

Tworzy tablicę JSON z podanych wartości.

## Składnia Analyze

```python
func.json_array(value1[, value2[, ...]])
```

## Przykłady Analyze

```python

func.json_array('fruits', func.json_array('apple', 'banana', 'orange'), func.json_object('price', 1.2, 'quantity', 3)) |
-----------------------------------------------------------------------------------------------------------------------+
["fruits",["apple","banana","orange"],{"price":1.2,"quantity":3}]                                                      |
```

## Składnia SQL

```sql
JSON_ARRAY(value1[, value2[, ...]])
```

## Typ zwracany

Tablica JSON.

## Przykłady SQL

### Przykłady SQL 1: tworzenie tablicy JSON ze stałych wartości lub wyrażeń

```sql
SELECT JSON_ARRAY('PlaidCloud Lakehouse', 3.14, NOW(), TRUE, NULL);

json_array('databend', 3.14, now(), true, null)         |
--------------------------------------------------------+
["PlaidCloud Lakehouse",3.14,"2023-09-06 07:23:55.399070",true,null]|

SELECT JSON_ARRAY('fruits', JSON_ARRAY('apple', 'banana', 'orange'), JSON_OBJECT('price', 1.2, 'quantity', 3));

json_array('fruits', json_array('apple', 'banana', 'orange'), json_object('price', 1.2, 'quantity', 3))|
-------------------------------------------------------------------------------------------------------+
["fruits",["apple","banana","orange"],{"price":1.2,"quantity":3}]                                      |
```

### Przykłady SQL 2: tworzenie tablicy JSON z danych tabeli

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

SELECT JSON_ARRAY(ProductName, Price) FROM products;

json_array(productname, price)|
------------------------------+
["Apple",1.2]                 |
["Banana",0.5]                |
["Orange",0.8]                |
```
