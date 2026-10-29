---
title: JSON_SET (Lakehouse v2)
description: JSON_SET — 在 JSON 文档的指定路径处设置值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-set.md
---

在 JSON 文档的指定路径处设置值。

## Analyze 语法

```python
func.json_set(get_column(table, 'data'), '$.age', 31)
```

## Analyze 示例

```python
func.json_set(get_column(table, 'data'), '$.age', 31)

┌──────────────┐
│ updated JSON │
└──────────────┘
```

## SQL 语法

```sql
JSON_SET(<data>, '$.age', 31)
```

## SQL 示例

```sql
SELECT JSON_SET(PARSE_JSON('{"name":"Alice"}'), '$.age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
