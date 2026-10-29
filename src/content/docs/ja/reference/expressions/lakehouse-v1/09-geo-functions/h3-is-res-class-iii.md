---
title: H3_IS_RES_CLASS_III（Lakehouse v1）
description: H3_IS_RES_CLASS_III — 指定したH3インデックスの解像度がクラスIIIの向きかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

指定した[H3](https://eng.uber.com/h3/)インデックスの解像度がクラスIIIの向きかどうかを確認します。

## Analyze Syntax

```python
func.h3_is_res_class_iii(h3)
```

## Analyze Examples

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_IS_RES_CLASS_III(h3)
```

## SQL Examples

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
