---
title: LENGTH (Lakehouse v2)
description: LENGTH — Devuelve la longitud de una cadena en bytes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Devuelve la longitud de una cadena en bytes.

## Sintaxis de Analyze

```python
func.length(<str>)
```

## Ejemplos de Analyze

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## Sintaxis de SQL

```sql
LENGTH(<str>)
```

## Ejemplos de SQL

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
