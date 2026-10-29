---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — zwraca datę następnego wskazanego dnia tygodnia po podanej dacie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Zwraca datę następnego wskazanego dnia tygodnia po podanej dacie.

## Składnia Analyze

```python
func.next_day(<date>, <weekday>)
```

## Przykłady Analyze

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## Składnia SQL

```sql
NEXT_DAY(<date>, <weekday>)
```

## Przykłady SQL

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
