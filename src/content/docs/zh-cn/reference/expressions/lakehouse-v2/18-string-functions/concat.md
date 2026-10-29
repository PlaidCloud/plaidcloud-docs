---
title: CONCAT (Lakehouse v2)
description: CONCAT：连接两个或多个字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

连接两个或多个字符串。

## Analyze 语法

```python
func.concat(<str1>, <str2>[, ...])
```

## Analyze 示例

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## SQL 语法

```sql
CONCAT(<str1>, <str2>[, ...])
```

## SQL 示例

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
