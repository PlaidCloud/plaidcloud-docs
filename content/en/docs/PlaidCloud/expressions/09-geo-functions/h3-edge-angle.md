---
title: H3_EDGE_ANGLE
---

Returns the average length of the H3 hexagon edge in grades.

## Analyze Syntax

```python
func.h3_edge_angle(res)
```

## Analyze Examples

```python
func.h3_edge_angle(10)

┌────────────────────────────┐
│   func.h3_edge_angle(10)   │
├────────────────────────────┤
│      0.0006822586214153981 │
└────────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_ANGLE(res)
```

## SQL Examples

```sql
SELECT H3_EDGE_ANGLE(10);

┌───────────────────────┐
│   h3_edge_angle(10)   │
├───────────────────────┤
│ 0.0006822586214153981 │
└───────────────────────┘
```