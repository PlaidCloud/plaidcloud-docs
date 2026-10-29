---
title: HOUR (Lakehouse v2)
description: HOUR — zwraca godzinę z daty i godziny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

Zwraca godzinę z daty i godziny.

## Składnia Analyze

```python
func.hour(<datetime>)
```

## Przykłady Analyze

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## Składnia SQL

```sql
HOUR(<datetime>)
```

## Przykłady SQL

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
