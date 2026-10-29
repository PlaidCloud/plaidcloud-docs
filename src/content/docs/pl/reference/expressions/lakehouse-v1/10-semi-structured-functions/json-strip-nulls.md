---
title: JSON_STRIP_NULLS (Lakehouse v1)
description: JSON_STRIP_NULLS — usuwa z obiektu JSON wszystkie właściwości o wartościach null.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-strip-nulls.md
---

Usuwa z obiektu JSON wszystkie właściwości o wartościach null. 

## Składnia Analyze

```python
func.json_strip_nulls(<json_string>)
```

## Przykłady Analyze

```python
func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_strip_nulls(func.parse_json('{"name": "alice", "age": 30, "city": null}'))            │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"age":30,"name":"Alice"}                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
JSON_STRIP_NULLS(<json_string>)
```

## Typ zwracany

Zwraca wartość tego samego typu co wejściowa wartość JSON.

## Przykłady SQL

```sql
SELECT JSON_STRIP_NULLS(PARSE_JSON('{"name": "Alice", "age": 30, "city": null}'));

json_strip_nulls(parse_json('{"name": "alice", "age": 30, "city": null}'))|
--------------------------------------------------------------------------+
{"age":30,"name":"Alice"}                                                 |
```
