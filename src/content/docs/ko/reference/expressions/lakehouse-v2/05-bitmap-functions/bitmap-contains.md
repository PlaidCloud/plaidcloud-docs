---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — 비트맵에 특정 값이 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

비트맵에 특정 값이 포함되어 있는지 확인합니다.

## Analyze 구문

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyze 예제

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQL 예제

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
