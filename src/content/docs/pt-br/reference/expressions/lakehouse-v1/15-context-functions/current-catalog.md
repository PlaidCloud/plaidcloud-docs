---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG — retorna o nome do catálogo em uso na sessão.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Retorna o nome do catálogo em uso na sessão.

## Sintaxe SQL

```sql
CURRENT_CATALOG()
```

## Exemplos de SQL

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
