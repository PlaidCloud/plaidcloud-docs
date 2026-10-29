---
title: LN (Lakehouse v2)
description: LN — devolve o logaritmo natural de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Devolve o logaritmo natural de um número.

## Sintaxe de Analyze

```python
func.ln(<x>)
```

## Exemplos de Analyze

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxe SQL

```sql
LN(<x>)
```

## Exemplos SQL

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
