---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — 使用路径表达式从 JSON 文档中提取 JSON 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

使用路径表达式从 JSON 文档中提取 JSON 值。

## Analyze 语法

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Analyze 示例

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## SQL 语法

```sql
JSON_QUERY(<data>, '$.items')
```

## SQL 示例

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
