---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — 날짜의 ISO 요일 인덱스를 반환합니다(1=월요일, 7=일요일).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

날짜의 ISO 요일 인덱스를 반환합니다(1=월요일, 7=일요일).

## Analyze 구문

```python
func.dayofweek_iso(<date>)
```

## Analyze 예제

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL 구문

```sql
DAYOFWEEK_ISO(<date>)
```

## SQL 예제

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
