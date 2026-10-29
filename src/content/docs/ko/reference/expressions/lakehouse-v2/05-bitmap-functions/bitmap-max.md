---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — 비트맵에서 가장 큰 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

비트맵에서 가장 큰 값을 반환합니다.

## Analyze 구문

```python
func.bitmap_max(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## SQL 구문

```sql
BITMAP_MAX(<bitmap>)
```

## SQL 예제

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
