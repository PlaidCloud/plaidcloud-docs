---
title: COT (Lakehouse v1)
description: COT — devuelve la cotangente de x, donde x se expresa en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

Devuelve la cotangente de `x`, donde `x` se expresa en radianes.

## Sintaxis de Analyze

```python
func.cot( <x> )
```

## Ejemplos de Analyze

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
COT( <x> )
```

## Ejemplos de SQL

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
