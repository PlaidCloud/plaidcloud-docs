---
title: EXP (Lakehouse v1)
description: EXP — devolve o valor de e (a base dos logaritmos naturais) elevado à potência de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Devolve o valor de e (a base dos logaritmos naturais) elevado à potência de `x`.

## Sintaxe do Analyze

```python
func.exp( <x> )
```

## Exemplos do Analyze

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## Sintaxe SQL

```sql
EXP( <x> )
```

## Exemplos SQL

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
