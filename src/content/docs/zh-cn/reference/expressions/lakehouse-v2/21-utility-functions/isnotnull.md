---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL：检查值是否不为 NULL。不为 NULL 时返回 1，否则返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

检查值是否不为 NULL。不为 NULL 时返回 1，否则返回 0。

## Analyze 语法

```python
func.isnotnull(<expr>)
```

## Analyze 示例

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
ISNOTNULL(<expr>)
```

## SQL 示例

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
