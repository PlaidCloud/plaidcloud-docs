---
title: H3_TO_CENTER_CHILD（Lakehouse v1）
description: H3_TO_CENTER_CHILD — 指定した解像度での中心の子インデックスを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

指定した解像度での中心の子インデックスを返します。

## Analyze Syntax

```python
func.h3_to_center_child(h3, res)
```

## Analyze Examples

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## SQL Examples

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
