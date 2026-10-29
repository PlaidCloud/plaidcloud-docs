---
title: RAND (Lakehouse v2)
description: RAND — devuelve un valor de coma flotante aleatorio entre 0 (incluido) y 1 (excluido).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Devuelve un valor de coma flotante aleatorio entre 0 (incluido) y 1 (excluido).

## Sintaxis de Analyze

```python
func.rand([<seed>])
```

## Ejemplos de Analyze

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## Sintaxis de SQL

```sql
RAND([<seed>])
```

## Ejemplos de SQL

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
