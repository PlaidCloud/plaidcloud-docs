---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — renvoie le jour de l'année d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

Renvoie le jour de l'année d'une date.

## Syntaxe Analyze

```python
func.dayofyear(<date>)
```

## Exemples Analyze

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## Syntaxe SQL

```sql
DAYOFYEAR(<date>)
```

## Exemples SQL

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
