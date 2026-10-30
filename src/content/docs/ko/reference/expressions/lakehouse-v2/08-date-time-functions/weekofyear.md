---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — 날짜의 연중 주 번호를 반환합니다. `WEEK`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

날짜의 연중 주 번호를 반환합니다. `WEEK`의 별칭입니다.

## Analyze 구문

```python
func.weekofyear(<date>)
```

## Analyze 예제

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL 구문

```sql
WEEKOFYEAR(<date>)
```

## SQL 예제

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
