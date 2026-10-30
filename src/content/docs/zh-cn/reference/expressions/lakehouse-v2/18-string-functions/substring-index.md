---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 SUBSTRING_INDEX 字符串函数。返回字符串中指定数量的分隔符出现之前或之后的子字符串。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

返回字符串中指定数量的分隔符出现之前或之后的子字符串。

## Analyze 语法

```python
func.substring_index(<str>, <delim>, <count>)
```

## Analyze 示例

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## SQL 语法

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## SQL 示例

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
