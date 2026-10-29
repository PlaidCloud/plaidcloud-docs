---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — renvoie l'heure actuelle.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

Renvoie l'heure actuelle.

## Syntaxe Analyze

```python
func.current_time()
```

## Exemples Analyze

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Syntaxe SQL

```sql
CURRENT_TIME()
```

## Exemples SQL

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
