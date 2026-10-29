---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP — renvoie la date et l'heure actuelles. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

Renvoie la date et l'heure actuelles. Alias de `NOW`.

## Syntaxe Analyze

```python
func.localtimestamp()
```

## Exemples Analyze

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
LOCALTIMESTAMP()
```

## Exemples SQL

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
