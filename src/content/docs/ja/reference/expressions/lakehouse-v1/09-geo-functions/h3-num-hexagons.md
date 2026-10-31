---
title: H3_NUM_HEXAGONS（Lakehouse v1）
description: H3_NUM_HEXAGONS — 指定した解像度での一意なH3インデックスの数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

指定した解像度での一意な[H3](https://eng.uber.com/h3/)インデックスの数を返します。

## Analyze Syntax

```python
func.h3_num_hexagons(res)
```

## Analyze Examples

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## SQL Syntax

```sql
H3_NUM_HEXAGONS(res)
```

## SQL Examples

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
