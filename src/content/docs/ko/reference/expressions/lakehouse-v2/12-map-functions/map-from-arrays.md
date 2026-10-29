---
title: MAP_FROM_ARRAYS (Lakehouse v2)
description: MAP_FROM_ARRAYS — 키 배열과 값 배열로 맵을 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-from-arrays.md
---

키 배열과 값 배열로 맵을 만듭니다.

## Analyze 구문

```python
func.map_from_arrays(['a','b'], [1, 2])
```

## Analyze 예제

```python
func.map_from_arrays(['a', 'b', 'c'], [1, 2, 3])

┌─────────────────────┐
│ {'a':1,'b':2,'c':3} │
└─────────────────────┘
```

## SQL 구문

```sql
MAP_FROM_ARRAYS(['a','b'], [1, 2])
```

## SQL 예제

```sql
SELECT MAP_FROM_ARRAYS(['a', 'b', 'c'], [1, 2, 3]);

┌─────────────────────┐
│ {"a":1,"b":2,"c":3} │
└─────────────────────┘
```
