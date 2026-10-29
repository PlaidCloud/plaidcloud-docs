---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — dodaje określoną liczbę minut do daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

Dodaje określoną liczbę minut do daty i godziny.

## Składnia Analyze

```python
func.minutes_add(<datetime>, <n>)
```

## Przykłady Analyze

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## Składnia SQL

```sql
MINUTES_ADD(<datetime>, <n>)
```

## Przykłady SQL

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
