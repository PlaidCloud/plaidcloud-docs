---
title: BITMAP_HAS_ALL (Lakehouse v1)
description: BITMAP_HAS_ALL — 첫 번째 비트맵에 두 번째 비트맵의 모든 비트가 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-all.md
---

첫 번째 비트맵에 두 번째 비트맵의 모든 비트가 포함되어 있는지 확인합니다.

## Analyze 구문

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Analyze 예제

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## SQL 예제

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```
