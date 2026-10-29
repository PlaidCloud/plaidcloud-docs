---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP — 지정한 위치에서 시작하여 카디널리티 제한만큼의 하위 비트맵을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

지정한 위치에서 시작하여 카디널리티 제한만큼의 하위 비트맵을 반환합니다.

## Analyze 구문

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Analyze 예제

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 구문

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## SQL 예제

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
