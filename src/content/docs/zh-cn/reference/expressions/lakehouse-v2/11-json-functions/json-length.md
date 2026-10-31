---
title: JSON_LENGTH (Lakehouse v2)
description: JSON_LENGTH — 返回 JSON 对象或数组中的元素个数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-length.md
---

返回 JSON 对象或数组中的元素个数。

## Analyze 语法

```python
func.json_length(get_column(table, 'data'))
```

## Analyze 示例

```python
func.json_length(get_column(table, 'data'))

┌───┐
│ 2 │
└───┘
```

## SQL 语法

```sql
JSON_LENGTH(<data>)
```

## SQL 示例

```sql
SELECT JSON_LENGTH(PARSE_JSON('{"name":"Alice","age":30}'));

┌───┐
│ 2 │
└───┘
```
