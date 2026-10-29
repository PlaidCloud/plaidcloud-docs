---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — 비트맵 집합의 합집합에 있는 고유 값의 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

비트맵 집합의 합집합에 있는 고유 값의 개수를 반환합니다.

## Analyze 구문

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Analyze 예제

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## SQL 구문

```sql
BITMAP_UNION_COUNT(<bm>)
```

## SQL 예제

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
