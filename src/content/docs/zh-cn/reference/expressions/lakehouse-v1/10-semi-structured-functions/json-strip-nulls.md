---
title: JSON_STRIP_NULLS（Lakehouse v1）
description: JSON_STRIP_NULLS — 从 JSON 对象中删除所有值为 null 的属性。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

从 JSON 对象中删除所有值为 null 的属性。

## Analyze 语法

```python
func.json_strip_nulls(<json_string>)
```

## Analyze 示例

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
JSON_STRIP_NULLS(<json_string>)
```

## 返回类型

返回与输入 JSON 值类型相同的值。

## SQL 示例

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
