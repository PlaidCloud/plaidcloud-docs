---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS – erstellt eine Map aus einem Array von Schlüsseln und einem Array von Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

Erstellt eine Map aus einem Array von Schlüsseln und einem Array von Werten.

## Analyze-Syntax

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Analyze-Beispiele

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## SQL-Syntax

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## SQL-Beispiele

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
