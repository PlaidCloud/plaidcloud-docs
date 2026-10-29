---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — alias de `FLOOR`. Consulte [FLOOR](../floor/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

Alias de `FLOOR`. Consulte [FLOOR](../floor/).

## Sintaxis de Analyze

```python
func.dfloor(3.7)
```

## Ejemplos de Analyze

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
DFLOOR(<x>)
```

## Ejemplos de SQL

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
