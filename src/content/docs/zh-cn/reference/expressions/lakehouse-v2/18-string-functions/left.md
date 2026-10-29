---
title: LEFT (Lakehouse v2)
description: LEFT：返回字符串最左侧的 N 个字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

返回字符串最左侧的 N 个字符。

## Analyze 语法

```python
func.left(<str>, <len>)
```

## Analyze 示例

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 语法

```sql
LEFT(<str>, <len>)
```

## SQL 示例

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
