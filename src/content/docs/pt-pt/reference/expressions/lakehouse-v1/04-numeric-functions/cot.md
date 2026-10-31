---
title: COT (Lakehouse v1)
description: COT — devolve a cotangente de x, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

Devolve a cotangente de `x`, em que `x` é dado em radianos.

## Sintaxe do Analyze

```python
func.cot( <x> )
```

## Exemplos do Analyze

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
COT( <x> )
```

## Exemplos SQL

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
