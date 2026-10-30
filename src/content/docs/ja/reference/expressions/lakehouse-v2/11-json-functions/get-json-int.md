---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — 指定したパスでJSONオブジェクトから整数値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

指定したパスでJSONオブジェクトから整数値を抽出します。

## Analyzeの構文

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Analyzeの例

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## SQLの構文

```sql
GET_JSON_INT(<data>, '$.age')
```

## SQLの例

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
