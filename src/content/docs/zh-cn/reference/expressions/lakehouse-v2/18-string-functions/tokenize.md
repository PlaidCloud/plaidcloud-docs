---
title: TOKENIZE (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 TOKENIZE 字符串函数。使用指定的分析器将字符串分词为词项数组，适用于全文搜索。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

使用指定的分析器将字符串分词为词项数组，适用于全文搜索场景。

## Analyze 语法

```python
func.tokenize('The quick brown fox', 'english')
```

## Analyze 示例

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## SQL 语法

```sql
TOKENIZE(<str>[, <analyzer>])
```

## SQL 示例

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
