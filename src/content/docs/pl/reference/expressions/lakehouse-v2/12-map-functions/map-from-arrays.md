---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — tworzy mapę z tablicy kluczy i tablicy wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

Tworzy mapę z tablicy kluczy i tablicy wartości.

## Składnia Analyze

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Przykłady Analyze

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## Składnia SQL

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## Przykłady SQL

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
