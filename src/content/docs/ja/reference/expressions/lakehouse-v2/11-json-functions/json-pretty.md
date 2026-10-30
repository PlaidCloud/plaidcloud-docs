---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — 読みやすいように、JSON値をインデント付きで整形します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

読みやすいように、JSON値をインデント付きで整形します。

## Analyzeの構文

```python
func.json_pretty(get_column(table, 'data'))
```

## Analyzeの例

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## SQLの構文

```sql
JSON_PRETTY(<data>)
```

## SQLの例

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
