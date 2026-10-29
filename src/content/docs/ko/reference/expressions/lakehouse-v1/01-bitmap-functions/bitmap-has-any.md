---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: BITMAP_HAS_ANY — 첫 번째 비트맵에 두 번째 비트맵의 비트와 일치하는 비트가 하나라도 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

첫 번째 비트맵에 두 번째 비트맵의 비트와 일치하는 비트가 하나라도 있는지 확인합니다.

## Analyze 구문

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Analyze 예제

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## SQL 예제

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
