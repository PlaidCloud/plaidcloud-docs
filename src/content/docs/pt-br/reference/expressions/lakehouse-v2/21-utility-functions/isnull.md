---
title: ISNULL (Lakehouse v2)
description: ISNULL — Verifica se um valor é NULL. Retorna 1 se for NULL, 0 caso contrário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

Verifica se um valor é NULL. Retorna 1 se for NULL, 0 caso contrário.

## Sintaxe do Analyze

```python
func.isnull(<expr>)
```

## Exemplos do Analyze

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
ISNULL(<expr>)
```

## Exemplos de SQL

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
