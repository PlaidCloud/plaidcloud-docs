---
title: CURTIME (Lakehouse v2)
description: CURTIME — renvoie l'heure actuelle. Alias de `CURRENT_TIME`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

Renvoie l'heure actuelle. Alias de `CURRENT_TIME`.

## Syntaxe Analyze

```python
func.curtime()
```

## Exemples Analyze

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Syntaxe SQL

```sql
CURTIME()
```

## Exemples SQL

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
