---
title: BITMAP_MAX (Lakehouse v1)
description: BITMAP_MAX — 비트맵의 최댓값을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-max.md
---

비트맵의 최댓값을 가져옵니다.

## Analyze 구문

```python
func.bitmap_max( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_MAX( <bitmap> )
```

## SQL 예제

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```
