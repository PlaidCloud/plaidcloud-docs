---
title: LN (Lakehouse v2)
description: LN – gibt den natürlichen Logarithmus einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Gibt den natürlichen Logarithmus einer Zahl zurück.

## Analyze-Syntax

```python
func.ln(<x>)
```

## Analyze-Beispiele

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL-Syntax

```sql
LN(<x>)
```

## SQL-Beispiele

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
