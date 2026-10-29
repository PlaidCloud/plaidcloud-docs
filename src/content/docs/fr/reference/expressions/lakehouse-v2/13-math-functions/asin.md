---
title: ASIN (Lakehouse v2)
description: ASIN — renvoie l'arc sinus d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

Renvoie l'arc sinus d'un nombre en radians.

## Syntaxe Analyze

```python
func.asin(<x>)
```

## Exemples Analyze

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## Syntaxe SQL

```sql
ASIN(<x>)
```

## Exemples SQL

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
