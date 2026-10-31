---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — 고유한 정수 값의 개수를 반환합니다(집계).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

고유한 정수 값의 개수를 반환합니다(집계).

## Analyze 구문

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Analyze 예제

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## SQL 구문

```sql
BITMAP_UNION_INT(<id>)
```

## SQL 예제

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
