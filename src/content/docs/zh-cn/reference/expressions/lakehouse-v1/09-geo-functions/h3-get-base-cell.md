---
title: H3_GET_BASE_CELL（Lakehouse v1）
description: H3_GET_BASE_CELL — 返回给定 H3 索引的基础单元编号。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

返回给定 [H3](https://eng.uber.com/h3/) 索引的基础单元编号。

## Analyze 语法

```python
func.h3_get_base_cell(h3)
```

## Analyze 示例

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_BASE_CELL(h3)
```

## SQL 示例

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
