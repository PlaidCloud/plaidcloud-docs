---
title: GET_JSON_OBJECT (Lakehouse v2)
description: GET_JSON_OBJECT — 지정한 경로를 사용하여 JSON 문자열에서 JSON 객체를 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-object.md
---

지정한 경로를 사용하여 JSON 문자열에서 JSON 객체를 추출합니다.

## Analyze 구문

```python
func.get_json_object(get_column(table, 'data'), '$.address')
```

## Analyze 예제

```python
func.get_json_object(get_column(table, 'data'), '$.address')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## SQL 구문

```sql
GET_JSON_OBJECT(<data>, '$.address')
```

## SQL 예제

```sql
SELECT GET_JSON_OBJECT('{"address":{"city":"NYC"}}', '$.address');

┌────────────────┐
│ {"city":"NYC"} │
└────────────────┘
```
