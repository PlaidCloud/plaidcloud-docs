---
title: COSH (Lakehouse v2)
description: COSH — devolve o cosseno hiperbólico de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

Devolve o cosseno hiperbólico de um número.

## Sintaxe de Analyze

```python
func.cosh(<x>)
```

## Exemplos de Analyze

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxe SQL

```sql
COSH(<x>)
```

## Exemplos SQL

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
