---
title: GET_JSON_DOUBLE (Lakehouse v2)
description: GET_JSON_DOUBLE — 지정한 경로를 사용하여 JSON 객체에서 double 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/get-json-double.md
---

지정한 경로를 사용하여 JSON 객체에서 double 값을 추출합니다.

## Analyze 구문

```python
func.get_json_double(get_column(table, 'data'), '$.price')
```

## Analyze 예제

```python
func.get_json_double(get_column(table, 'data'), '$.price')

┌───────┐
│ 19.99 │
└───────┘
```

## SQL 구문

```sql
GET_JSON_DOUBLE(<data>, '$.price')
```

## SQL 예제

```sql
SELECT GET_JSON_DOUBLE('{"price": 19.99}', '$.price');

┌───────┐
│ 19.99 │
└───────┘
```
