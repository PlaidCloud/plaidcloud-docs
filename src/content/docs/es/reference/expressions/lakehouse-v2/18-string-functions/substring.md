---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — Devuelve una subcadena a partir de una posición especificada. Alias de `SUBSTR`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

Devuelve una subcadena a partir de una posición especificada. Alias de `SUBSTR`.

## Sintaxis de Analyze

```python
func.substring(<str>, <pos>[, <len>])
```

## Ejemplos de Analyze

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxis de SQL

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## Ejemplos de SQL

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
