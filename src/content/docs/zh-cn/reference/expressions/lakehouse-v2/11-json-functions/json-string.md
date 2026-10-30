---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — 将 JSON 值转换为 JSON 编码的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

将 JSON 值转换为 JSON 编码的字符串。

## Analyze 语法

```python
func.json_string(get_column(table, 'data'))
```

## Analyze 示例

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## SQL 语法

```sql
JSON_STRING(<data>)
```

## SQL 示例

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
