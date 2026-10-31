---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — 날짜의 연도와 주 번호를 정수로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

날짜의 연도와 주 번호를 정수로 반환합니다.

## Analyze 구문

```python
func.yearweek(<date>[, <mode>])
```

## Analyze 예제

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## SQL 구문

```sql
YEARWEEK(<date>[, <mode>])
```

## SQL 예제

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
