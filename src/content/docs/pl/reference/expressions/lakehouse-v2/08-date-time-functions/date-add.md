---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD — dodaje do daty lub daty i godziny podany przedział czasu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

Dodaje do daty lub daty i godziny podany przedział czasu.

## Składnia Analyze

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Przykłady Analyze

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## Składnia SQL

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## Przykłady SQL

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
