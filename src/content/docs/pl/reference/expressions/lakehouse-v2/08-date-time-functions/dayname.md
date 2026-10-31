---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — zwraca nazwę dnia tygodnia dla daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

Zwraca nazwę dnia tygodnia dla daty.

## Składnia Analyze

```python
func.dayname(<date>)
```

## Przykłady Analyze

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## Składnia SQL

```sql
DAYNAME(<date>)
```

## Przykłady SQL

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
