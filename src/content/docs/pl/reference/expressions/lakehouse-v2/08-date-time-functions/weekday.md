---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — zwraca indeks dnia tygodnia dla daty (0=poniedziałek, 6=niedziela).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

Zwraca indeks dnia tygodnia dla daty (0=poniedziałek, 6=niedziela).

## Składnia Analyze

```python
func.weekday(<date>)
```

## Przykłady Analyze

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
WEEKDAY(<date>)
```

## Przykłady SQL

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
