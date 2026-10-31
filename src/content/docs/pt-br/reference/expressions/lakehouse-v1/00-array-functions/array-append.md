---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND adiciona um elemento ao array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

Adiciona um elemento ao array.

## Sintaxe do Analyze

```python
func.array_append( <array>, <element>)
```

## Exemplos do Analyze

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_APPEND( <array>, <element>)
```

## Exemplos de SQL

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
