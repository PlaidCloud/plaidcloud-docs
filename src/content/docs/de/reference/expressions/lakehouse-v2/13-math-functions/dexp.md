---
title: DEXP (Lakehouse v2)
description: DEXP – Alias für `EXP`. Siehe [EXP](../exp/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dexp.md
---

Alias für `EXP`. Siehe [EXP](../exp/).

## Analyze-Syntax

```python
func.dexp(1)
```

## Analyze-Beispiele

```python
func.dexp(1)

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```

## SQL-Syntax

```sql
DEXP(<x>)
```

## SQL-Beispiele

```sql
SELECT DEXP(1);

┌───────────────────┐
│ 2.718281828459045 │
└───────────────────┘
```
