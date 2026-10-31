---
title: SIN (Lakehouse v2)
description: SIN — retorna o seno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sin.md
---

Retorna o seno de um número em radianos.

## Sintaxe do Analyze

```python
func.sin(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT SIN(0);

┌─────┐
│ 0.0  │
└─────┘
```
