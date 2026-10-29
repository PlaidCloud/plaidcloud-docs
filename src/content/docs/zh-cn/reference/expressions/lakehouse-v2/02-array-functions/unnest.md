---
title: UNNEST (Lakehouse v2)
description: UNNEST：将数组展开为一组行。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

将数组展开为一组行。

## Analyze 语法

```python
func.unnest([1, 2, 3])
```

## Analyze 示例

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## SQL 语法

```sql
UNNEST([1, 2, 3])
```

## SQL 示例

```sql
SELECT * FROM UNNEST([1, 2, 3]) AS t(val);

┌─────┐
│ val │
├─────┤
│   1 │
│   2 │
│   3 │
└─────┘
```
