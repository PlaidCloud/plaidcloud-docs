---
title: APPROX_TOP_K
description: APPROX_TOP_K — returns the top-k most frequent values and their approximate counts.
---

Returns the top-k most frequent values and their approximate counts.

## Analyze Syntax

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze Examples

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL Syntax

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL Examples

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
