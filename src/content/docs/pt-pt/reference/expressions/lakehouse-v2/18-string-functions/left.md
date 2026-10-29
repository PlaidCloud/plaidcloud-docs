---
title: LEFT (Lakehouse v2)
description: LEFT — devolve os N carateres mais à esquerda de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

Devolve os N carateres mais à esquerda de uma cadeia.

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

## Exemplos SQL

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
