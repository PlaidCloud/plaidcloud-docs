---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — 返回用于初始化的空百分位状态。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

返回用于初始化的空百分位状态。

## Analyze 语法

```python
func.percentile_empty()
```

## Analyze 示例

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## SQL 语法

```sql
PERCENTILE_EMPTY()
```

## SQL 示例

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
