---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — zwraca indeks dnia tygodnia dla daty (1 = niedziela, 7 = sobota).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

Zwraca indeks dnia tygodnia dla daty (1 = niedziela, 7 = sobota).

## Składnia Analyze

```python
func.dayofweek(<date>)
```

## Przykłady Analyze

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## Składnia SQL

```sql
DAYOFWEEK(<date>)
```

## Przykłady SQL

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
