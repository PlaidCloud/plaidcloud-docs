---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT — cria uma matriz com um elemento especificado repetido N vezes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

Cria uma matriz com um elemento especificado repetido N vezes.

## Sintaxe do Analyze

```python
func.array_repeat('x', 3)
```

## Exemplos do Analyze

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## Sintaxe SQL

```sql
ARRAY_REPEAT('x', 3)
```

## Exemplos SQL

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
