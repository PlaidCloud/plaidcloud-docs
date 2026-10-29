---
title: BITMAP_OR (Lakehouse v1)
description: BITMAP_OR — 두 비트맵에 대해 비트 OR 연산을 수행합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or.md
---

두 비트맵에 대해 비트 OR 연산을 수행합니다.

## Analyze 구문

```python
func.bitmap_or( <bitmap1>, <bitmap2> )
```

## Analyze 예제

```python
func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7]))

┌─────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7])) │
├─────────────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_OR( <bitmap1>, <bitmap2> )
```

## SQL 예제

```sql
SELECT BITMAP_OR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([6,7]))::String;

┌──────────────────────────────────────────────────────────────────┐
│ bitmap_or(build_bitmap([1, 4, 5]), build_bitmap([6, 7]))::string │
├──────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                        │
└──────────────────────────────────────────────────────────────────┘
```
