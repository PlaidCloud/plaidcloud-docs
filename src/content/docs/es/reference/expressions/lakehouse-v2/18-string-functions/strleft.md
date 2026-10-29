---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — Devuelve los primeros N caracteres de una cadena, contando desde la izquierda. Alias de `LEFT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

Devuelve los primeros N caracteres de una cadena, contando desde la izquierda. Alias de `LEFT`.

## Sintaxis de Analyze

```python
func.strleft(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxis de SQL

```sql
STRLEFT(<str>, <len>)
```

## Ejemplos de SQL

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
