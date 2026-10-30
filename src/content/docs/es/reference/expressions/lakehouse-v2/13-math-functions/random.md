---
title: RANDOM (Lakehouse v2)
description: RANDOM — devuelve un valor de coma flotante aleatorio entre 0 y 1. Alias de `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Devuelve un valor de coma flotante aleatorio entre 0 y 1. Alias de `RAND`.

## Sintaxis de Analyze

```python
func.random([<seed>])
```

## Ejemplos de Analyze

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## Sintaxis de SQL

```sql
RANDOM([<seed>])
```

## Ejemplos de SQL

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
