---
title: COSINE_SIMILARITY_NORM (Lakehouse v2)
description: COSINE_SIMILARITY_NORM – gibt die Kosinus-Ähnlichkeit zwischen zwei normalisierten Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity-norm.md
---

Gibt die Kosinus-Ähnlichkeit zwischen zwei normalisierten Arrays zurück.

## Analyze-Syntax

```python
func.cosine_similarity_norm(<array1>, <array2>)
```

## Analyze-Beispiele

```python
func.cosine_similarity_norm([0.6, 0.8], [0.8, 0.6])

┌──────┐
│ 0.96  │
└──────┘
```

## SQL-Syntax

```sql
COSINE_SIMILARITY_NORM(<array1>, <array2>)
```

## SQL-Beispiele

```sql
SELECT COSINE_SIMILARITY_NORM([0.6, 0.8], [0.8, 0.6]);

┌──────┐
│ 0.96  │
└──────┘
```
