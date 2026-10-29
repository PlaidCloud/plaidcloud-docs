---
title: BITMAP (Lakehouse v2)
description: BITMAP — 값 집합의 비트맵 합집합을 반환합니다. 일반적으로 BITMAP_AGG와 함께 사용합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

값 집합의 비트맵 합집합을 반환합니다. 일반적으로 BITMAP_AGG와 함께 사용합니다.

## Analyze 구문

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze 예제

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP(<id>)
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
