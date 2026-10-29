---
title: NGRAM_SEARCH（Lakehouse v2）
description: NGRAM_SEARCH — n-gramの一致に基づいて、2つの文字列の類似度スコアを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

n-gramの一致に基づいて、2つの文字列の類似度スコアを返します。

## Analyze 構文

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Analyze の例

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## SQL 構文

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## SQL の例

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
