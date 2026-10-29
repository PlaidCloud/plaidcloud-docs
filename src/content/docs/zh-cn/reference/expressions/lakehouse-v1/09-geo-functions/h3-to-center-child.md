---
title: H3_TO_CENTER_CHILD（Lakehouse v1）
description: H3_TO_CENTER_CHILD — 返回指定分辨率下的中心子索引。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

返回指定分辨率下的中心子索引。

## Analyze 语法

```python
func.h3_to_center_child(h3, res)
```

## Analyze 示例

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## SQL 示例

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
