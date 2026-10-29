---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT remove todos os duplicados e valores NULL do array sem preservar a ordem original.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

Remove todos os duplicados e valores NULL do array sem preservar a ordem original.

## Sintaxe do Analyze

```python
func.array_distinct( <array> )
```

## Exemplos do Analyze

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_DISTINCT( <array> )
```

## Exemplos de SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
