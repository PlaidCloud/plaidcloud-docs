---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — 지정한 날짜 이전에 가장 가까운 지정 요일의 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

지정한 날짜 이전에 가장 가까운 지정 요일의 날짜를 반환합니다.

## Analyze 구문

```python
func.previous_day(<date>, <weekday>)
```

## Analyze 예제

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## SQL 구문

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## SQL 예제

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
