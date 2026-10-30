---
title: TANH (Lakehouse v2)
description: TANH — retorna a tangente hiperbólica de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

Retorna a tangente hiperbólica de um número.

## Sintaxe do Analyze

```python
func.tanh(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
