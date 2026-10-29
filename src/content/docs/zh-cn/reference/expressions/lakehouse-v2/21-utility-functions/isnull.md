---
title: ISNULL (Lakehouse v2)
description: ISNULL：检查值是否为 NULL。为 NULL 时返回 1，否则返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

检查值是否为 NULL。为 NULL 时返回 1，否则返回 0。

## Analyze 语法

```python
func.isnull(<expr>)
```

## Analyze 示例

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
ISNULL(<expr>)
```

## SQL 示例

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
