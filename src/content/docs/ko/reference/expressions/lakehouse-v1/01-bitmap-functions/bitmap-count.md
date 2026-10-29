---
title: BITMAP_COUNT (Lakehouse v1)
description: BITMAP_COUNT — 비트맵에서 1로 설정된 비트의 수를 셉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-count.md
---

비트맵에서 1로 설정된 비트의 수를 셉니다.

## Analyze 구문

```python
func.bitmap_count( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_count(build_bitmap([1, 4, 5]))

┌────────────────────────────────────────────┐
│ func.bitmap_count(build_bitmap([1, 4, 5])) │
├────────────────────────────────────────────┤
│                                          3 │
└────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_COUNT( <bitmap> )
```

## 별칭

- [BITMAP_CARDINALITY](../bitmap-cardinality)

## SQL 예제

```sql
SELECT BITMAP_COUNT(BUILD_BITMAP([1,4,5])), BITMAP_CARDINALITY(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ bitmap_count(build_bitmap([1, 4, 5])) │ bitmap_cardinality(build_bitmap([1, 4, 5])) │
├───────────────────────────────────────┼─────────────────────────────────────────────┤
│                                     3 │                                           3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
