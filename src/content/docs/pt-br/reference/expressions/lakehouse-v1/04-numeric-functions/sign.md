---
title: SIGN (Lakehouse v1)
description: SIGN — retorna o sinal do argumento como -1, 0 ou 1, dependendo de x ser negativo, zero ou positivo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sign.md
---

Retorna o sinal do argumento como -1, 0 ou 1, dependendo de `x` ser negativo, zero ou positivo, ou NULL se o argumento for NULL.

## Sintaxe do Analyze

```python
func.sign( <x> )
```

## Exemplos do Analyze

```python
func.sign(0)

┌──────────────┐
│ func.sign(0) │
├──────────────┤
│            0 │
└──────────────┘
```

## Sintaxe SQL

```sql
SIGN( <x> )
```

## Exemplos de SQL

```sql
SELECT SIGN(0);

┌─────────┐
│ sign(0) │
├─────────┤
│       0 │
└─────────┘
```
