---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — 按指定路径从 JSON 对象中提取双精度浮点值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

按指定路径从 JSON 对象中提取双精度浮点值。

## Analyze 语法

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Analyze 示例

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## SQL 语法

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## SQL 示例

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
