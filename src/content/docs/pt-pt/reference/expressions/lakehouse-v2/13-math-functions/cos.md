---
title: COS (Lakehouse v2)
description: COS — devolve o cosseno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Devolve o cosseno de um número em radianos.

## Sintaxe de Analyze

```python
func.cos(<x>)
```

## Exemplos de Analyze

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## Sintaxe SQL

```sql
COS(<x>)
```

## Exemplos SQL

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
