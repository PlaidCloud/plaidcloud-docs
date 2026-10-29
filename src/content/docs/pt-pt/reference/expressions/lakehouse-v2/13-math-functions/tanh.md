---
title: TANH (Lakehouse v2)
description: TANH — devolve a tangente hiperbólica de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Devolve a tangente hiperbólica de um número.

## Sintaxe de Analyze

```python
func.tanh(<x>)
```

## Exemplos de Analyze

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxe SQL

```sql
TANH(<x>)
```

## Exemplos SQL

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
