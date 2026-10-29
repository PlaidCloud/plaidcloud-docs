---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION — 논리 UNION 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

논리 UNION 연산을 수행하여 비트맵에서 1로 설정된 비트의 수를 셉니다.

## Analyze 구문

```python
func.bitmap_union( <bitmap> )
```

## Analyze 예제

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## SQL 구문

```sql
BITMAP_UNION( <bitmap> )
```

## SQL 예제

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
