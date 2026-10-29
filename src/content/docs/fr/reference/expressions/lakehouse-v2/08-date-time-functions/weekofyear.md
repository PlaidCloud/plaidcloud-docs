---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — renvoie la semaine de l'année pour une date. Alias de `WEEK`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

Renvoie la semaine de l'année pour une date. Alias de `WEEK`.

## Syntaxe Analyze

```python
func.weekofyear(<date>)
```

## Exemples Analyze

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Syntaxe SQL

```sql
WEEKOFYEAR(<date>)
```

## Exemples SQL

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
