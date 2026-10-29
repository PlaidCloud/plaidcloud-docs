---
title: LTRIM (Lakehouse v2)
description: LTRIM — Elimina los espacios en blanco iniciales o los caracteres especificados de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

Elimina los espacios en blanco iniciales o los caracteres especificados de una cadena.

## Sintaxis de Analyze

```python
func.ltrim(<str>)
```

## Ejemplos de Analyze

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
LTRIM(<str>)
```

## Ejemplos de SQL

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
