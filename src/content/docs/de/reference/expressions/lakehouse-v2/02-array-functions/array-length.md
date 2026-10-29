---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH – gibt die Anzahl der Elemente eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

Gibt die Anzahl der Elemente eines Arrays zurück.

## Analyze-Syntax

```python
func.array_length([1, 2, 3])
```

## Analyze-Beispiele

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_LENGTH([1, 2, 3])
```

## SQL-Beispiele

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
