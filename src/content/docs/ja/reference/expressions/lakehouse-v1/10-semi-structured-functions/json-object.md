---
title: JSON_OBJECT (Lakehouse v1)
description: JSON_OBJECT — キーと値を交互に指定してJSONオブジェクトを作成します。TRY_JSON_OBJECTはエラーの代わりにNULLを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

キーと値の引数を交互に指定して、JSONオブジェクトを作成します。キーは文字列である必要があり、値には定数、式、列を指定できます。キーまたは値がNULLのペアは結果から除外されます。NULLの要素を保持するJSON_ARRAYとは異なります。NULLを保持するには、[JSON_OBJECT_KEEP_NULL](../json-object-keep-null/)を使用します。

`TRY_JSON_OBJECT` は同じ引数を受け取り、引数を変換できない場合にエラーを発生させる代わりにNULLを返します。

## Analyze構文

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Analyzeの例

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## SQL構文

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## 戻り値の型

JSONオブジェクト。

## SQLの例

### SQLの例1：定数値を使ったJSONオブジェクトの作成

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### SQLの例2：テーブルデータからのJSONオブジェクトの作成

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

### SQLの例3：エラー時にNULLを返すTRY_JSON_OBJECT

引数の数が奇数の場合、値のないキーが生じるため、JSON_OBJECTはエラーとして拒否します。

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
