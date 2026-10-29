---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — 날짜에 지정한 개월 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

날짜에 지정한 개월 수를 더합니다.

## Analyze 구문

```python
func.months_add(<date>, <n>)
```

## Analyze 예제

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## SQL 구문

```sql
MONTHS_ADD(<date>, <n>)
```

## SQL 예제

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
