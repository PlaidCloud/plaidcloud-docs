---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — 비트맵에서 특정 값을 제거합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

비트맵에서 특정 값을 제거합니다.

## Analyze 구문

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Analyze 예제

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
