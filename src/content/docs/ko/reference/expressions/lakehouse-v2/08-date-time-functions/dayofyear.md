---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — 날짜에서 연중 일을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

날짜에서 연중 일을 반환합니다.

## Analyze 구문

```python
func.dayofyear(<date>)
```

## Analyze 예제

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQL 구문

```sql
DAYOFYEAR(<date>)
```

## SQL 예제

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
