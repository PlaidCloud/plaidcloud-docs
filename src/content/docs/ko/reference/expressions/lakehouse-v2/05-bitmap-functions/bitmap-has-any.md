---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — 두 비트맵에 공통 요소가 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

두 비트맵에 공통 요소가 있는지 확인합니다.

## Analyze 구문

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Analyze 예제

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## SQL 예제

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
