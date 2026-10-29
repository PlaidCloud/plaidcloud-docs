---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — Retorna o plano lógico de uma visão materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

Retorna o plano lógico de uma visão materializada.

## Sintaxe do Analyze

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Exemplos do Analyze

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## Sintaxe SQL

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## Exemplos de SQL

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
