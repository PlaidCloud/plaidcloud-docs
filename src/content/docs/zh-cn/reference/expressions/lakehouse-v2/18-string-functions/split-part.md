---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART：按分隔符拆分字符串，并返回指定索引处的元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

按分隔符拆分字符串，并返回指定索引处的元素。

## Analyze 语法

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Analyze 示例

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## SQL 语法

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## SQL 示例

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
