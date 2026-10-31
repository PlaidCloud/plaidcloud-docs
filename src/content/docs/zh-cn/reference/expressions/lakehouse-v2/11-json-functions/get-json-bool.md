---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — 按指定路径从 JSON 对象中提取布尔值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

按指定路径从 JSON 对象中提取布尔值。

## Analyze 语法

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Analyze 示例

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## SQL 示例

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
