---
title: H3_UNIDIRECTIONAL_EDGE_IS_VALID（Lakehouse v1）
description: H3_UNIDIRECTIONAL_EDGE_IS_VALID — 指定したH3Indexが有効な単方向エッジかどうかを判定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-unidirectional-edge-is-valid.md
---

指定したH3Indexが有効な単方向エッジのインデックスかどうかを判定します。単方向エッジの場合は1、それ以外の場合は0を返します。

## Analyze Syntax

```python
func.h3_unidirectional_edge_is_valid(h3)
```

## Analyze Examples

```python
func.h3_unidirectional_edge_is_valid(1248204388774707199)

┌───────────────────────────────────────────────────────────┐
│ func.h3_unidirectional_edge_is_valid(1248204388774707199) │
├───────────────────────────────────────────────────────────┤
│ true                                                      │
└───────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_UNIDIRECTIONAL_EDGE_IS_VALID(h3)
```

## SQL Examples

```sql
SELECT H3_UNIDIRECTIONAL_EDGE_IS_VALID(1248204388774707199);

┌──────────────────────────────────────────────────────┐
│ h3_unidirectional_edge_is_valid(1248204388774707199) │
├──────────────────────────────────────────────────────┤
│ true                                                 │
└──────────────────────────────────────────────────────┘
```
