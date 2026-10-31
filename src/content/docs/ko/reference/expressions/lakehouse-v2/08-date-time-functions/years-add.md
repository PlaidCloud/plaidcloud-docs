---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — 날짜에 지정한 연수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

날짜에 지정한 연수를 더합니다.

## Analyze 구문

```python
func.years_add(<date>, <n>)
```

## Analyze 예제

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## SQL 구문

```sql
YEARS_ADD(<date>, <n>)
```

## SQL 예제

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
