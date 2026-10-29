---
title: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE（Lakehouse v1）
description: H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE — 从单向边 H3Index 返回目标六边形索引。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-destination-index-from-unidirectional-edge.md
---

从单向边 H3Index 返回目标六边形索引。

## Analyze 语法

```python
func.h3_get_destination_index_from_unidirectional_edge(h3)
```

## Analyze 示例

```python
func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199)

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                          599686043507097599 │
└─────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## SQL 示例

```sql
SELECT H3_GET_DESTINATION_INDEX_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌────────────────────────────────────────────────────────────────────────┐
│ h3_get_destination_index_from_unidirectional_edge(1248204388774707199) │
├────────────────────────────────────────────────────────────────────────┤
│                                                     599686043507097599 │
└────────────────────────────────────────────────────────────────────────┘
```
