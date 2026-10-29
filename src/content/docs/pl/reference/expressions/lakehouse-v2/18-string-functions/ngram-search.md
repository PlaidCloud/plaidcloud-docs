---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — zwraca wskaźnik podobieństwa dwóch ciągów na podstawie dopasowania n-gramów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

Zwraca wskaźnik podobieństwa dwóch ciągów na podstawie dopasowania n-gramów.

## Składnia Analyze

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Przykłady Analyze

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## Składnia SQL

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## Przykłady SQL

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
