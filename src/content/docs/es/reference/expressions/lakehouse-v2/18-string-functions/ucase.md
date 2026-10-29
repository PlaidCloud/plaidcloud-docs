---
title: UCASE (Lakehouse v2)
description: UCASE — Convierte una cadena a mayúsculas. Alias de `UPPER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

Convierte una cadena a mayúsculas. Alias de `UPPER`.

## Sintaxis de Analyze

```python
func.ucase(<str>)
```

## Ejemplos de Analyze

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Sintaxis de SQL

```sql
UCASE(<str>)
```

## Ejemplos de SQL

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
