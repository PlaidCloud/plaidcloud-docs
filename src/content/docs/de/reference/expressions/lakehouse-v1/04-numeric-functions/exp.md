---
title: EXP (Lakehouse v1)
description: EXP – gibt den Wert von e (der Basis des natürlichen Logarithmus) potenziert mit x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Gibt den Wert von e (der Basis des natürlichen Logarithmus) potenziert mit `x` zurück.

## Analyze-Syntax

```python
func.exp( <x> )
```

## Analyze-Beispiele

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## SQL-Syntax

```sql
EXP( <x> )
```

## SQL-Beispiele

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
