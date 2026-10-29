---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — 指定したパスでJSONオブジェクトから文字列値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

指定したパスでJSONオブジェクトから文字列値を抽出します。

## Analyzeの構文

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Analyzeの例

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## SQLの構文

```sql
GET_JSON_STRING(<data>, '$.name')
```

## SQLの例

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
