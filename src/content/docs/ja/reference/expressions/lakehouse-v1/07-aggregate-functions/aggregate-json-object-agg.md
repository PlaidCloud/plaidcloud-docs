---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG — キーと値のペアを JSON オブジェクトに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

キーと値のペアを JSON オブジェクトに変換します。入力の各行に対して、キーを `<key_expression>` から、値を `<value_expression>` から求めたキーと値のペアを生成します。これらのペアは 1 つの JSON オブジェクトにまとめられます。

関連項目: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Analyzeの構文

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Analyzeの例
詳細は SQLの例 を参照してください。

## SQLの構文

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| パラメーター        | 説明                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | JSON オブジェクトのキーを指定します。**文字列式のみ**サポートされます。`key_expression` が NULL と評価された場合、そのキーと値のペアはスキップされます。  |
| value_expression | JSON オブジェクトの値を指定します。サポートされている任意のデータ型を指定できます。`value_expression` が NULL と評価された場合、そのキーと値のペアはスキップされます。 |

## 戻り値の型

JSON オブジェクト。

## SQLの例

この例は、JSON_OBJECT_AGG を使用して、小数、整数、JSON バリアント、配列などさまざまな型のデータを、b 列を各 JSON オブジェクトのキーとして JSON オブジェクトに集計する様子を示しています。

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
