---
title: INSPECT_MV_PLAN (Lakehouse v2)
description: INSPECT_MV_PLAN — 구체화된 뷰의 논리 계획을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-plan.md
---

구체화된 뷰의 논리 계획을 반환합니다.

## Analyze 구문

```python
func.inspect_mv_plan(<db>, <mv>)
```

## Analyze 예제

```python
func.inspect_mv_plan('mydb', 'my_mv')

┌────────┐
│ (plan)  │
└────────┘
```

## SQL 구문

```sql
INSPECT_MV_PLAN(<db>, <mv>)
```

## SQL 예제

```sql
SELECT INSPECT_MV_PLAN('mydb', 'my_mv');

┌────────────────┐
│ (logical plan)  │
└────────────────┘
```
