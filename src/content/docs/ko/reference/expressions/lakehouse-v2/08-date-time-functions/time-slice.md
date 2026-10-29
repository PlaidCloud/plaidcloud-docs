---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — 지정한 시간을 시간 간격의 시작 또는 끝으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

지정한 시간을 시간 간격의 시작 또는 끝으로 변환합니다.

## Analyze 구문

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze 예제

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL 예제

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
