---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 ENCODE_SORT_KEY 实用函数。将值编码为保持排序顺序的二进制排序键，适用于复合排序键。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

将值编码为保持排序顺序的二进制排序键，适用于复合排序键。

## Analyze 语法

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Analyze 示例

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## SQL 语法

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## SQL 示例

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
