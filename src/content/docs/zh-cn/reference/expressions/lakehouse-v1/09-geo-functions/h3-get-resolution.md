---
title: H3_GET_RESOLUTION（Lakehouse v1）
description: H3_GET_RESOLUTION — 返回给定 H3 索引的分辨率。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-resolution.md
---

返回给定 [H3](https://eng.uber.com/h3/) 索引的分辨率。

## Analyze 语法

```python
func.h3_get_resolution(h3)
```

## Analyze 示例

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_GET_RESOLUTION(h3)
```

## SQL 示例

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```
