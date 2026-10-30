---
title: WEEKS_ADD (Lakehouse v2)
description: WEEKS_ADD — dodaje określoną liczbę tygodni do daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-add.md
---

Dodaje określoną liczbę tygodni do daty.

## Składnia Analyze

```python
func.weeks_add(<date>, <n>)
```

## Przykłady Analyze

```python
func.weeks_add('2024-01-01', 2)

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Składnia SQL

```sql
WEEKS_ADD(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT WEEKS_ADD('2024-01-01', 2);

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
