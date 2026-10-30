---
title: LAST_QUERY_ID (Lakehouse v2)
description: LAST_QUERY_ID — 가장 최근에 실행한 쿼리의 ID를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/last-query-id.md
---

가장 최근에 실행한 쿼리의 ID를 반환합니다.

## Analyze 구문

```python
func.last_query_id()
```

## Analyze 예제

```python
func.last_query_id()

┌───────────────┐
│ 'abc-123-def'  │
└───────────────┘
```

## SQL 구문

```sql
LAST_QUERY_ID()
```

## SQL 예제

```sql
SELECT LAST_QUERY_ID();

┌─────────────────┐
│ abc-123-def-456  │
└─────────────────┘
```
