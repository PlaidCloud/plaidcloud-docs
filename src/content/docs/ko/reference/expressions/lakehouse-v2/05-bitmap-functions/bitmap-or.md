---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — 두 비트맵의 합집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

두 비트맵의 합집합을 반환합니다.

## Analyze 구문

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Analyze 예제

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
