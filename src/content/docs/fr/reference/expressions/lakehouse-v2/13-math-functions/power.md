---
title: POWER (Lakehouse v2)
description: POWER — renvoie un nombre élevé à la puissance d'un autre nombre. Alias de `POW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

Renvoie un nombre élevé à la puissance d'un autre nombre. Alias de `POW`.

## Syntaxe Analyze

```python
func.power(<x>, <y>)
```

## Exemples Analyze

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Syntaxe SQL

```sql
POWER(<x>, <y>)
```

## Exemples SQL

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
