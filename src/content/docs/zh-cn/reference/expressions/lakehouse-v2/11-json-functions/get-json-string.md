---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — 按指定路径从 JSON 对象中提取字符串值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

按指定路径从 JSON 对象中提取字符串值。

## Analyze 语法

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Analyze 示例

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## SQL 语法

```sql
GET_JSON_STRING(<data>, '$.name')
```

## SQL 示例

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
