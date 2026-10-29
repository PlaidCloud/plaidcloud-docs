---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — devolve uma subcadeia a partir de uma posição especificada, com um comprimento opcional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

Devolve uma subcadeia a partir de uma posição especificada, com um comprimento opcional.

## Sintaxe do Analyze

```python
func.substr(<str>, <pos>[, <len>])
```

## Exemplos do Analyze

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxe SQL

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## Exemplos SQL

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
