---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — 按指定路径从 JSON 对象中提取整数值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

按指定路径从 JSON 对象中提取整数值。

## Analyze 语法

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Analyze 示例

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## SQL 语法

```sql
GET_JSON_INT(<data>, '$.age')
```

## SQL 示例

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
