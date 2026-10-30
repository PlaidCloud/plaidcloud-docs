---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — 비트맵을 행 집합으로 펼칩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

비트맵을 행 집합으로 펼칩니다.

## Analyze 구문

```python
func.unnest_bitmap(<bitmap>)
```

## Analyze 예제

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## SQL 구문

```sql
UNNEST_BITMAP(<bitmap>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
