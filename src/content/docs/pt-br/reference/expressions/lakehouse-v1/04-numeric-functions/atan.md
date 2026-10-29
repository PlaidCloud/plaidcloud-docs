---
title: ATAN (Lakehouse v1)
description: ATAN — retorna o arco tangente de x, ou seja, o valor cuja tangente é x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

Retorna o arco tangente de `x`, ou seja, o valor cuja tangente é `x`.

## Sintaxe do Analyze

```python
func.atan( <x> )
```

## Exemplos do Analyze

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
ATAN( <x> )
```

## Exemplos de SQL

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
