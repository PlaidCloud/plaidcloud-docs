---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — Gibt den logischen Plan einer materialisierten Ansicht zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

Gibt den logischen Plan einer materialisierten Ansicht zurück.

## Analyze-Syntax

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Analyze-Beispiele

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## SQL-Syntax

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## SQL-Beispiele

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
