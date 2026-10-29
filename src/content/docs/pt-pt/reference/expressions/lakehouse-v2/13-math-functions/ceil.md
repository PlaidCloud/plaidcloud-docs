---
title: CEIL (Lakehouse v2)
description: CEIL — devolve o menor número inteiro maior ou igual a um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Devolve o menor número inteiro maior ou igual a um número.

## Sintaxe de Analyze

```python
func.ceil(<x>)
```

## Exemplos de Analyze

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## Sintaxe SQL

```sql
CEIL(<x>)
```

## Exemplos SQL

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
