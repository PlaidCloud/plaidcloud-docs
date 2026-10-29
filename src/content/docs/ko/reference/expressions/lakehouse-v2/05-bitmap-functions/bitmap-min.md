---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — 비트맵에서 가장 작은 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

비트맵에서 가장 작은 값을 반환합니다.

## Analyze 구문

```python
func.bitmap_min(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
BITMAP_MIN(<bitmap>)
```

## SQL 예제

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
