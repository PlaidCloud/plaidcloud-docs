---
title: JSON_STRING (Lakehouse v2)
description: JSON_STRING — JSON 값을 JSON으로 인코딩된 문자열로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-string.md
---

JSON 값을 JSON으로 인코딩된 문자열로 변환합니다.

## Analyze 구문

```python
func.json_string(get_column(table, 'data'))
```

## Analyze 예제

```python
func.json_string(get_column(table, 'json_val'))

┌───────────┐
│ '{"a":1}' │
└───────────┘
```

## SQL 구문

```sql
JSON_STRING(<data>)
```

## SQL 예제

```sql
SELECT JSON_STRING(PARSE_JSON('{"a": 1}'));

┌─────────┐
│ {"a":1} │
└─────────┘
```
