---
title: WEEK (Lakehouse v2)
description: WEEK — 날짜의 주 번호(연중 몇 번째 주인지)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

날짜의 주 번호(연중 몇 번째 주인지)를 반환합니다.

## Analyze 구문

```python
func.week(<date>[, <mode>])
```

## Analyze 예제

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL 구문

```sql
WEEK(<date>[, <mode>])
```

## SQL 예제

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
