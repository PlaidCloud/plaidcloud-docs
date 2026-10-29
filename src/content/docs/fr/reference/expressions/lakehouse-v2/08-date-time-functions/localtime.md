---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — renvoie la date et l'heure actuelles. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

Renvoie la date et l'heure actuelles. Alias de `NOW`.

## Syntaxe Analyze

```python
func.localtime()
```

## Exemples Analyze

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
LOCALTIME()
```

## Exemples SQL

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
