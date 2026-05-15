---
title: NGRAM_SEARCH
description: NGRAM_SEARCH — returns a similarity score between two strings based on n-gram matching.
---

Returns a similarity score between two strings based on n-gram matching.

## Analyze Syntax

```python
func.ngram_search(<str1>, <str2>, <n>)
```

## Analyze Examples

```python
func.ngram_search('StarRocks', 'Starrocks', 4)

┌─────┐
│ 0.5  │
└─────┘
```

## SQL Syntax

```sql
NGRAM_SEARCH(<str1>, <str2>, <n>)
```

## SQL Examples

```sql
SELECT NGRAM_SEARCH('StarRocks', 'Starrocks', 4);

┌─────┐
│ 0.5  │
└─────┘
```
