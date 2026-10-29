---
title: QUARTER (Lakehouse v2)
description: QUARTER — renvoie le trimestre de l'année d'une date (1-4).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

Renvoie le trimestre de l'année d'une date (1-4).

## Syntaxe Analyze

```python
func.quarter(<date>)
```

## Exemples Analyze

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## Syntaxe SQL

```sql
QUARTER(<date>)
```

## Exemples SQL

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
