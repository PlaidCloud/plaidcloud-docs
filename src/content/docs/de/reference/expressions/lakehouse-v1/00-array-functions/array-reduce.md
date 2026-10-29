---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE – wendet die Lambda-Funktion iterativ auf die Elemente des Arrays an, um das Array auf einen einzelnen Wert zu reduzieren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

Wendet die Lambda-Funktion iterativ auf die Elemente des Arrays an, um das Array auf einen einzelnen Wert zu reduzieren.

## Analyze-Syntax

```python
func.array_reduce( <array>, <lambda> )
```

## Analyze-Beispiele

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
