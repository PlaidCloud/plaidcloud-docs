---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — 값의 32비트 해시를 계산하여 해당 해시를 담은 비트맵을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

값의 32비트 해시를 계산하여 해당 해시를 담은 비트맵을 반환합니다.

## Analyze 구문

```python
func.bitmap_hash(<value>)
```

## Analyze 예제

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_HASH(<value>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
