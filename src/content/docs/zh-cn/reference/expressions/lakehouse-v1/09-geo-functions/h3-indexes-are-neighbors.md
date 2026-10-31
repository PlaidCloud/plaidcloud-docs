---
title: H3_INDEXES_ARE_NEIGHBORS（Lakehouse v1）
description: H3_INDEXES_ARE_NEIGHBORS — 返回提供的 H3 索引是否相邻。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-indexes-are-neighbors.md
---

返回提供的 [H3](https://eng.uber.com/h3/) 索引是否相邻。

## Analyze 语法

```python
func.h3_indexes_are_neighbors(h3, a_h3)
```

## Analyze 示例

```python
func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897)

┌───────────────────────────────────────────────────────────────────────┐
│ func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├───────────────────────────────────────────────────────────────────────┤
│ true                                                                  │
└───────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_INDEXES_ARE_NEIGHBORS(h3, a_h3)
```

## SQL 示例

```sql
SELECT H3_INDEXES_ARE_NEIGHBORS(644325524701193974, 644325524701193897);

┌──────────────────────────────────────────────────────────────────┐
│ h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├──────────────────────────────────────────────────────────────────┤
│ true                                                             │
└──────────────────────────────────────────────────────────────────┘
```
