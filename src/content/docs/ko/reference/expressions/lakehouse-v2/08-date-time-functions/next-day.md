---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — 지정한 날짜 이후에 처음 오는 지정 요일의 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

지정한 날짜 이후에 처음 오는 지정 요일의 날짜를 반환합니다.

## Analyze 구문

```python
func.next_day(<date>, <weekday>)
```

## Analyze 예제

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## SQL 구문

```sql
NEXT_DAY(<date>, <weekday>)
```

## SQL 예제

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
