---
title: ACOS (Lakehouse v2)
description: ACOS — renvoie l'arc cosinus d'un nombre en radians.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

Renvoie l'arc cosinus d'un nombre en radians.

## Syntaxe Analyze

```python
func.acos(<x>)
```

## Exemples Analyze

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## Syntaxe SQL

```sql
ACOS(<x>)
```

## Exemples SQL

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
