---
title: CEILING (Lakehouse v2)
description: CEILING — devolve o menor número inteiro maior ou igual a um número. Alias de `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Devolve o menor número inteiro maior ou igual a um número. Alias de `CEIL`.

## Sintaxe de Analyze

```python
func.ceiling(<x>)
```

## Exemplos de Analyze

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## Sintaxe SQL

```sql
CEILING(<x>)
```

## Exemplos SQL

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
