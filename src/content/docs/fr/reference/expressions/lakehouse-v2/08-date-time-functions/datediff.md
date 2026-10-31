---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — renvoie le nombre de jours entre deux dates.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

Renvoie le nombre de jours entre deux dates.

## Syntaxe Analyze

```python
func.datediff(<end_date>, <start_date>)
```

## Exemples Analyze

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Syntaxe SQL

```sql
DATEDIFF(<end_date>, <start_date>)
```

## Exemples SQL

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
