---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP：将位图展开为一组行。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

将位图展开为一组行。

## Analyze 语法

```python
func.unnest_bitmap(<bitmap>)
```

## Analyze 示例

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## SQL 语法

```sql
UNNEST_BITMAP(<bitmap>)
```

## SQL 示例

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
