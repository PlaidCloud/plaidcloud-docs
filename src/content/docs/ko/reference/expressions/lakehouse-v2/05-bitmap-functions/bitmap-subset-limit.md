---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — 오프셋에서 시작하여 카디널리티 제한만큼의 비트맵 부분집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

오프셋에서 시작하여 카디널리티 제한만큼의 비트맵 부분집합을 반환합니다.

## Analyze 구문

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Analyze 예제

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
