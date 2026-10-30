---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT — 시작 값부터 시작하는 범위에서 크기 제한을 두고 원본 비트맵의 하위 비트맵을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

시작 값부터 시작하는 범위에서 크기 제한을 두고 원본 비트맵의 하위 비트맵을 생성합니다.

## Analyze 구문

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Analyze 예제

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## SQL 예제

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
