---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — renvoie le nom du jour de la semaine d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

Renvoie le nom du jour de la semaine d'une date.

## Syntaxe Analyze

```python
func.dayname(<date>)
```

## Exemples Analyze

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## Syntaxe SQL

```sql
DAYNAME(<date>)
```

## Exemples SQL

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
