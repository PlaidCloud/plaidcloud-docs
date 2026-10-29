---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — 删除 JSON 文档中指定路径处的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

删除 JSON 文档中指定路径处的元素。

## Analyze 语法

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Analyze 示例

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## SQL 语法

```sql
JSON_REMOVE(<data>, '$.temp')
```

## SQL 示例

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
