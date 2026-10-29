---
title: RANDOM (Lakehouse v2)
description: RANDOM — devolve um valor aleatório em vírgula flutuante entre 0 e 1. Alias de `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Devolve um valor aleatório em vírgula flutuante entre 0 e 1. Alias de `RAND`.

## Sintaxe de Analyze

```python
func.random([<seed>])
```

## Exemplos de Analyze

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## Sintaxe SQL

```sql
RANDOM([<seed>])
```

## Exemplos SQL

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
