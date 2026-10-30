---
title: H3_GET_RESOLUTION（Lakehouse v1）
description: H3_GET_RESOLUTION — 指定したH3インデックスの解像度を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-resolution.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスの解像度を返します。

## Analyze Syntax

```python
func.h3_get_resolution(h3)
```

## Analyze Examples

```python
func.h3_get_resolution(644325524701193974)

┌────────────────────────────────────────────┐
│ func.h3_get_resolution(644325524701193974) │
├────────────────────────────────────────────┤
│                                         15 │
└────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_GET_RESOLUTION(h3)
```

## SQL Examples

```sql
SELECT H3_GET_RESOLUTION(644325524701193974);

┌───────────────────────────────────────┐
│ h3_get_resolution(644325524701193974) │
├───────────────────────────────────────┤
│                                    15 │
└───────────────────────────────────────┘
```
