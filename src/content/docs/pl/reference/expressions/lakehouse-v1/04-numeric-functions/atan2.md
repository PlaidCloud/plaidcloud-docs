---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — zwraca arcus tangens dwóch zmiennych x i y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Zwraca arcus tangens dwóch zmiennych `x` i `y`. Działa podobnie do obliczania arcus tangensa `y` / `x`, z tą różnicą, że znaki obu argumentów służą do określenia ćwiartki wyniku. `ATAN(y, x)` jest synonimem `ATAN2(y, x)`.

## Składnia Analyze

```python
func.atan2( <y, x> )
```

## Przykłady Analyze

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## Składnia SQL

```sql
ATAN2( <y, x> )
```

## Przykłady SQL

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
