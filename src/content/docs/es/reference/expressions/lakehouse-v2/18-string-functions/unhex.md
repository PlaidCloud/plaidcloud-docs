---
title: UNHEX (Lakehouse v2)
description: UNHEX — Convierte una cadena hexadecimal en una cadena de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Convierte una cadena hexadecimal en una cadena de caracteres.

## Sintaxis de Analyze

```python
func.unhex(<hex_str>)
```

## Ejemplos de Analyze

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
UNHEX(<hex_str>)
```

## Ejemplos de SQL

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
