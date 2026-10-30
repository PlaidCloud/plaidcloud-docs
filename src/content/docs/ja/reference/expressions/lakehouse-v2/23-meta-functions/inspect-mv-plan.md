---
title: INSPECT_MV_PLAN（Lakehouse v2）
description: INSPECT_MV_PLAN — マテリアライズドビューの論理プランを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

マテリアライズドビューの論理プランを返します。

## Analyze 構文

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Analyze の例

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## SQL 構文

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## SQL の例

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
