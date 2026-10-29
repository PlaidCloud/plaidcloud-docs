---
title: SIN (Lakehouse v1)
description: SIN — zwraca sinus x, gdzie x jest podane w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Zwraca sinus `x`, gdzie `x` jest podane w radianach.

## Składnia Analyze

```python
func.sin( <x> )
```

## Przykłady Analyze

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## Składnia SQL

```sql
SIN( <x> )
```

## Przykłady SQL

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
