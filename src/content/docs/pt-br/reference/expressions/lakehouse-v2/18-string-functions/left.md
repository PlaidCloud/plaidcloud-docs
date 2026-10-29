---
title: LEFT (Lakehouse v2)
description: LEFT — retorna os N primeiros caracteres (mais à esquerda) de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Retorna os N primeiros caracteres (mais à esquerda) de uma string.

## Sintaxe do Analyze

```python
func.left(<str>, <len>)
```

## Exemplos do Analyze

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxe SQL

```sql
LEFT(<str>, <len>)
```

## Exemplos de SQL

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
