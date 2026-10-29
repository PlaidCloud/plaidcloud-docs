---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — devolve o fatorial de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Devolve o fatorial de `x`. Se `x` for menor ou igual a 0, a função devolve 0.

## Sintaxe do Analyze

```python
func.factorial( <x> )
```

## Exemplos do Analyze

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## Sintaxe SQL

```sql
FACTORIAL( <x> )
```

## Exemplos SQL

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
