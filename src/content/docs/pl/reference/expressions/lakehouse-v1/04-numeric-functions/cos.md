---
title: COS (Lakehouse v1)
description: COS — zwraca cosinus x, gdzie x jest podane w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

Zwraca cosinus `x`, gdzie `x` jest podane w radianach.

## Składnia Analyze

```python
func.cos( <x> )
```

## Przykłady Analyze

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## Składnia SQL

```sql
COS( <x> )
```

## Przykłady SQL

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
