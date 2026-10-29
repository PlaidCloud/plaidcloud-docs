---
title: JSON_EXISTS (Lakehouse v2)
description: JSON_EXISTS — JSON 문서의 지정한 경로에 값이 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-exists.md
---

JSON 문서의 지정한 경로에 값이 있는지 확인합니다.

## Analyze 구문

```python
func.json_exists(get_column(table, 'data'), '$.name')
```

## Analyze 예제

```python
func.json_exists(get_column(table, 'data'), '$.name')

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
JSON_EXISTS(<data>, '$.name')
```

## SQL 예제

```sql
SELECT JSON_EXISTS(PARSE_JSON('{"name":"Alice"}'), '$.name');

┌───┐
│ 1 │
└───┘
```
