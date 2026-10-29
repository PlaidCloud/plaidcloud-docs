---
title: BITMAP_FROM_BINARY (Lakehouse v2)
description: BITMAP_FROM_BINARY — 바이너리 값을 비트맵으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-binary.md
---

바이너리 값을 비트맵으로 변환합니다.

## Analyze 구문

```python
func.bitmap_from_binary(<binary>)
```

## Analyze 예제

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_FROM_BINARY(<binary>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
