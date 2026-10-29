---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — 根据数值计算百分位状态。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

根据数值计算百分位状态。

## Analyze 语法

```python
func.percentile_hash(<value>)
```

## Analyze 示例

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## SQL 语法

```sql
PERCENTILE_HASH(<value>)
```

## SQL 示例

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
