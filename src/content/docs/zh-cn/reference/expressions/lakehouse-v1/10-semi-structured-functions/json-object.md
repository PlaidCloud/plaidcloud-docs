---
title: JSON_OBJECT（Lakehouse v1）
description: JSON_OBJECT — 根据交替出现的键和值创建 JSON 对象；TRY_JSON_OBJECT 返回 NULL 而不是报错。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object.md
---

根据交替出现的键和值参数创建 JSON 对象。键必须是字符串；值可以是常量、表达式或列。键或值为 NULL 的键值对会从结果中省略，这与保留 NULL 元素的 JSON_ARRAY 不同；如需保留这些键值对，请使用 [JSON_OBJECT_KEEP_NULL](../json-object-keep-null/)。

`TRY_JSON_OBJECT` 接受相同的参数，当参数无法转换时返回 NULL，而不是引发错误。

## Analyze 语法

```python
func.json_object(key1, value1[, key2, value2[, ...]])

func.try_json_object(key1, value1[, key2, value2[, ...]])
```

## Analyze 示例

```python
func.json_object('name', table.product_name, 'price', table.price)

json_object('name', product_name, 'price', price)|
--------------------------------------------------+
{"name":"Apple","price":1.2}                      |
```

## SQL 语法

```sql
JSON_OBJECT(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT(key1, value1[, key2, value2[, ...]])
```

## 返回类型

JSON 对象。

## SQL 示例

### SQL 示例 1：使用常量值创建 JSON 对象

```sql
SELECT JSON_OBJECT('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', TRUE);

json_object('name', 'PlaidCloud Lakehouse', 'version', 1, 'active', true)|
--------------------------------------------------------------------------+
{"active":true,"name":"PlaidCloud Lakehouse","version":1}                 |
```

### SQL 示例 2：基于表数据创建 JSON 对象

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

### SQL 示例 3：TRY_JSON_OBJECT 在出错时返回 NULL

参数个数为奇数时，会有一个键没有对应的值，JSON_OBJECT 会拒绝这种情况：

```sql
SELECT TRY_JSON_OBJECT('name');

try_json_object('name')|
-----------------------+
NULL                   |
```
