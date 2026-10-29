---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — Devuelve una puntuación de similitud entre dos cadenas basada en la coincidencia de n-gramas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

Devuelve una puntuación de similitud entre dos cadenas basada en la coincidencia de n-gramas.

## Sintaxis de Analyze

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Ejemplos de Analyze

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## Sintaxis de SQL

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## Ejemplos de SQL

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
