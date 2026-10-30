---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — zwraca datę poprzedniego wskazanego dnia tygodnia przed podaną datą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Zwraca datę poprzedniego wskazanego dnia tygodnia przed podaną datą.

## Składnia Analyze

```python
func.previous_day(<date>, <weekday>)
```

## Przykłady Analyze

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## Składnia SQL

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## Przykłady SQL

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
