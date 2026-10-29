---
title: H3_IS_RES_CLASS_III（Lakehouse v1）
description: H3_IS_RES_CLASS_III — 检查给定 H3 索引的分辨率是否为 Class III 方向。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

检查给定 [H3](https://eng.uber.com/h3/) 索引的分辨率是否为 Class III 方向。

## Analyze 语法

```python
func.h3_is_res_class_iii(h3)
```

## Analyze 示例

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_IS_RES_CLASS_III(h3)
```

## SQL 示例

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
