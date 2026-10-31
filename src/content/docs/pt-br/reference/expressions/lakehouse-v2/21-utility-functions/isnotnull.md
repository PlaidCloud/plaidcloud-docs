---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — verifica se um valor não é NULL. Retorna 1 se não for NULL, 0 caso contrário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

Verifica se um valor não é NULL. Retorna 1 se não for NULL, 0 caso contrário.

## Sintaxe do Analyze

```python
func.isnotnull(<expr>)
```

## Exemplos do Analyze

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
ISNOTNULL(<expr>)
```

## Exemplos de SQL

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
