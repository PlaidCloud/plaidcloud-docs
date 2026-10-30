---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG：将键值对转换为 JSON 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

将键值对转换为 JSON 对象。对输入中的每一行，生成一个键值对，其中键来自 `<key_expression>`，值来自 `<value_expression>`。这些键值对随后被合并为单个 JSON 对象。

另请参阅：[JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Analyze 语法

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Analyze 示例
详见 SQL 示例

## SQL 语法

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| 参数        | 说明                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | 指定 JSON 对象中的键。**仅支持字符串**表达式。如果 `key_expression` 的计算结果为 NULL，则跳过该键值对。  |
| value_expression | 指定 JSON 对象中的值。可以是任何受支持的数据类型。如果 `value_expression` 的计算结果为 NULL，则跳过该键值对。 |

## 返回类型

JSON 对象。

## SQL 示例

此示例演示如何使用 JSON_OBJECT_AGG 将不同类型的数据（如小数、整数、JSON 变体和数组）聚合为 JSON 对象，并以列 b 作为每个 JSON 对象的键：

```sql
CREATE TABLE d (
    a DECIMAL(10, 2), 
    b STRING, 
    c INT, 
    d VARIANT, 
    e ARRAY(STRING)
);

INSERT INTO d VALUES
    (20, 'abc', NULL, '{"k":"v"}', ['a','b']),
    (10, 'de', 100, 'null', []),
    (4.23, NULL, 200, '"uvw"', ['x','y']),
    (5.99, 'xyz', 300, '[1,2,3]', ['z']);

SELECT
    json_object_agg(b, a) AS json_a,
    json_object_agg(b, c) AS json_c,
    json_object_agg(b, d) AS json_d,
    json_object_agg(b, e) AS json_e
FROM
    d;

-[ RECORD 1 ]-----------------------------------
json_a: {"abc":20.0,"de":10.0,"xyz":5.99}
json_c: {"de":100,"xyz":300}
json_d: {"abc":{"k":"v"},"de":null,"xyz":[1,2,3]}
json_e: {"abc":["a","b"],"de":[],"xyz":["z"]}
```
