---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — 시간 값을 초로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

시간 값을 초로 변환합니다.

## Analyze 구문

```python
func.time_to_sec(<time>)
```

## Analyze 예제

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## SQL 구문

```sql
TIME_TO_SEC(<time>)
```

## SQL 예제

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
