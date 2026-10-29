---
title: RANDOM (Lakehouse v2)
description: RANDOM – gibt einen zufälligen Gleitkommawert zwischen 0 und 1 zurück. Alias für `RAND`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/random.md
---

Gibt einen zufälligen Gleitkommawert zwischen 0 und 1 zurück. Alias für `RAND`.

## Analyze-Syntax

```python
func.random([<seed>])
```

## Analyze-Beispiele

```python
func.random()

┌───────────┐
│ 0.8123...  │
└───────────┘
```

## SQL-Syntax

```sql
RANDOM([<seed>])
```

## SQL-Beispiele

```sql
SELECT RANDOM();

┌───────────┐
│ 0.8123...  │
└───────────┘
```
