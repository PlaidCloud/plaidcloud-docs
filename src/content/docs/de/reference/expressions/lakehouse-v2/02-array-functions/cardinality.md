---
title: "CARDINALITY (Array, Lakehouse v2)"
description: CARDINALITY – gibt die Anzahl der Elemente eines Arrays zurück. Alias für `ARRAY_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/cardinality.md
---

Gibt die Anzahl der Elemente eines Arrays zurück. Alias für `ARRAY_LENGTH`.

## Analyze-Syntax

```python
func.cardinality([1, 2, 3])
```

## Analyze-Beispiele

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
CARDINALITY([1, 2, 3])
```

## SQL-Beispiele

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
