---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN – verkettet die Elemente eines Arrays mit einem Trennzeichen zu einer Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

Verkettet die Elemente eines Arrays mit einem Trennzeichen zu einer Zeichenfolge.

## Analyze-Syntax

```python
func.array_join([1,2,3], '-')
```

## Analyze-Beispiele

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_JOIN([1,2,3], '-')
```

## SQL-Beispiele

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
