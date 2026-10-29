---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — renvoie le nombre d'années entre deux dates.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

Renvoie le nombre d'années entre deux dates.

## Syntaxe Analyze

```python
func.years_diff(<end_date>, <start_date>)
```

## Exemples Analyze

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## Exemples SQL

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
