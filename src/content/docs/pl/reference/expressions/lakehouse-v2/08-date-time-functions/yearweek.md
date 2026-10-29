---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — zwraca rok i numer tygodnia dla daty jako liczbę całkowitą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Zwraca rok i numer tygodnia dla daty jako liczbę całkowitą.

## Składnia Analyze

```python
func.yearweek(<date>[, <mode>])
```

## Przykłady Analyze

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## Składnia SQL

```sql
YEARWEEK(<date>[, <mode>])
```

## Przykłady SQL

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
