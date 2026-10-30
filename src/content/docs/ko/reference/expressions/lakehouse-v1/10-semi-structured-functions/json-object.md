---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — 번갈아 나오는 키와 값으로 JSON 객체를 만듭니다. TRY_JSON_OBJECT는 오류 대신 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

번갈아 나오는 키 인수와 값 인수로 JSON 객체를 만듭니다. 키는 문자열이어야 하며, 값은 상수, 식 또는 열일 수 있습니다. 키나 값이 NULL인 쌍은 결과에서 제외됩니다. NULL 요소를 유지하는 JSON_ARRAY와 다른 점이며, 이러한 쌍을 유지하려면 [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/)을 사용하십시오.

`TRY_JSON_OBJECT`는 같은 인수를 받으며, 인수를 변환할 수 없을 때 오류를 발생시키는 대신 NULL을 반환합니다.

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

## 반환 타입

JSON 객체.

## SQL Examples

### SQL Examples 1: 상수 값으로 JSON 객체 만들기

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### SQL Examples 2: 테이블 데이터로 JSON 객체 만들기

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

### SQL Examples 3: 오류 시 NULL을 반환하는 TRY_JSON_OBJECT

인수가 홀수 개이면 값이 없는 키가 생기며, JSON_OBJECT는 이를 거부합니다.

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
