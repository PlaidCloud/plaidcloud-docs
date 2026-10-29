---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — 지정한 날짜가 속한 월의 마지막 날을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

지정한 날짜가 속한 월의 마지막 날을 반환합니다.

## Analyze 구문

```python
func.last_day(<date>[, <unit>])
```

## Analyze 예제

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL 구문

```sql
LAST_DAY(<date>[, <unit>])
```

## SQL 예제

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
