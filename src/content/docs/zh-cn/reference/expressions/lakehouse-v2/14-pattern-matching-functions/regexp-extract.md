---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — 提取第一个与正则表达式模式匹配的子字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

提取第一个与正则表达式模式匹配的子字符串。

## Analyze 语法

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Analyze 示例

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## SQL 语法

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## SQL 示例

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
