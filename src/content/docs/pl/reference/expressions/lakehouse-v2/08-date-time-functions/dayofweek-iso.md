---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — zwraca indeks dnia tygodnia ISO dla daty (1 = poniedziałek, 7 = niedziela).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

Zwraca indeks dnia tygodnia ISO dla daty (1 = poniedziałek, 7 = niedziela).

## Składnia Analyze

```python
func.dayofweek_iso(<date>)
```

## Przykłady Analyze

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Składnia SQL

```sql
DAYOFWEEK_ISO(<date>)
```

## Przykłady SQL

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
