---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG gibt den Namen des Katalogs zurück, der aktuell für die Sitzung verwendet wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Gibt den Namen des Katalogs zurück, der aktuell für die Sitzung verwendet wird.

## SQL-Syntax

```sql
CURRENT_CATALOG()
```

## SQL-Beispiele

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
