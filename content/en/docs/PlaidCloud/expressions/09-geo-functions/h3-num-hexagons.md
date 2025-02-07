---
title: H3_NUM_HEXAGONS
---

Returns the number of unique [H3](https://eng.uber.com/h3/) indexes at the given resolution. 

## Analyze Syntax

```python
func.h3_num_hexagons(res)
```

## Analyze Examples

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## SQL Syntax

```sql
H3_NUM_HEXAGONS(res)
```

## SQL Examples

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```