---
title: DATE_SLICE (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 DATE_SLICE 날짜/시간 함수를 사용합니다. 지정한 기간을 기준으로 주어진 시간을 시간 간격의 시작 또는 끝으로 변환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

지정한 기간을 기준으로 주어진 시간을 시간 간격의 시작 또는 끝으로 변환합니다.

## Analyze 구문

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze 예제

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## SQL 구문

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL 예제

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
