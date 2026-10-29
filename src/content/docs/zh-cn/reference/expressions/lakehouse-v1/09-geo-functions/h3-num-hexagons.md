---
title: H3_NUM_HEXAGONS（Lakehouse v1）
description: H3_NUM_HEXAGONS — 返回给定分辨率下唯一 H3 索引的数量。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

返回给定分辨率下唯一 [H3](https://eng.uber.com/h3/) 索引的数量。

## Analyze 语法

```python
func.h3_num_hexagons(res)
```

## Analyze 示例

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## SQL 语法

```sql
H3_NUM_HEXAGONS(res)
```

## SQL 示例

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
