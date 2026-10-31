---
title: LOWER (Lakehouse v2)
description: LOWER — Convierte una cadena a minúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Convierte una cadena a minúsculas.

## Sintaxis de Analyze

```python
func.lower(<str>)
```

## Ejemplos de Analyze

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
LOWER(<str>)
```

## Ejemplos de SQL

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
