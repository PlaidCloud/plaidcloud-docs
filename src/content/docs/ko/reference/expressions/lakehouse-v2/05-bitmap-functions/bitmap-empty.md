---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — 빈 비트맵을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

빈 비트맵을 반환합니다.

## Analyze 구문

```python
func.bitmap_empty()
```

## Analyze 예제

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## SQL 구문

```sql
BITMAP_EMPTY()
```

## SQL 예제

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
