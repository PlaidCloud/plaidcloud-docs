---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE — Invierte una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Invierte una cadena.

## Sintaxis de Analyze

```python
func.reverse(<str>)
```

## Ejemplos de Analyze

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## Sintaxis de SQL

```sql
REVERSE(<str>)
```

## Ejemplos de SQL

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
