---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY — 비트맵을 바이너리 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

비트맵을 바이너리 값으로 변환합니다.

## Analyze 구문

```python
func.bitmap_to_binary(<bitmap>)
```

## Analyze 예제

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## SQL 예제

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
