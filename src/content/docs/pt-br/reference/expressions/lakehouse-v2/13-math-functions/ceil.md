---
title: CEIL (Lakehouse v2)
description: CEIL — retorna o menor inteiro maior ou igual a um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceil.md
---

Retorna o menor inteiro maior ou igual a um número.

## Sintaxe do Analyze

```python
func.ceil(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
