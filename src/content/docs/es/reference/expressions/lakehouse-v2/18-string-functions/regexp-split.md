---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — Divide una cadena según un patrón de expresión regular y devuelve una matriz de subcadenas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

Divide una cadena según un patrón de expresión regular y devuelve una matriz de subcadenas.

## Sintaxis de Analyze

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Ejemplos de Analyze

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## Sintaxis de SQL

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## Ejemplos de SQL

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
