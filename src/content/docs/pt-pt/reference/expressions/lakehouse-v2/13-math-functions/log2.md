---
title: LOG2 (Lakehouse v2)
description: LOG2 — devolve o logaritmo de base 2 de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Devolve o logaritmo de base 2 de um número.

## Sintaxe de Analyze

```python
func.log2(<x>)
```

## Exemplos de Analyze

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxe SQL

```sql
LOG2(<x>)
```

## Exemplos SQL

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
