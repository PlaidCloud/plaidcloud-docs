---
title: DAY (Lakehouse v2)
description: DAY — renvoie le jour du mois d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

Renvoie le jour du mois d'une date.

## Syntaxe Analyze

```python
func.day(<date>)
```

## Exemples Analyze

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Syntaxe SQL

```sql
DAY(<date>)
```

## Exemples SQL

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
