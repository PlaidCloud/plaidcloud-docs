---
title: YEAR (Lakehouse v2)
description: YEAR — 날짜에서 연도를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

날짜에서 연도를 반환합니다.

## Analyze 구문

```python
func.year(<date>)
```

## Analyze 예제

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## SQL 구문

```sql
YEAR(<date>)
```

## SQL 예제

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
