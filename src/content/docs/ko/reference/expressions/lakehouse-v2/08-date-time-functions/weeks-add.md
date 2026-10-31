---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — 날짜에 지정한 주 수를 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

날짜에 지정한 주 수를 더합니다.

## Analyze 구문

```python
func.weeks_add(<date>, <n>)
```

## Analyze 예제

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL 구문

```sql
WEEKS_ADD(<date>, <n>)
```

## SQL 예제

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
