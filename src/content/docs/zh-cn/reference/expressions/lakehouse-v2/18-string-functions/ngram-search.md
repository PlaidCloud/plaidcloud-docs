---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH：基于 n-gram 匹配返回两个字符串之间的相似度得分。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

基于 n-gram 匹配返回两个字符串之间的相似度得分。

## Analyze 语法

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Analyze 示例

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## SQL 语法

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## SQL 示例

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
