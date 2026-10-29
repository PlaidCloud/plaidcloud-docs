---
title: RADIANS (Lakehouse v1)
description: RADIANS — zwraca argument x przekonwertowany ze stopni na radiany.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

Zwraca argument `x` przekonwertowany ze stopni na radiany.

## Składnia Analyze

```python
func.radians( <x> )
```

## Przykłady Analyze

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## Składnia SQL

```sql
RADIANS( <x> )
```

## Przykłady SQL

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
