---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG — renvoie le nom du catalogue actuellement utilisé pour la session.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Renvoie le nom du catalogue actuellement utilisé pour la session.

## Syntaxe SQL

```sql
CURRENT_CATALOG()
```

## Exemples SQL

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
