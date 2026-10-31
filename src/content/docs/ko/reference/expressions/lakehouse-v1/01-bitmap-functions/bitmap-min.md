---
title: BITMAP_MIN (Lakehouse v1)
description: BITMAP_MIN — 비트맵의 최솟값을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

비트맵의 최솟값을 가져옵니다.

## Analyze 구문

```python
func.bitmap_min( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_MIN( <bitmap> )
```

## SQL 예제

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
