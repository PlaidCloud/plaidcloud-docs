---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR — 두 비트맵의 대칭차집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

두 비트맵의 대칭차집합을 반환합니다.

## Analyze 구문

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Analyze 예제

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
