---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — 指定したパスでJSON文字列からJSONオブジェクトを抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

指定したパスでJSON文字列からJSONオブジェクトを抽出します。

## Analyzeの構文

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Analyzeの例

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQLの構文

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## SQLの例

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
