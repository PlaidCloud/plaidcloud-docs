---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN：返回物化视图的逻辑计划。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

返回物化视图的逻辑计划。

## Analyze 语法

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Analyze 示例

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## SQL 语法

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## SQL 示例

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
