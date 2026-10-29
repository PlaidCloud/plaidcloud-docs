---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — 날짜에서 월 중 일을 반환합니다. `DAY`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

날짜에서 월 중 일을 반환합니다. `DAY`의 별칭입니다.

## Analyze 구문

```python
func.dayofmonth(<date>)
```

## Analyze 예제

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL 구문

```sql
DAYOFMONTH(<date>)
```

## SQL 예제

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
