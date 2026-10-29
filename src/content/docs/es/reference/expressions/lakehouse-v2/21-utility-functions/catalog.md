---
title: CATALOG (Lakehouse v2)
description: CATALOG — Devuelve el nombre del catálogo actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

Devuelve el nombre del catálogo actual.

## Sintaxis de Analyze

```python
func.catalog()
```

## Ejemplos de Analyze

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## Sintaxis de SQL

```sql
CATALOG()
```

## Ejemplos de SQL

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
