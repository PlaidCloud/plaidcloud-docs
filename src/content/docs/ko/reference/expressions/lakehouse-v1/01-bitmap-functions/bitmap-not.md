---
title: BITMAP_NOT (Lakehouse v1)
description: BITMAP_NOT — 첫 번째 비트맵의 요소 중 두 번째 비트맵에 없는 요소로 새 비트맵을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not.md
---

첫 번째 비트맵의 요소 중 두 번째 비트맵에 없는 요소로 새 비트맵을 생성합니다.

## Analyze 구문

```python
func.bitmap_not( <bitmap1>, <bitmap2> )
```

## Analyze 예제

```python
func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)

┌───────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_not(func.build_bitmap([1, 4, 5]), func.cast(func.build_bitmap([5, 6, 7])), Text)  │
├───────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_NOT( <bitmap1>, <bitmap2> )
```

## 별칭

- [BITMAP_AND_NOT](../bitmap-and-not)

## SQL 예제

```sql
SELECT BITMAP_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                  │
└──────────────────────────────────────────────────────────────────────┘

SELECT BITMAP_AND_NOT(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────────┐
│ bitmap_and_not(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────────┤
│ 1,4                                                                      │
└──────────────────────────────────────────────────────────────────────────┘
```
