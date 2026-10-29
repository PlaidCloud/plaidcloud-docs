---
title: MAP_CONCAT (Lakehouse v2)
description: MAP_CONCAT — łączy wiele map w jedną mapę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/map-concat.md
---

Łączy wiele map w jedną mapę.

## Składnia Analyze

```python
func.map_concat(map1, map2)
```

## Przykłady Analyze

```python
func.map_concat(MAP{'a':1}, MAP{'b':2})

┌───────────────┐
│ {'a':1,'b':2} │
└───────────────┘
```

## Składnia SQL

```sql
MAP_CONCAT(map1, map2)
```

## Przykłady SQL

```sql
SELECT MAP_CONCAT(MAP{'a':1}, MAP{'b':2});

┌───────────────┐
│ {"a":1,"b":2} │
└───────────────┘
```
