---
title: LCASE (Lakehouse v2)
description: LCASE — Convierte una cadena a minúsculas. Alias de `LOWER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

Convierte una cadena a minúsculas. Alias de `LOWER`.

## Sintaxis de Analyze

```python
func.lcase(<str>)
```

## Ejemplos de Analyze

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
LCASE(<str>)
```

## Ejemplos de SQL

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
