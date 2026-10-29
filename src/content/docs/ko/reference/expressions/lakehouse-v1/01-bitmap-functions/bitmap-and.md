---
title: BITMAP_AND (Lakehouse v1)
description: BITMAP_AND — 두 비트맵에 대해 비트 AND 연산을 수행합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and.md
---

두 비트맵에 대해 비트 AND 연산을 수행합니다.

## Analyze 구문

```python
func.bitmap_and( <bitmap1>, <bitmap2> )
```

## Analyze 예제

```python
func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string)

┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_and(func.build_bitmap([1, 4, 5]), func.cast(build_bitmap([4, 5])), string) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4,5                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_AND( <bitmap1>, <bitmap2> )
```

## SQL 예제

```sql
SELECT BITMAP_AND(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([4,5]))::String;

┌───────────────────────────────────────────────────────────────────┐
│ bitmap_and(build_bitmap([1, 4, 5]), build_bitmap([4, 5]))::string │
├───────────────────────────────────────────────────────────────────┤
│ 4,5                                                               │
└───────────────────────────────────────────────────────────────────┘
```
