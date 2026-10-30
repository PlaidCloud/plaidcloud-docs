---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — 计算值的 HLL 哈希。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

计算值的 HLL 哈希。

## Analyze 语法

```python
func.hll_hash(<expr>)
```

## Analyze 示例

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## SQL 语法

```sql
HLL_HASH(<expr>)
```

## SQL 示例

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
