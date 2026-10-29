---
title: RETENTION (Lakehouse v2)
description: RETENTION — 이벤트 집합의 리텐션을 계산합니다. 0과 1로 이루어진 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/retention.md
---

이벤트 집합의 리텐션을 계산합니다. 0과 1로 이루어진 배열을 반환합니다.

## Analyze 구문

```python
func.retention(cond1, cond2)
```

## Analyze 예제

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## SQL 구문

```sql
RETENTION(cond1, cond2)
```

## SQL 예제

```sql
SELECT uid, RETENTION(dt='2024-01-01', dt='2024-01-02', dt='2024-01-03')
FROM events GROUP BY uid;

┌─────┬────────────┐
│ uid │ retention  │
├─────┼────────────┤
│   1 │ [1,1,0]    │
│   2 │ [1,0,0]    │
│   3 │ [1,1,1]    │
└─────┴────────────┘
```
