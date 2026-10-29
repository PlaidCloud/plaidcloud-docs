---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — 비트맵에서 설정된 비트의 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

비트맵에서 설정된 비트의 수를 반환합니다.

## Analyze 구문

```python
func.bitmap_count(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## SQL 구문

```sql
BITMAP_COUNT(<bitmap>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
