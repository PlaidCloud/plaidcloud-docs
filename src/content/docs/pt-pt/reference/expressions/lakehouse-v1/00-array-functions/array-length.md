---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH — devolve o comprimento de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

Devolve o comprimento de uma matriz.

## Sintaxe do Analyze

```python
func.array_length( <array> )
```

## Exemplos do Analyze

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_LENGTH( <array> )
```

## Exemplos SQL

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
