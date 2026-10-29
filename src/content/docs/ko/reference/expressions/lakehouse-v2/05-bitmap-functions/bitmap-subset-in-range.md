---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — 지정한 범위에 속하는 비트맵의 부분집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

지정한 범위에 속하는 비트맵의 부분집합을 반환합니다.

## Analyze 구문

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Analyze 예제

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
