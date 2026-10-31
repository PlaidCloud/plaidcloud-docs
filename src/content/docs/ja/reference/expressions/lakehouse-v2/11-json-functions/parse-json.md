---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — JSON文字列を解析し、JSON値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

JSON文字列を解析し、JSON値を返します。

## Analyzeの構文

```python
func.parse_json('{"a":1}')
```

## Analyzeの例

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQLの構文

```sql
PARSE_JSON('{"a":1}')
```

## SQLの例

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
