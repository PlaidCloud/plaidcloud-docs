---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — 비트맵을 지정한 크기의 여러 하위 비트맵으로 분할합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

비트맵을 지정한 크기의 여러 하위 비트맵으로 분할합니다.

## Analyze 구문

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Analyze 예제

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## SQL 구문

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
