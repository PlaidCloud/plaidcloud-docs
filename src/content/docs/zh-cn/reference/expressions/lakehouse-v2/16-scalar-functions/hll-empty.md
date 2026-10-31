---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — 返回空的 HLL 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

返回空的 HLL 值。

## Analyze 语法

```python
func.hll_empty()
```

## Analyze 示例

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## SQL 语法

```sql
HLL_EMPTY()
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
