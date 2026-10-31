---
title: RTRIM (Lakehouse v2)
description: RTRIM — Elimina los espacios en blanco finales o los caracteres especificados de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

Elimina los espacios en blanco finales o los caracteres especificados de una cadena.

## Sintaxis de Analyze

```python
func.rtrim(<str>)
```

## Ejemplos de Analyze

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
RTRIM(<str>)
```

## Ejemplos de SQL

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
