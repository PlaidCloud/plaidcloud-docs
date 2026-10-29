---
title: DLOG1 (Lakehouse v2)
description: DLOG1 – Alias für `LN`. Siehe [LN](../ln/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

Alias für `LN`. Siehe [LN](../ln/).

## Analyze-Syntax

```python
func.dlog1(2.718281828459045)
```

## Analyze-Beispiele

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## SQL-Syntax

```sql
DLOG1(<x>)
```

## SQL-Beispiele

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
