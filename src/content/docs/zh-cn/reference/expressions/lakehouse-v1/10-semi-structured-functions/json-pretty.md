---
title: JSON_PRETTY（Lakehouse v1）
description: JSON_PRETTY — 格式化 JSON 数据，使其更易读、更美观。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-pretty.md
---

格式化 JSON 数据，使其更易读、更美观。它会自动为 JSON 数据添加缩进、换行和其他格式，以获得更好的视觉呈现。

## Analyze 语法

```python
func.json_pretty(<json_string>)
```

## Analyze 示例

```python
func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                               │
│   "location": "City",                                                                           │
│   "person": {                                                                                   │
│     "age": 25,                                                                                  │
│     "name": "Bob"                                                                               │
│   }                                                                                             │
│ }                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
JSON_PRETTY(<json_string>)
```

## 返回类型

String。

## SQL 示例

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

---
┌──────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"name":"alice","age":30}')) │
│                        String                        │
├──────────────────────────────────────────────────────┤
│ {                                                    │
│   "age": 30,                                         │
│   "name": "Alice"                                    │
│ }                                                    │
└──────────────────────────────────────────────────────┘

SELECT JSON_PRETTY(PARSE_JSON('{"person": {"name": "Bob", "age": 25}, "location": "City"}'));

---
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                        │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                     │
│   "location": "City",                                                                 │
│   "person": {                                                                         │
│     "age": 25,                                                                        │
│     "name": "Bob"                                                                     │
│   }                                                                                   │
│ }                                                                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
