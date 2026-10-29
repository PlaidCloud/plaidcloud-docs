---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — n-gram 일치를 기준으로 두 문자열 간의 유사도 점수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

n-gram 일치를 기준으로 두 문자열 간의 유사도 점수를 반환합니다.

## Analyze 구문

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Analyze 예제

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## SQL 구문

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## SQL 예제

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
