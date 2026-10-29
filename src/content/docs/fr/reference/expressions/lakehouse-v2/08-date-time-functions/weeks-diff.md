---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — renvoie le nombre de semaines entre deux dates.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

Renvoie le nombre de semaines entre deux dates.

## Syntaxe Analyze

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Exemples Analyze

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## Syntaxe SQL

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## Exemples SQL

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
