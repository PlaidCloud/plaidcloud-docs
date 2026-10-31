---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — 检查 JSON 文档在指定路径处是否包含特定值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

检查 JSON 文档在指定路径处是否包含特定值。

## Analyze 语法

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Analyze 示例

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## SQL 示例

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
