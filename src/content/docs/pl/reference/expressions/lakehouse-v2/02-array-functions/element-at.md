---
title: "ELEMENT_AT (Array, Lakehouse v2)"
description: ELEMENT_AT — zwraca element na wskazanej pozycji w tablicy (numerowanie od 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

Zwraca element na wskazanej pozycji w tablicy (numerowanie od 1).

## Składnia Analyze

```python
func.element_at([10, 20, 30], 2)
```

## Przykłady Analyze

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## Składnia SQL

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## Przykłady SQL

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
