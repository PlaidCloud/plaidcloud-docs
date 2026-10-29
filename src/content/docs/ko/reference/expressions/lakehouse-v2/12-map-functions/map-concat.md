---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — 여러 맵을 하나의 맵으로 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

여러 맵을 하나의 맵으로 연결합니다.

## Analyze 구문

```python
func.map_concat(map1, map2)
```

## Analyze 예제

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## SQL 구문

```sql
MAP_CONCAT(map1, map2)
```

## SQL 예제

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
