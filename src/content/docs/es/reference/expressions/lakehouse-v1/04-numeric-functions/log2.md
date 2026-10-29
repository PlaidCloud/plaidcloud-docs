---
title: LOG2 (Lakehouse v1)
description: LOG2 — devuelve el logaritmo en base 2 de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Devuelve el logaritmo en base 2 de `x`. Si `x` es menor o igual que 0.0E0, la función devuelve NULL.

## Sintaxis de Analyze

```python
func.log2( <x> )
```

## Ejemplos de Analyze

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## Sintaxis de SQL

```sql
LOG2( <x> )
```

## Ejemplos de SQL

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
