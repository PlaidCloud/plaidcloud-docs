---
title: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE（Lakehouse v1）
description: H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE — 始点と終点の六角形インデックスを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-indexes-from-unidirectional-edge.md
---

指定した単方向エッジのH3Indexから、始点と終点の六角形インデックスを返します。

## Analyze Syntax

```python
func.h3_get_indexes_from_unidirectional_edge(h3)
```

## Analyze Examples

```python
func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)

┌────────────────────────────────────────────────────────────────────┐
│ func.h3_get_indexes_from_unidirectional_edge(1248204388774707199)  │
├────────────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                            │
└────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(h3)
```

## SQL Examples

```sql
SELECT H3_GET_INDEXES_FROM_UNIDIRECTIONAL_EDGE(1248204388774707199);

┌──────────────────────────────────────────────────────────────┐
│ h3_get_indexes_from_unidirectional_edge(1248204388774707199) │
├──────────────────────────────────────────────────────────────┤
│ (599686042433355775,599686043507097599)                      │
└──────────────────────────────────────────────────────────────┘
```
