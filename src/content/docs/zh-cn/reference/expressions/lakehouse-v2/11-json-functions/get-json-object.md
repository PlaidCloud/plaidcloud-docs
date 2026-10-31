---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — 按指定路径从 JSON 字符串中提取 JSON 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

按指定路径从 JSON 字符串中提取 JSON 对象。

## Analyze 语法

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Analyze 示例

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL 语法

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## SQL 示例

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
