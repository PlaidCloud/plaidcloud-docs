---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — 날짜/시간 값에 지정한 시간 간격을 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

날짜/시간 값에 지정한 시간 간격을 더합니다.

## Analyze 구문

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Analyze 예제

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL 구문

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## SQL 예제

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
