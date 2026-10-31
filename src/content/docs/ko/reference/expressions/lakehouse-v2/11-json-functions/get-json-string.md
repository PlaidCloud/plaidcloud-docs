---
title: GET_JSON_STRING (Lakehouse v2)
description: GET_JSON_STRING — 지정한 경로를 사용하여 JSON 객체에서 문자열 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-string.md
---

지정한 경로를 사용하여 JSON 객체에서 문자열 값을 추출합니다.

## Analyze 구문

```python
func.get_json_string(get_column(table, 'data'), '$.name')
```

## Analyze 예제

```python
func.get_json_string(get_column(table, 'data'), '$.name')

┌───────┐
│ Alice │
└───────┘
```

## SQL 구문

```sql
GET_JSON_STRING(<data>, '$.name')
```

## SQL 예제

```sql
SELECT GET_JSON_STRING('{"name": "Alice"}', '$.name');

┌───────┐
│ Alice │
└───────┘
```
