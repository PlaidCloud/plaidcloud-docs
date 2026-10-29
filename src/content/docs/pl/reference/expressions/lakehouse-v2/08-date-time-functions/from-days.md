---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — konwertuje liczbę dni na datę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

Konwertuje liczbę dni na datę.

## Składnia Analyze

```python
func.from_days(<n>)
```

## Przykłady Analyze

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## Składnia SQL

```sql
FROM_DAYS(<n>)
```

## Przykłady SQL

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
