---
title: ACOS (Lakehouse v1)
description: ACOS — zwraca arcus cosinus x, czyli wartość, której cosinus wynosi x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

Zwraca arcus cosinus `x`, czyli wartość, której cosinus wynosi `x`. Zwraca NULL, jeśli `x` nie mieści się w zakresie od -1 do 1.

## Składnia Analyze

```python
func.abs( <x> )
```

## Przykłady Analyze

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## Składnia SQL

```sql
ACOS( <x> )
```

## Przykłady SQL

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
