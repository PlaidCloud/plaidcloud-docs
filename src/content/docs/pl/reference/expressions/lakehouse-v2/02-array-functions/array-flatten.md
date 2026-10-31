---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — spłaszcza zagnieżdżone tablice do tablicy jednopoziomowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

Spłaszcza zagnieżdżone tablice do tablicy jednopoziomowej.

## Składnia Analyze

```python
func.array_flatten([[1,2],[3,4]])
```

## Przykłady Analyze

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Składnia SQL

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## Przykłady SQL

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
