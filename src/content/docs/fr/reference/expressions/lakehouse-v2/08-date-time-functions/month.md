---
title: MONTH (Lakehouse v2)
description: MONTH — renvoie le mois d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

Renvoie le mois d'une date.

## Syntaxe Analyze

```python
func.month(<date>)
```

## Exemples Analyze

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Syntaxe SQL

```sql
MONTH(<date>)
```

## Exemples SQL

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
