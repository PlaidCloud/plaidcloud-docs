---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — 날짜에 지정한 시간 간격을 더합니다. `DATE_ADD`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

날짜에 지정한 시간 간격을 더합니다. `DATE_ADD`의 별칭입니다.

## Analyze 구문

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Analyze 예제

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL 구문

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## SQL 예제

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
