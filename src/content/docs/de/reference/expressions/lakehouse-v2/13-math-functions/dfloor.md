---
title: DFLOOR (Lakehouse v2)
description: DFLOOR – Alias für `FLOOR`. Siehe [FLOOR](../floor/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

Alias für `FLOOR`. Siehe [FLOOR](../floor/).

## Analyze-Syntax

```python
func.dfloor(3.7)
```

## Analyze-Beispiele

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
DFLOOR(<x>)
```

## SQL-Beispiele

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
