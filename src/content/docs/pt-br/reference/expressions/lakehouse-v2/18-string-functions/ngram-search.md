---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — retorna uma pontuação de similaridade entre duas strings com base na correspondência de n-gramas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

Retorna uma pontuação de similaridade entre duas strings com base na correspondência de n-gramas.

## Sintaxe do Analyze

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Exemplos do Analyze

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## Sintaxe SQL

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## Exemplos de SQL

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
