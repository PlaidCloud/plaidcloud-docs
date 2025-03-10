---
title: H3_EDGE_LENGTH_KM
---

Returns the average hexagon edge length in kilometers at the given resolution. Excludes pentagons.

## Analyze Syntax

```python
func.h3_edge_length_km(res)
```

## Analyze Examples

```python
func.h3_edge_length_km(1)

┌───────────────────────────┐
│ func.h3_edge_length_km(1) │
├───────────────────────────┤
│         483.0568390711111 │
└───────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_LENGTH_KM(res)
```

## SQL Examples

```sql
SELECT H3_EDGE_LENGTH_KM(1);

┌──────────────────────┐
│ h3_edge_length_km(1) │
├──────────────────────┤
│    483.0568390711111 │
└──────────────────────┘
```