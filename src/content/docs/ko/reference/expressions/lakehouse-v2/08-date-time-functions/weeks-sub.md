---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — 날짜에서 지정한 주 수를 뺍니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

날짜에서 지정한 주 수를 뺍니다.

## Analyze 구문

```python
func.weeks_sub(<date>, <n>)
```

## Analyze 예제

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQL 구문

```sql
WEEKS_SUB(<date>, <n>)
```

## SQL 예제

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
