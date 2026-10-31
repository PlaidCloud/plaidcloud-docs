---
title: STRLEFT (Lakehouse v2)
description: STRLEFT：返回字符串最左侧的 N 个字符。是 `LEFT` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

返回字符串最左侧的 N 个字符。是 `LEFT` 的别名。

## Analyze 语法

```python
func.strleft(<str>, <len>)
```

## Analyze 示例

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 语法

```sql
STRLEFT(<str>, <len>)
```

## SQL 示例

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
