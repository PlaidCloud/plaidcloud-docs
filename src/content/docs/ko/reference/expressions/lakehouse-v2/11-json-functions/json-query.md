---
title: JSON_QUERY (Lakehouse v2)
description: JSON_QUERY — 경로 식을 사용하여 JSON 문서에서 JSON 값을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-query.md
---

경로 식을 사용하여 JSON 문서에서 JSON 값을 추출합니다.

## Analyze 구문

```python
func.json_query(get_column(table, 'data'), '$.items')
```

## Analyze 예제

```python
func.json_query(get_column(table, 'data'), '$.items')

┌────────────┐
│ JSON value │
└────────────┘
```

## SQL 구문

```sql
JSON_QUERY(<data>, '$.items')
```

## SQL 예제

```sql
SELECT JSON_QUERY(PARSE_JSON('{"items":[1,2,3]}'), '$.items');

┌─────────┐
│ [1,2,3] │
└─────────┘
```
