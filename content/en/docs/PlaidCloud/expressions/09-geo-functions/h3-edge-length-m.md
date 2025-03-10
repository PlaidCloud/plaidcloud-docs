---
title: H3_EDGE_LENGTH_M
---

Returns the average hexagon edge length in meters at the given resolution. Excludes pentagons.

## Analyze Syntax

```python
func.h3_edge_length(1)
```

## Analyze Examples

```python
func.h3_edge_length(1)

┌──────────────────────────┐
│ func.h3_edge_length_m(1) │
├──────────────────────────┤
│        483056.8390711111 │
└──────────────────────────┘
```

## SQL Syntax

```sql
H3_EDGE_LENGTH_M(1)
```

## SQL Examples

```sql
┌─────────────────────┐
│ h3_edge_length_m(1) │
├─────────────────────┤
│   483056.8390711111 │
└─────────────────────┘
```