---
title: JSON_ARRAY (Lakehouse v1)
description: JSON_ARRAY — Cria um array JSON com os valores especificados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array.md
---

Cria um array JSON com os valores especificados.

## Sintaxe do Analyze

```python
func.json_array(value1[, value2[, ...]])
```

## Exemplos do Analyze

```python

func.json_array('fruits', func.json_array('apple', 'banana', 'orange'), func.json_object('price', 1.2, 'quantity', 3)) |
-----------------------------------------------------------------------------------------------------------------------+
["fruits",["apple","banana","orange"],{"price":1.2,"quantity":3}]                                                      |
```

## Sintaxe SQL

```sql
JSON_ARRAY(value1[, value2[, ...]])
```

## Tipo de retorno

Array JSON.

## Exemplos de SQL

### Exemplos de SQL 1: criação de um array JSON com valores constantes ou expressões

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

### Exemplos de SQL 2: criação de um array JSON a partir de dados da tabela

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
