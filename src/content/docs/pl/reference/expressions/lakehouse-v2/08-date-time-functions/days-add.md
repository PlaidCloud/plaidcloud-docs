---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — dodaje do daty podaną liczbę dni.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

Dodaje do daty podaną liczbę dni.

## Składnia Analyze

```python
func.days_add(<date>, <n>)
```

## Przykłady Analyze

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Składnia SQL

```sql
DAYS_ADD(<date>, <n>)
```

## Przykłady SQL

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
