---
title: EXP (Lakehouse v2)
description: EXP — devolve e elevado à potência de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Devolve e elevado à potência de um número.

## Sintaxe de Analyze

```python
func.exp(<x>)
```

## Exemplos de Analyze

```python
func.exp(1)

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```

## Sintaxe SQL

```sql
EXP(<x>)
```

## Exemplos SQL

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
