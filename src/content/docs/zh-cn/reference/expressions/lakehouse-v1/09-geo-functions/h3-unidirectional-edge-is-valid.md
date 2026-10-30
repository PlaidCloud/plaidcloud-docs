---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID（Lakehouse v1）
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — 判断提供的 H3Index 是否为有效的单向边索引。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

判断提供的 H3Index 是否为有效的单向边索引。如果是单向边，则返回 1，否则返回 0。

## Analyze 语法

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Analyze 示例

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## SQL 示例

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
