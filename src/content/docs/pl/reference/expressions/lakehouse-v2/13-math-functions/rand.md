---
title: RAND (Lakehouse v2)
description: RAND — zwraca losową wartość zmiennoprzecinkową z przedziału od 0 (włącznie) do 1 (wyłącznie).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Zwraca losową wartość zmiennoprzecinkową z przedziału od 0 (włącznie) do 1 (wyłącznie).

## Składnia Analyze

```python
func.rand([<seed>])
```

## Przykłady Analyze

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## Składnia SQL

```sql
RAND([<seed>])
```

## Przykłady SQL

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
