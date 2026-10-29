---
title: CEILING (Lakehouse v2)
description: CEILING — retorna o menor inteiro maior ou igual a um número. Alias de `CEIL`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/ceiling.md
---

Retorna o menor inteiro maior ou igual a um número. Alias de `CEIL`.

## Sintaxe do Analyze

```python
func.ceiling(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
