---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — 두 비트맵의 차집합(첫 번째에는 있고 두 번째에는 없는 요소)을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

두 비트맵의 차집합(첫 번째에는 있고 두 번째에는 없는 요소)을 반환합니다.

## Analyze 구문

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Analyze 예제

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
