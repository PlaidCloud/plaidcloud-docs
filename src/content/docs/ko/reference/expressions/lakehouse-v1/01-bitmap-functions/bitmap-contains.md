---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS — 비트맵에 특정 값이 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

비트맵에 특정 값이 포함되어 있는지 확인합니다.


## Analyze 구문

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Analyze 예제

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## SQL 예제

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
