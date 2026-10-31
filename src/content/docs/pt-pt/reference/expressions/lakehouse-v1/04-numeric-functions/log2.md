---
title: LOG2 (Lakehouse v1)
description: LOG2 — devolve o logaritmo de base 2 de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Devolve o logaritmo de base 2 de `x`. Se `x` for menor ou igual a 0.0E0, a função devolve NULL.

## Sintaxe do Analyze

```python
func.log2( <x> )
```

## Exemplos do Analyze

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## Sintaxe SQL

```sql
LOG2( <x> )
```

## Exemplos SQL

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
