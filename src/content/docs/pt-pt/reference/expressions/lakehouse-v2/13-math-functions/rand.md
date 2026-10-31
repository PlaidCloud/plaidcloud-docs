---
title: RAND (Lakehouse v2)
description: RAND — devolve um valor aleatório em vírgula flutuante entre 0 (inclusive) e 1 (exclusive).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Devolve um valor aleatório em vírgula flutuante entre 0 (inclusive) e 1 (exclusive).

## Sintaxe de Analyze

```python
func.rand([<seed>])
```

## Exemplos de Analyze

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## Sintaxe SQL

```sql
RAND([<seed>])
```

## Exemplos SQL

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
