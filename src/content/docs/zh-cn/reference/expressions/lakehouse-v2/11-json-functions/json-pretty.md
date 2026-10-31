---
title: JSON_PRETTY (Lakehouse v2)
description: JSON_PRETTY — 为 JSON 值添加缩进格式，提高可读性。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-pretty.md
---

为 JSON 值添加缩进格式，提高可读性。

## Analyze 语法

```python
func.json_pretty(get_column(table, 'data'))
```

## Analyze 示例

```python
func.json_pretty(get_column(table, 'data'))

┌──────────────────┐
│ (formatted JSON) │
└──────────────────┘
```

## SQL 语法

```sql
JSON_PRETTY(<data>)
```

## SQL 示例

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────────────────────────┐
│ {
  "name": "Alice",
  "age": 30
} │
└────────────────────────────────────┘
```
