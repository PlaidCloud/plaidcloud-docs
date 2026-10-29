---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS — 以 JSON 数组形式返回顶层 JSON 对象的键。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

以 JSON 数组形式返回顶层 JSON 对象的键。

## Analyze 语法

```python
func.json_keys(get_column(table, 'data'))
```

## Analyze 示例

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## SQL 语法

```sql
JSON_KEYS(<data>)
```

## SQL 示例

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
