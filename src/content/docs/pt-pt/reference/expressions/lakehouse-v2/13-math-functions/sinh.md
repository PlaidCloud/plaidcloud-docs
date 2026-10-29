---
title: SINH (Lakehouse v2)
description: SINH — devolve o seno hiperbólico de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Devolve o seno hiperbólico de um número.

## Sintaxe de Analyze

```python
func.sinh(<x>)
```

## Exemplos de Analyze

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxe SQL

```sql
SINH(<x>)
```

## Exemplos SQL

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
