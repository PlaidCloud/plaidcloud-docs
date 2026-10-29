---
title: JSON_EACH (Lakehouse v2)
description: JSON_EACH — 将顶层 JSON 对象展开为一组键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-each.md
---

将顶层 JSON 对象展开为一组键值对。

## Analyze 语法

```python
func.json_each(get_column(table, 'data'))
```

## Analyze 示例

```python
func.json_each(get_column(table, 'data'))
```

## SQL 语法

```sql
JSON_EACH(<data>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(JSON_EACH(PARSE_JSON('{"a":1,"b":2}')));

┌─────┬───────┐
│ key │ value │
├─────┼───────┤
│ a   │ 1     │
│ b   │ 2     │
└─────┴───────┘
```
