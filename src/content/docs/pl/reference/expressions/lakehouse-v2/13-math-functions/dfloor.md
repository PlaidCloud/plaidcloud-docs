---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — alias funkcji `FLOOR`. Zobacz [FLOOR](../floor/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

Alias funkcji `FLOOR`. Zobacz [FLOOR](../floor/).

## Składnia Analyze

```python
func.dfloor(3.7)
```

## Przykłady Analyze

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## Składnia SQL

```sql
DFLOOR(<x>)
```

## Przykłady SQL

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
