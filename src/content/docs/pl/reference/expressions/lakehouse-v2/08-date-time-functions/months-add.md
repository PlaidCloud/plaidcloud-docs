---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — dodaje określoną liczbę miesięcy do daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

Dodaje określoną liczbę miesięcy do daty.

## Składnia Analyze

```python
func.months_add(<date>, <n>)
```

## Przykłady Analyze

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## Składnia SQL

```sql
MONTHS_ADD(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
