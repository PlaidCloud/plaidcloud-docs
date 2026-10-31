---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — 정수 값을 비트맵으로 집계합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

정수 값을 비트맵으로 집계합니다.

## Analyze 구문

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze 예제

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_AGG(<id>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
