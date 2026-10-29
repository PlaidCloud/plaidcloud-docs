---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v1)
description: BITMAP_SUBSET_IN_RANGE — 지정한 범위 내에서 원본 비트맵의 하위 비트맵을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-in-range.md
---

지정한 범위 내에서 원본 비트맵의 하위 비트맵을 생성합니다.

## Analyze 구문

```python
func.bitmap_subset_in_range( <bitmap>, <start>, <end> )
```

## Analyze 예제

```python
func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9)

┌─────────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9) │
├─────────────────────────────────────────────────────────────────┤
│ 7                                                               │
└─────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_SUBSET_IN_RANGE( <bitmap>, <start>, <end> )
```

## SQL 예제

```sql
SELECT BITMAP_SUBSET_IN_RANGE(BUILD_BITMAP([5,7,9]), 6, 9)::String;

┌───────────────────────────────────────────────────────────────┐
│ bitmap_subset_in_range(build_bitmap([5, 7, 9]), 6, 9)::string │
├───────────────────────────────────────────────────────────────┤
│ 7                                                             │
└───────────────────────────────────────────────────────────────┘
```
