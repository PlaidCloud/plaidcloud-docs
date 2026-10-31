---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — 返回出现频率最高的前 k 个值及其近似计数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

返回出现频率最高的前 k 个值及其近似计数。

## Analyze 语法

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze 示例

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL 语法

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL 示例

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
