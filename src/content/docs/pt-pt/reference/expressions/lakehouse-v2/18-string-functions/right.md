---
title: RIGHT (Lakehouse v2)
description: RIGHT — devolve os N carateres mais à direita de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

Devolve os N carateres mais à direita de uma cadeia.

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

## Exemplos SQL

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
