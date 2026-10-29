---
title: INTERSECT_COUNT (Lakehouse v1)
description: INTERSECT_COUNT — 2つのビットマップ列の間で、共通するビットの数を数えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/intersect-count.md
---

2つのビットマップ列の間で、共通するビットの数を数えます。

## Analyzeの構文

```python
func.intersect_count(( '<bitmap1>', '<bitmap2>' ), ( <bitmap_column1>, <bitmap_column2> ))
```

## Analyzeの例

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

## SQLの構文

```sql
INTERSECT_COUNT( '<bitmap1>', '<bitmap2>' )( <bitmap_column1>, <bitmap_column2> )
```

## SQLの例

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
