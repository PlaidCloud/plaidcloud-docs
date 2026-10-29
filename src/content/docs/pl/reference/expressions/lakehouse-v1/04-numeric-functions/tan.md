---
title: TAN (Lakehouse v1)
description: TAN — zwraca tangens x, gdzie x jest podane w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

Zwraca tangens `x`, gdzie `x` jest podane w radianach.

## Składnia Analyze

```python
func.tan( <x> )
```

## Przykłady Analyze

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## Składnia SQL

```sql
TAN( <x> )
```

## Przykłady SQL

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
