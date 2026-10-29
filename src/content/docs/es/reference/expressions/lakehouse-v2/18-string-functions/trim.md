---
title: TRIM (Lakehouse v2)
description: TRIM — Elimina los espacios en blanco iniciales y finales, o los caracteres especificados, de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

Elimina los espacios en blanco iniciales y finales, o los caracteres especificados, de una cadena.

## Sintaxis de Analyze

```python
func.trim(<str>)
```

## Ejemplos de Analyze

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
TRIM(<str>)
```

## Ejemplos de SQL

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
