---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — renvoie l'indice ISO du jour de la semaine d'une date (1 = lundi, 7 = dimanche).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

Renvoie l'indice ISO du jour de la semaine d'une date (1 = lundi, 7 = dimanche).

## Syntaxe Analyze

```python
func.dayofweek_iso(<date>)
```

## Exemples Analyze

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## Syntaxe SQL

```sql
DAYOFWEEK_ISO(<date>)
```

## Exemples SQL

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
