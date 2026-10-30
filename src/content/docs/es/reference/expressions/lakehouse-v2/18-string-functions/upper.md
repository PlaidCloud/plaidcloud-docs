---
title: UPPER (Lakehouse v2)
description: UPPER — Convierte una cadena a mayúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

Convierte una cadena a mayúsculas.

## Sintaxis de Analyze

```python
func.upper(<str>)
```

## Ejemplos de Analyze

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Sintaxis de SQL

```sql
UPPER(<str>)
```

## Ejemplos de SQL

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
