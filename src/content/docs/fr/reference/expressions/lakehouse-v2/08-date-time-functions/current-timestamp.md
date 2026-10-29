---
title: CURRENT_TIMESTAMP (Lakehouse v2)
description: CURRENT_TIMESTAMP — renvoie la date et l'heure actuelles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timestamp.md
---

Renvoie la date et l'heure actuelles.

## Syntaxe Analyze

```python
func.current_timestamp()
```

## Exemples Analyze

```python
func.current_timestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
CURRENT_TIMESTAMP()
```

## Exemples SQL

```sql
SELECT CURRENT_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
