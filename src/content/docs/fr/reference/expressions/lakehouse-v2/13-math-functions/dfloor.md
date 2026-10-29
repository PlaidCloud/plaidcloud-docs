---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — alias de `FLOOR`. Voir [FLOOR](../floor/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

Alias de `FLOOR`. Voir [FLOOR](../floor/).

## Syntaxe Analyze

```python
func.dfloor(3.7)
```

## Exemples Analyze

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
DFLOOR(<x>)
```

## Exemples SQL

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
