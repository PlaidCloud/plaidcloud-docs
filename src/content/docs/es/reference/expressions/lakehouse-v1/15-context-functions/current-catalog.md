---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG devuelve el nombre del catálogo que se está usando actualmente en la sesión.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Devuelve el nombre del catálogo que se está usando actualmente en la sesión.

## Sintaxis de SQL

```sql
CURRENT_CATALOG()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
