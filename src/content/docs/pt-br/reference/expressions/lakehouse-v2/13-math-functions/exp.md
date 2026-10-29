---
title: EXP (Lakehouse v2)
description: EXP — retorna e elevado à potência de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/exp.md
---

Retorna e elevado à potência de um número.

## Sintaxe do Analyze

```python
func.exp(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT EXP(1);

┌───────────────────┐
│ 2.718281828459045  │
└───────────────────┘
```
