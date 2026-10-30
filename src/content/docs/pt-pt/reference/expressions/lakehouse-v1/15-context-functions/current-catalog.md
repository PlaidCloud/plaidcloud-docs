---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG — devolve o nome do catálogo atualmente em utilização na sessão.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Devolve o nome do catálogo atualmente em utilização na sessão.

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
