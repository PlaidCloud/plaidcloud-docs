---
title: EXP (Lakehouse v1)
description: EXP — retorna o valor de e (a base dos logaritmos naturais) elevado à potência x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Retorna o valor de e (a base dos logaritmos naturais) elevado à potência `x`.

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

## Exemplos de SQL

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
