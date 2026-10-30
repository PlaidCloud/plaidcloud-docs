---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — renvoie le plan logique d'une vue matérialisée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

Renvoie le plan logique d'une vue matérialisée.

## Syntaxe Analyze

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Exemples Analyze

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## Syntaxe SQL

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## Exemples SQL

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
