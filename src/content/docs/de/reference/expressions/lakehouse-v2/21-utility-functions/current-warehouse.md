---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — Gibt den Namen des aktuellen Warehouses zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

Gibt den Namen des aktuellen Warehouses zurück.

## Analyze-Syntax

```python
func.current_warehouse()
```

## Analyze-Beispiele

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## SQL-Syntax

```sql
CURRENT_WAREHOUSE()
```

## SQL-Beispiele

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
