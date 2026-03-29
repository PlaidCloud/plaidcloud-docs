---
title: EQUIWIDTH_BUCKET
---

Returns the bucket number for a value in an equi-width histogram. Divides the range [min, max] into equal-width intervals.

## Analyze Syntax

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Analyze Examples

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## SQL Syntax

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## SQL Examples

```sql
SELECT score, EQUIWIDTH_BUCKET(score, 0, 100, 10) AS bucket
FROM students;

┌───────┬────────┐
│ score │ bucket │
├───────┼────────┤
│    25 │      3 │
│    75 │      8 │
│    95 │     10 │
└───────┴────────┘
```
