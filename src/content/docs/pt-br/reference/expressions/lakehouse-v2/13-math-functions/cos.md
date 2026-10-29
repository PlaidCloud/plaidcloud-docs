---
title: COS (Lakehouse v2)
description: COS — retorna o cosseno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

Retorna o cosseno de um número em radianos.

## Sintaxe do Analyze

```python
func.cos(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
