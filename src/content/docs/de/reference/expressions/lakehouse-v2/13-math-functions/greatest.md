---
title: GREATEST (Lakehouse v2)
description: GREATEST – gibt den größten Wert aus einer Liste von Werten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

Gibt den größten Wert aus einer Liste von Werten zurück.

## Analyze-Syntax

```python
func.greatest(<val1>, <val2>[, ...])
```

## Analyze-Beispiele

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## SQL-Syntax

```sql
GREATEST(<val1>, <val2>[, ...])
```

## SQL-Beispiele

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
