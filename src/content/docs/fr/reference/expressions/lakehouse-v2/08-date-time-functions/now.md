---
title: NOW (Lakehouse v2)
description: NOW — renvoie la date et l'heure actuelles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Renvoie la date et l'heure actuelles.

## Syntaxe Analyze

```python
func.now()
```

## Exemples Analyze

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
NOW()
```

## Exemples SQL

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
