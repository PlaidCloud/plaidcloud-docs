---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT — 비트맵 집합의 교집합을 반환합니다(집계).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

비트맵 집합의 교집합을 반환합니다(집계).

## Analyze 구문

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Analyze 예제

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_INTERSECT(<bm>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
