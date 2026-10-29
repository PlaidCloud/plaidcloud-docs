---
title: GET_QUERY_PROFILE (Lakehouse v2)
description: GET_QUERY_PROFILE — 지정한 쿼리 ID의 쿼리 프로필을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/get-query-profile.md
---

지정한 쿼리 ID의 쿼리 프로필을 반환합니다. 성능 분석과 디버깅에 유용합니다.

## Analyze 구문

```python
func.get_query_profile('query_id')
```

## Analyze 예제

```python
func.get_query_profile('abc-123')

┌──────────────────────┐
│ (query profile text) │
└──────────────────────┘
```

## SQL 구문

```sql
GET_QUERY_PROFILE(<query_id>)
```

## SQL 예제

```sql
SELECT GET_QUERY_PROFILE(LAST_QUERY_ID());

┌──────────────────────────┐
│ (detailed query profile) │
└──────────────────────────┘
```
