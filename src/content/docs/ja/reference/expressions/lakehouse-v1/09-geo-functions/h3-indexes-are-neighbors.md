---
title: H3_INDEXES_ARE_NEIGHBORS（Lakehouse v1）
description: H3_INDEXES_ARE_NEIGHBORS — 指定したH3インデックスどうしが隣接しているかどうかを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-indexes-are-neighbors.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスどうしが隣接しているかどうかを返します。

## Analyze Syntax

```python
func.h3_indexes_are_neighbors(h3, a_h3)
```

## Analyze Examples

```python
func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897)

┌───────────────────────────────────────────────────────────────────────┐
│ func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├───────────────────────────────────────────────────────────────────────┤
│ true                                                                  │
└───────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_INDEXES_ARE_NEIGHBORS(h3, a_h3)
```

## SQL Examples

```sql
SELECT H3_INDEXES_ARE_NEIGHBORS(644325524701193974, 644325524701193897);

┌──────────────────────────────────────────────────────────────────┐
│ h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├──────────────────────────────────────────────────────────────────┤
│ true                                                             │
└──────────────────────────────────────────────────────────────────┘
```
