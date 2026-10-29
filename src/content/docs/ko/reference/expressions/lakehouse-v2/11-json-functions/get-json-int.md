---
title: GET_JSON_INT (Lakehouse v2)
description: GET_JSON_INT — 지정한 경로를 사용하여 JSON 객체에서 정수 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-int.md
---

지정한 경로를 사용하여 JSON 객체에서 정수 값을 추출합니다.

## Analyze 구문

```python
func.get_json_int(get_column(table, 'data'), '$.age')
```

## Analyze 예제

```python
func.get_json_int(get_column(table, 'data'), '$.age')

┌────┐
│ 30 │
└────┘
```

## SQL 구문

```sql
GET_JSON_INT(<data>, '$.age')
```

## SQL 예제

```sql
SELECT GET_JSON_INT('{"age": 30}', '$.age');

┌────┐
│ 30 │
└────┘
```
