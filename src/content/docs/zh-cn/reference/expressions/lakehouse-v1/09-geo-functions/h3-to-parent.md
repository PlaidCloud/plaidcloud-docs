---
title: H3_TO_PARENT（Lakehouse v1）
description: H3_TO_PARENT — 返回在分辨率 parent_res 下包含 h3 的父索引。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

返回在分辨率 `parent_res` 下包含 `h3` 的父索引。返回 0 表示发生了错误。

## Analyze 语法

```python
func.h3_to_parent(h3, parent_res)
```

## Analyze 示例

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## SQL 语法

```sql
H3_TO_PARENT(h3, parent_res)
```

## SQL 示例

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
