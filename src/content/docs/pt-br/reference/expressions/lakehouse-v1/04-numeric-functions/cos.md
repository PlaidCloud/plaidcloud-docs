---
title: COS (Lakehouse v1)
description: COS — retorna o cosseno de x, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

Retorna o cosseno de `x`, em que `x` é dado em radianos.

## Sintaxe do Analyze

```python
func.cos( <x> )
```

## Exemplos do Analyze

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
COS( <x> )
```

## Exemplos de SQL

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
