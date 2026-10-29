---
title: LOG2 (Lakehouse v2)
description: LOG2 — retorna o logaritmo de base 2 de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

Retorna o logaritmo de base 2 de um número.

## Sintaxe do Analyze

```python
func.log2(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
