---
title: H3_GET_BASE_CELL（Lakehouse v1）
description: H3_GET_BASE_CELL — 指定したH3インデックスのベースセル番号を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-base-cell.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスのベースセル番号を返します。

## Analyze Syntax

```python
func.h3_get_base_cell(h3)
```

## Analyze Examples

```python
func.h3_get_base_cell(644325524701193974)

┌───────────────────────────────────────────┐
│ func.h3_get_base_cell(644325524701193974) │
├───────────────────────────────────────────┤
│                                         8 │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_BASE_CELL(h3)
```

## SQL Examples

```sql
SELECT H3_GET_BASE_CELL(644325524701193974);

┌──────────────────────────────────────┐
│ h3_get_base_cell(644325524701193974) │
├──────────────────────────────────────┤
│                                    8 │
└──────────────────────────────────────┘
```
