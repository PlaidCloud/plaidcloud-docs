---
title: LOG10 (Lakehouse v2)
description: LOG10 — devolve o logaritmo de base 10 de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Devolve o logaritmo de base 10 de um número.

## Sintaxe de Analyze

```python
func.log10(<x>)
```

## Exemplos de Analyze

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxe SQL

```sql
LOG10(<x>)
```

## Exemplos SQL

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
