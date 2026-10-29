---
title: REPLACE (Lakehouse v2)
description: REPLACE — Reemplaza todas las apariciones de una subcadena por otra subcadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

Reemplaza todas las apariciones de una subcadena por otra subcadena.

## Sintaxis de Analyze

```python
func.replace(<str>, <old>, <new>)
```

## Ejemplos de Analyze

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
REPLACE(<str>, <old>, <new>)
```

## Ejemplos de SQL

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
