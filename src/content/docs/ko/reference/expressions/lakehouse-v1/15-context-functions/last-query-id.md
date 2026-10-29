---
title: LAST_QUERY_ID (Lakehouse v1)
description: LAST_QUERY_ID — 현재 세션에서 마지막 쿼리의 쿼리 ID를 반환하며, 인덱스는 (-1, 1, 1+2)가 될 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/last-query-id.md
---

현재 세션에서 마지막 쿼리의 쿼리 ID를 반환합니다. 인덱스는 (-1, 1, 1+2)... 등이 될 수 있으며, 범위를 벗어난 인덱스는 빈 문자열을 반환합니다.

## Analyze 구문

```python
func.last_query_id(<index>)
```

## Analyze 예제

```python
func.last_query_id(-1)

┌──────────────────────────────────────┐
│    func.last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```


## SQL 구문

```sql
LAST_QUERY_ID(<index>)
```

## SQL 예제

```sql
SELECT LAST_QUERY_ID(-1);

┌──────────────────────────────────────┐
│         last_query_id((- 1))         │
├──────────────────────────────────────┤
│ a6f615c6-5bad-4863-8558-afd01889448c │
└──────────────────────────────────────┘
```
