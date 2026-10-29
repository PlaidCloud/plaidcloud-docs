---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — パス式を使用してJSONドキュメントからJSON値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

パス式を使用してJSONドキュメントからJSON値を抽出します。

## Analyzeの構文

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Analyzeの例

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## SQLの構文

```sql
JSON_QUERY(<data>, '$.items')
```

## SQLの例

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
