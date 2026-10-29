---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — devolve os N carateres mais à esquerda de uma cadeia. Alias de `LEFT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

Devolve os N carateres mais à esquerda de uma cadeia. Alias de `LEFT`.

## Sintaxe do Analyze

```python
func.strleft(<str>, <len>)
```

## Exemplos do Analyze

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxe SQL

```sql
STRLEFT(<str>, <len>)
```

## Exemplos SQL

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
