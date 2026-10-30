---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — 指定したパスでJSONオブジェクトから倍精度浮動小数点値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

指定したパスでJSONオブジェクトから倍精度浮動小数点値を抽出します。

## Analyzeの構文

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Analyzeの例

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## SQLの構文

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## SQLの例

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
