---
title: VERSION (Lakehouse v2)
description: VERSION — Devuelve la versión del protocolo MySQL de StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

Devuelve la versión del protocolo MySQL de StarRocks.

## Sintaxis de Analyze

```python
func.version()
```

## Ejemplos de Analyze

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## Sintaxis de SQL

```sql
VERSION()
```

## Ejemplos de SQL

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
