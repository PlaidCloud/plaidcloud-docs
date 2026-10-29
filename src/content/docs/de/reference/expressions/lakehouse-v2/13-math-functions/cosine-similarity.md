---
title: COSINE_SIMILARITY (Lakehouse v2)
description: COSINE_SIMILARITY – gibt die Kosinus-Ähnlichkeit zwischen zwei Arrays (Vektoren) zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosine-similarity.md
---

Gibt die Kosinus-Ähnlichkeit zwischen zwei Arrays (Vektoren) zurück.

## Analyze-Syntax

```python
func.cosine_similarity(<array1>, <array2>)
```

## Analyze-Beispiele

```python
func.cosine_similarity([1.0, 2.0], [2.0, 4.0])

┌─────┐
│ 1.0  │
└─────┘
```

## SQL-Syntax

```sql
COSINE_SIMILARITY(<array1>, <array2>)
```

## SQL-Beispiele

```sql
SELECT COSINE_SIMILARITY([1.0, 2.0], [2.0, 4.0]);

┌─────┐
│ 1.0  │
└─────┘
```
