---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — renvoie le nom du mois d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

Renvoie le nom du mois d'une date.

## Syntaxe Analyze

```python
func.monthname(<date>)
```

## Exemples Analyze

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## Syntaxe SQL

```sql
MONTHNAME(<date>)
```

## Exemples SQL

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
