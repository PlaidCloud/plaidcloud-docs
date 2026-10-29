---
title: FLOOR (Lakehouse v2)
description: FLOOR — devolve o maior número inteiro menor ou igual a um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/floor.md
---

Devolve o maior número inteiro menor ou igual a um número.

## Sintaxe de Analyze

```python
func.floor(<x>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
