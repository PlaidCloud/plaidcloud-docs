---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — renvoie la différence entre deux valeurs d'heure.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

Renvoie la différence entre deux valeurs d'heure.

## Syntaxe Analyze

```python
func.timediff(<time1>, <time2>)
```

## Exemples Analyze

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## Syntaxe SQL

```sql
TIMEDIFF(<time1>, <time2>)
```

## Exemples SQL

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
