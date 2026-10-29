---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — JSON値をJSONエンコードされた文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

JSON値をJSONエンコードされた文字列に変換します。

## Analyzeの構文

```python
func.json_string(get_column(table, 'data'))
```

## Analyzeの例

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## SQLの構文

```sql
JSON_STRING(<data>)
```

## SQLの例

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
