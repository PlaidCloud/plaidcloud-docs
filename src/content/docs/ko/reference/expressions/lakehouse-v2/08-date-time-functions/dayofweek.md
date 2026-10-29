---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — 날짜의 요일 인덱스를 반환합니다(1=일요일, 7=토요일).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

날짜의 요일 인덱스를 반환합니다(1=일요일, 7=토요일).

## Analyze 구문

```python
func.dayofweek(<date>)
```

## Analyze 예제

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## SQL 구문

```sql
DAYOFWEEK(<date>)
```

## SQL 예제

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
