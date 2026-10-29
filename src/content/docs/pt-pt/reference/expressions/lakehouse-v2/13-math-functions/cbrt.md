---
title: CBRT (Lakehouse v2)
description: CBRT — devolve a raiz cúbica de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

Devolve a raiz cúbica de um número.

## Sintaxe de Analyze

```python
func.cbrt(<x>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
