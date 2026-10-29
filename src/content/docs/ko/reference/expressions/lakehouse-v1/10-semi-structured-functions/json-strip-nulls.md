---
title: JSON_STRIP_NULLS (Lakehouse v1)
description: JSON_STRIP_NULLS — JSON 객체에서 값이 null인 모든 속성을 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

JSON 객체에서 값이 null인 모든 속성을 제거합니다. 

## Analyze Syntax

```python
func.json_strip_nulls(<json_string>)
```

## Analyze Examples

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
JSON_STRIP_NULLS(<json_string>)
```

## 반환 타입

입력 JSON 값과 같은 타입의 값을 반환합니다.

## SQL Examples

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
