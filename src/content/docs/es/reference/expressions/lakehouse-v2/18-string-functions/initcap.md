---
title: INITCAP (Lakehouse v2)
description: INITCAP — Convierte en mayúscula la primera letra de cada palabra de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Convierte en mayúscula la primera letra de cada palabra de una cadena.

## Sintaxis de Analyze

```python
func.initcap(<str>)
```

## Ejemplos de Analyze

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
INITCAP(<str>)
```

## Ejemplos de SQL

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
