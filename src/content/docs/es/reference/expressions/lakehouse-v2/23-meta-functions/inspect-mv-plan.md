---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — Devuelve el plan lógico de una vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

Devuelve el plan lógico de una vista materializada.

## Sintaxis de Analyze

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Ejemplos de Analyze

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## Sintaxis de SQL

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## Ejemplos de SQL

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
