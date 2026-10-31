---
title: RAND (Lakehouse v2)
description: RAND — retorna um valor de ponto flutuante aleatório entre 0 (inclusivo) e 1 (exclusivo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Retorna um valor de ponto flutuante aleatório entre 0 (inclusivo) e 1 (exclusivo).

## Sintaxe do Analyze

```python
func.rand([<seed>])
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
