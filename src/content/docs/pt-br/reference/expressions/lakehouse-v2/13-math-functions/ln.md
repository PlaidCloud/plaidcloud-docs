---
title: LN (Lakehouse v2)
description: LN — retorna o logaritmo natural de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ln.md
---

Retorna o logaritmo natural de um número.

## Sintaxe do Analyze

```python
func.ln(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
