---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — ビットマップを行の集合に展開します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

ビットマップを行の集合に展開します。

## Analyzeの構文

```python
func.unnest_bitmap(<bitmap>)
```

## Analyzeの例

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## SQLの構文

```sql
UNNEST_BITMAP(<bitmap>)
```

## SQLの例

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
