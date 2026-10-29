---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — acrescenta um elemento ao final de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

Acrescenta um elemento ao final de um array.

## Sintaxe do Analyze

```python
func.array_append([1, 2, 3], 4)
```

## Exemplos do Analyze

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Sintaxe SQL

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## Exemplos SQL

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
