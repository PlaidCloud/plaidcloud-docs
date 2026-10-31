---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — Comprueba si una cadena es NULL o está vacía. Devuelve 1 si es así y 0 en caso contrario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

Comprueba si una cadena es NULL o está vacía. Devuelve 1 si es así y 0 en caso contrario.

## Sintaxis de Analyze

```python
func.null_or_empty(<str>)
```

## Ejemplos de Analyze

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
NULL_OR_EMPTY(<str>)
```

## Ejemplos de SQL

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
