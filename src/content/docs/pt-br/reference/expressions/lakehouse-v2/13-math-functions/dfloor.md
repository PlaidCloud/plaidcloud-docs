---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — alias de `FLOOR`. Consulte [FLOOR](../floor/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

Alias de `FLOOR`. Consulte [FLOOR](../floor/).

## Sintaxe do Analyze

```python
func.dfloor(3.7)
```

## Exemplos do Analyze

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
DFLOOR(<x>)
```

## Exemplos de SQL

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
