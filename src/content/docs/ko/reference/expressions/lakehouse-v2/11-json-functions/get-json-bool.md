---
title: GET_JSON_BOOL (Lakehouse v2)
description: GET_JSON_BOOL — 지정한 경로를 사용하여 JSON 객체에서 불리언 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-bool.md
---

지정한 경로를 사용하여 JSON 객체에서 불리언 값을 추출합니다.

## Analyze 구문

```python
func.get_json_bool(get_column(table, 'data'), '$.active')
```

## Analyze 예제

```python
func.get_json_bool(get_column(table, 'data'), '$.active')

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
GET_JSON_BOOL(<data>, '$.active')
```

## SQL 예제

```sql
SELECT GET_JSON_BOOL('{"active": true}', '$.active');

┌───┐
│ 1 │
└───┘
```
