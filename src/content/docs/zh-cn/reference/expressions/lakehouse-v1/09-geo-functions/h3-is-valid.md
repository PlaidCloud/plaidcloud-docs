---
title: H3_IS_VALID（Lakehouse v1）
description: H3_IS_VALID — 检查给定 H3 索引是否有效。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

检查给定 [H3](https://eng.uber.com/h3/) 索引是否有效。

## Analyze 语法

```python
func.h3_is_valid(h3)
```

## Analyze 示例

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
H3_IS_VALID(h3)
```

## SQL 示例

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
