---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — renvoie le jour du mois d'une date. Alias de `DAY`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

Renvoie le jour du mois d'une date. Alias de `DAY`.

## Syntaxe Analyze

```python
func.dayofmonth(<date>)
```

## Exemples Analyze

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## Syntaxe SQL

```sql
DAYOFMONTH(<date>)
```

## Exemples SQL

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
