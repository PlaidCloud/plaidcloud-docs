---
title: RANGE (Lakehouse v1)
description: RANGE retorna um array coletado no intervalo [start, end).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/range.md
---

Retorna um array coletado no intervalo [start, end).

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

## Exemplos de SQL

```sql
SELECT RANGE(1, 5);

┌───────────────┐
│  range(1, 5)  │
├───────────────┤
│ [1,2,3,4]     │
└───────────────┘
```
