---
title: GET_QUERY_DUMP (Lakehouse v2)
description: GET_QUERY_DUMP — 진단 목적으로 쿼리 덤프를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/get-query-dump.md
---

진단 목적으로 쿼리 덤프를 반환합니다.

## Analyze 구문

```python
func.get_query_dump(<query>)
```

## Analyze 예제

```python
func.get_query_dump('SELECT * FROM t')

┌────────┐
│ (dump)  │
└────────┘
```

## SQL 구문

```sql
GET_QUERY_DUMP(<query>)
```

## SQL 예제

```sql
SELECT GET_QUERY_DUMP('SELECT * FROM t');

┌───────────────────┐
│ (diagnostic dump)  │
└───────────────────┘
```
