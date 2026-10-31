---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — renvoie l'indice du jour de la semaine d'une date (1 = dimanche, 7 = samedi).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

Renvoie l'indice du jour de la semaine d'une date (1 = dimanche, 7 = samedi).

## Syntaxe Analyze

```python
func.dayofweek(<date>)
```

## Exemples Analyze

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## Syntaxe SQL

```sql
DAYOFWEEK(<date>)
```

## Exemples SQL

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
