---
title: JSON_PRETTY (Lakehouse v1)
description: JSON_PRETTY — JSON 데이터를 서식화하여 더 읽기 쉽고 보기 좋게 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-pretty.md
---

JSON 데이터를 서식화하여 더 읽기 쉽고 보기 좋게 만듭니다. 시각적으로 더 잘 보이도록 JSON 데이터에 들여쓰기, 줄 바꿈 등의 서식을 자동으로 추가합니다.

## Analyze Syntax

```python
func.json_pretty(<json_string>)
```

## Analyze Examples

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

## SQL Syntax

```sql
JSON_PRETTY(<json_string>)
```

## 반환 타입

문자열.

## SQL Examples

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
