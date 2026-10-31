---
title: INTERSECT_COUNT (Lakehouse v1)
description: INTERSECT_COUNT – zählt die Anzahl der übereinstimmenden Bits zwischen zwei Bitmap-Spalten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/intersect-count.md
---

Zählt die Anzahl der übereinstimmenden Bits zwischen zwei Bitmap-Spalten.

## Analyze-Syntax

```python
func.intersect_count(( '<bitmap1>', '<bitmap2>' ), ( <bitmap_column1>, <bitmap_column2> ))
```

## Analyze-Beispiele

```python
# Given a dataset like this:

┌───────────────────────────────────────┐
│        id       │ tag  │      v       │
├─────────────────┼─────────────────────┤
│               1 │   a  │  0, 1        │
│               3 │   b  │  0, 1, 2     │
│               2 │   c  │  1, 3, 4     │
└───────────────────────────────────────┘

# This is produced
func.intersect_count(('b', 'c'), (v, tag))
┌──────────────────────────────────────────────────────────┐
│        id       │ func.intersect_count('b', 'c')(v, tag) │
├─────────────────┼────────────────────────────────────────┤
│               1 │                                      0 │
│               3 │                                      3 │
│               2 │                                      3 │
└──────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
INTERSECT_COUNT( '<bitmap1>', '<bitmap2>' )( <bitmap_column1>, <bitmap_column2> )
```

## SQL-Beispiele

```sql
CREATE TABLE agg_bitmap_test(id Int, tag String, v Bitmap);

INSERT INTO
  agg_bitmap_test(id, tag, v)
VALUES
  (1, 'a', to_bitmap('0, 1')),
  (2, 'b', to_bitmap('0, 1, 2')),
  (3, 'c', to_bitmap('1, 3, 4'));

SELECT id, INTERSECT_COUNT('b', 'c')(v, tag) 
FROM agg_bitmap_test GROUP BY id;

┌─────────────────────────────────────────────────────┐
│        id       │ intersect_count('b', 'c')(v, tag) │
├─────────────────┼───────────────────────────────────┤
│               1 │                                 0 │
│               3 │                                 3 │
│               2 │                                 3 │
└─────────────────────────────────────────────────────┘
```
