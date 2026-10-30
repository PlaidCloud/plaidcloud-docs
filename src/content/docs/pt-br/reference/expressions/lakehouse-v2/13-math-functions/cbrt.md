---
title: CBRT (Lakehouse v2)
description: CBRT — retorna a raiz cúbica de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Retorna a raiz cúbica de um número.

## Sintaxe do Analyze

```python
func.cbrt(<x>)
```

## Exemplos do Analyze

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxe SQL

```sql
CBRT(<x>)
```

## Exemplos de SQL

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
