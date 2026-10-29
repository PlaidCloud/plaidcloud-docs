---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — dodaje do daty i godziny podaną liczbę godzin.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

Dodaje do daty i godziny podaną liczbę godzin.

## Składnia Analyze

```python
func.hours_add(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
HOURS_ADD(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
