---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH retorna o comprimento de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

Retorna o comprimento de um array.

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

## Exemplos de SQL

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
