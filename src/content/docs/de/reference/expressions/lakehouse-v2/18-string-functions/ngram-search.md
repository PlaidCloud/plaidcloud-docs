---
title: NGRAM_SEARCH (Lakehouse v2)
description: NGRAM_SEARCH — gibt auf Basis eines N-Gramm-Abgleichs einen Ähnlichkeitswert für zwei Zeichenfolgen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ngram-search.md
---

Gibt auf Basis eines N-Gramm-Abgleichs einen Ähnlichkeitswert für zwei Zeichenfolgen zurück.

## Analyze-Syntax

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Analyze-Beispiele

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## SQL-Syntax

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## SQL-Beispiele

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
