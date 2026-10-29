---
title: RANDOM (Lakehouse v2)
description: RANDOM — retorna um valor de ponto flutuante aleatório entre 0 e 1. Alias de `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Retorna um valor de ponto flutuante aleatório entre 0 e 1. Alias de `RAND`.

## Sintaxe do Analyze

```python
func.random([<seed>])
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
