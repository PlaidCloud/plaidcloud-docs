---
title: MONTHS_DIFF (Lakehouse v2)
description: MONTHS_DIFF — renvoie le nombre de mois entre deux dates.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-diff.md
---

Renvoie le nombre de mois entre deux dates.

## Syntaxe Analyze

```python
func.months_diff(<end_date>, <start_date>)
```

## Exemples Analyze

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## Exemples SQL

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
