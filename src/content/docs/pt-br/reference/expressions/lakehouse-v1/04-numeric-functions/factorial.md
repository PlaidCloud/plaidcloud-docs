---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL — retorna o logaritmo fatorial de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Retorna o logaritmo fatorial de `x`. Se `x` for menor ou igual a 0, a função retorna 0.

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

## Exemplos de SQL

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
