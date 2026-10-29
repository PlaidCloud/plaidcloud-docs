---
title: QUARTER (Lakehouse v2)
description: QUARTER — 날짜에서 해당 연도의 분기(1~4)를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

날짜에서 해당 연도의 분기(1~4)를 반환합니다.

## Analyze 구문

```python
func.quarter(<date>)
```

## Analyze 예제

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## SQL 구문

```sql
QUARTER(<date>)
```

## SQL 예제

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
