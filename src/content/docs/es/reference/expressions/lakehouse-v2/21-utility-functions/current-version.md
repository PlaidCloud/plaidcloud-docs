---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — Devuelve la versión actual de StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

Devuelve la versión actual de StarRocks.

## Sintaxis de Analyze

```python
func.current_version()
```

## Ejemplos de Analyze

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## Sintaxis de SQL

```sql
CURRENT_VERSION()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
