---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — 비트맵 집합의 합집합을 반환합니다(집계).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

비트맵 집합의 합집합을 반환합니다(집계).

## Analyze 구문

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Analyze 예제

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_UNION(<bm>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
