---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND — acrescenta um elemento no início da matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

Acrescenta um elemento no início da matriz.

## Sintaxe do Analyze

```python
func.array_prepend( <element>, <array> )
```

## Exemplos do Analyze

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_PREPEND( <element>, <array> )
```

## Exemplos SQL

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
