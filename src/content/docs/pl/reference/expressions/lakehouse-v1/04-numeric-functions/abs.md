---
title: ABS (Lakehouse v1)
description: ABS — zwraca wartość bezwzględną x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

Zwraca wartość bezwzględną `x`.

## Składnia Analyze

```python
func.abs( <x> )
```

## Przykłady Analyze

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## Składnia SQL

```sql
ABS( <x> )
```

## Przykłady SQL

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
