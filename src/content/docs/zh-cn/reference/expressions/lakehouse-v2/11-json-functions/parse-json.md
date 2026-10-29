---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — 解析 JSON 字符串并返回 JSON 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

解析 JSON 字符串并返回 JSON 值。

## Analyze 语法

```python
func.parse_json('{"a":1}')
```

## Analyze 示例

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL 语法

```sql
PARSE_JSON('{"a":1}')
```

## SQL 示例

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
