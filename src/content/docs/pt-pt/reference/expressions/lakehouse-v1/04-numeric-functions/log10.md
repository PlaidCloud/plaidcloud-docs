---
title: LOG10 (Lakehouse v1)
description: LOG10 — devolve o logaritmo de base 10 de x. Referência.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Devolve o logaritmo de base 10 de `x`. Se `x` for menor ou igual a 0.0E0, a função devolve NULL.


## Sintaxe do Analyze

```python
func.log10( <x> )
```

## Exemplos do Analyze

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## Sintaxe SQL

```sql
LOG10( <x> )
```

## Exemplos SQL

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
