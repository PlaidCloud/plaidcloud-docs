---
title: FLOOR (Lakehouse v2)
description: FLOOR — retorna o maior inteiro menor ou igual a um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Retorna o maior inteiro menor ou igual a um número.

## Sintaxe do Analyze

```python
func.floor(<x>)
```

## Exemplos do Analyze

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## Sintaxe SQL

```sql
FLOOR(<x>)
```

## Exemplos de SQL

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
