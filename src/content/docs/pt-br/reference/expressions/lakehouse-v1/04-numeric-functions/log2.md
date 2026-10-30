---
title: LOG2 (Lakehouse v1)
description: LOG2 — retorna o logaritmo de x na base 2.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Retorna o logaritmo de `x` na base 2. Se `x` for menor ou igual a 0.0E0, a função retorna NULL.

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

## Exemplos de SQL

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
