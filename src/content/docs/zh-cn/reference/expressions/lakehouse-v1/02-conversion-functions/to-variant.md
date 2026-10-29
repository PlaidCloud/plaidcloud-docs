---
title: TO_VARIANT (Lakehouse v1)
description: TO_VARIANT：将值转换为 VARIANT 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-variant.md
---

将值转换为 VARIANT 数据类型。

## Analyze 语法

```python
func.to_variant( <expr> )
```

## Analyze 示例

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_VARIANT( <expr> )
```

## SQL 示例

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
