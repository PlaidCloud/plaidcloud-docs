---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — 检查 JSON 文档在指定路径处是否存在值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

检查 JSON 文档在指定路径处是否存在值。

## Analyze 语法

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Analyze 示例

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
JSON_EXISTS(<data>, '$.name')
```

## SQL 示例

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
