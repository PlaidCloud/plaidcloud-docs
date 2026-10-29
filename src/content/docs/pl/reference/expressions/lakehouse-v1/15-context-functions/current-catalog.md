---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG — zwraca nazwę katalogu używanego aktualnie w sesji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

Zwraca nazwę katalogu używanego aktualnie w sesji.

## Składnia SQL

```sql
CURRENT_CATALOG()
```

## Przykłady SQL

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
