---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — 날짜에 해당하는 월의 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

날짜에 해당하는 월의 이름을 반환합니다.

## Analyze 구문

```python
func.monthname(<date>)
```

## Analyze 예제

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## SQL 구문

```sql
MONTHNAME(<date>)
```

## SQL 예제

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
