---
title: SIN (Lakehouse v2)
description: SIN — devolve o seno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Devolve o seno de um número em radianos.

## Sintaxe de Analyze

```python
func.sin(<x>)
```

## Exemplos de Analyze

```python
func.sin(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxe SQL

```sql
SIN(<x>)
```

## Exemplos SQL

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
