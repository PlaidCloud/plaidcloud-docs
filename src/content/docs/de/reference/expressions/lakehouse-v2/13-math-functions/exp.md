---
title: EXP (Lakehouse v2)
description: EXP – gibt e potenziert mit einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Gibt e potenziert mit einer Zahl zurück.

## Analyze-Syntax

```python
func.exp(<x>)
```

## Analyze-Beispiele

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## SQL-Syntax

```sql
EXP(<x>)
```

## SQL-Beispiele

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
