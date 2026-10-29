---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — renvoie un score de similarité entre deux chaînes, fondé sur la correspondance de n-grammes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

Renvoie un score de similarité entre deux chaînes, fondé sur la correspondance de n-grammes.

## Syntaxe Analyze

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Exemples Analyze

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## Syntaxe SQL

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## Exemples SQL

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
