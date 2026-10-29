---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — 두 비트맵의 교집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

두 비트맵의 교집합을 반환합니다.

## Analyze 구문

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Analyze 예제

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
