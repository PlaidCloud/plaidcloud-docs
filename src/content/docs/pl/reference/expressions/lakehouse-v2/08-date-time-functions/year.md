---
title: YEAR (Lakehouse v2)
description: YEAR — zwraca rok z daty.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

Zwraca rok z daty.

## Składnia Analyze

```python
func.year(<date>)
```

## Przykłady Analyze

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## Składnia SQL

```sql
YEAR(<date>)
```

## Przykłady SQL

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
