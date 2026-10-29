---
title: H3_GET_UNIDIRECTIONAL_EDGE（Lakehouse v1）
description: H3_GET_UNIDIRECTIONAL_EDGE — 返回两个给定 H3 索引之间的边。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-unidirectional-edge.md
---

返回两个给定 [H3](https://eng.uber.com/h3/) 索引之间的边。

## Analyze 语法

```python
func.h3_get_unidirectional_edge(h3, a_h3)
```

## Analyze 示例

```python
func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754)

┌─────────────────────────────────────────────────────────────────────────┐
│ func.h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├─────────────────────────────────────────────────────────────────────────┤
│                                                     1581074247194257065 │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_UNIDIRECTIONAL_EDGE(h3, a_h3)
```

## SQL 示例

```sql
SELECT H3_GET_UNIDIRECTIONAL_EDGE(644325524701193897, 644325524701193754);

┌────────────────────────────────────────────────────────────────────┐
│ h3_get_unidirectional_edge(644325524701193897, 644325524701193754) │
├────────────────────────────────────────────────────────────────────┤
│                                                1581074247194257065 │
└────────────────────────────────────────────────────────────────────┘
```
