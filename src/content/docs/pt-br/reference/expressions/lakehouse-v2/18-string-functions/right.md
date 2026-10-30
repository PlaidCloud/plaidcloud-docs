---
title: RIGHT (Lakehouse v2)
description: RIGHT — retorna os N últimos caracteres (mais à direita) de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Retorna os N últimos caracteres (mais à direita) de uma string.

## Sintaxe do Analyze

```python
func.right(<str>, <len>)
```

## Exemplos do Analyze

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxe SQL

```sql
RIGHT(<str>, <len>)
```

## Exemplos de SQL

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
