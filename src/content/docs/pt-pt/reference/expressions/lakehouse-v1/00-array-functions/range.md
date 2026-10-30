---
title: RANGE (Lakehouse v1)
description: RANGE — devolve uma matriz recolhida pelo intervalo [start, end).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Devolve uma matriz recolhida pelo intervalo [start, end).

## Sintaxe do Analyze

```python
func.range( <start>, <end> )
```

## Exemplos do Analyze

```python
func.range(1, 5)

┌────────────────────┐
│  func.range(1, 5)  │
├────────────────────┤
│ [1,2,3,4]          │
└────────────────────┘
```

## Sintaxe SQL

```sql
RANGE( <start>, <end> )
```

## Exemplos SQL

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
