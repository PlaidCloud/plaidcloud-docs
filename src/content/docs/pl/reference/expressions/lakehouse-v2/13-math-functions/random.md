---
title: RANDOM (Lakehouse v2)
description: RANDOM — zwraca losową wartość zmiennoprzecinkową z przedziału od 0 do 1. Alias funkcji `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Zwraca losową wartość zmiennoprzecinkową z przedziału od 0 do 1. Alias funkcji `RAND`.

## Składnia Analyze

```python
func.random([<seed>])
```

## Przykłady Analyze

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## Składnia SQL

```sql
RANDOM([<seed>])
```

## Przykłady SQL

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
