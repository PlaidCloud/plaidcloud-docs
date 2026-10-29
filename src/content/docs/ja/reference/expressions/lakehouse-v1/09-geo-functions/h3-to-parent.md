---
title: H3_TO_PARENT（Lakehouse v1）
description: H3_TO_PARENT — 解像度parent_resで、h3を含む親インデックスを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

解像度`parent_res`で、`h3`を含む親インデックスを返します。0が返された場合は、エラーが発生したことを示します。

## Analyze Syntax

```python
func.h3_to_parent(h3, parent_res)
```

## Analyze Examples

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## SQL Syntax

```sql
H3_TO_PARENT(h3, parent_res)
```

## SQL Examples

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
