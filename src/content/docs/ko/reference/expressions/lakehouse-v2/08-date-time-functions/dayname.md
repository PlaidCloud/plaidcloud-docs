---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — 날짜에 해당하는 요일 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

날짜에 해당하는 요일 이름을 반환합니다.

## Analyze 구문

```python
func.dayname(<date>)
```

## Analyze 예제

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## SQL 구문

```sql
DAYNAME(<date>)
```

## SQL 예제

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
