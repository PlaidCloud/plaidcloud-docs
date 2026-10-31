---
title: DEGREES (Lakehouse v1)
description: DEGREES — zwraca argument x przekonwertowany z radianów na stopnie, gdzie x jest podane w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

Zwraca argument `x` przekonwertowany z radianów na stopnie, gdzie `x` jest podane w radianach.

## Składnia Analyze

```python
func.degrees( <x> )
```

## Przykłady Analyze

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## Składnia SQL

```sql
DEGREES( <x> )
```

## Przykłady SQL

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
