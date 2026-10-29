---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — konwertuje datę na liczbę dni.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

Konwertuje datę na liczbę dni.

## Składnia Analyze

```python
func.to_days(<date>)
```

## Przykłady Analyze

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## Składnia SQL

```sql
TO_DAYS(<date>)
```

## Przykłady SQL

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
