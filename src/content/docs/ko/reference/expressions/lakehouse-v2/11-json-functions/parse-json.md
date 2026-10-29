---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — JSON 문자열을 파싱하여 JSON 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

JSON 문자열을 파싱하여 JSON 값을 반환합니다.

## Analyze 구문

```python
func.parse_json('{"a":1}')
```

## Analyze 예제

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL 구문

```sql
PARSE_JSON('{"a":1}')
```

## SQL 예제

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
