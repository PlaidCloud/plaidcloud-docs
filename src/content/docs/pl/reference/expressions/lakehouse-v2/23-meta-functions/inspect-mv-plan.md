---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — zwraca plan logiczny widoku zmaterializowanego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

Zwraca plan logiczny widoku zmaterializowanego.

## Składnia Analyze

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Przykłady Analyze

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## Składnia SQL

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## Przykłady SQL

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
