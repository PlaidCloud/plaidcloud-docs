---
title: H3_EXACT_EDGE_LENGTH_RADS（Lakehouse v1）
description: H3_EXACT_EDGE_LENGTH_RADS — 计算此有向边的长度，单位为弧度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-exact-edge-length-rads.md
---

计算此有向边的长度，单位为弧度。

## Analyze 语法

```python
func.h3_exact_edge_length_km(h3)
```

## Analyze 示例

```python
func.h3_exact_edge_length_km(1319695429381652479)

┌───────────────────────────────────────────────────┐
│ func.h3_exact_edge_length_km(1319695429381652479) │
├───────────────────────────────────────────────────┤
│                                 8.267326832647143 │
└───────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_EXACT_EDGE_LENGTH_RADS(h3)
```

## SQL 示例

```sql
SELECT H3_EXACT_EDGE_LENGTH_KM(1319695429381652479);

┌──────────────────────────────────────────────┐
│ h3_exact_edge_length_km(1319695429381652479) │
├──────────────────────────────────────────────┤
│                            8.267326832647143 │
└──────────────────────────────────────────────┘
```
