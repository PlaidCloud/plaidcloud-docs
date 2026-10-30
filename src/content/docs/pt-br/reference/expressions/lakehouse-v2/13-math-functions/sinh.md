---
title: SINH (Lakehouse v2)
description: SINH — retorna o seno hiperbólico de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

Retorna o seno hiperbólico de um número.

## Sintaxe do Analyze

```python
func.sinh(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
