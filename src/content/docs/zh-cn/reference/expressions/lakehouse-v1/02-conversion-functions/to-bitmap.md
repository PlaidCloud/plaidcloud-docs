---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP：将值转换为 BITMAP 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

将值转换为 BITMAP 数据类型。

## Analyze 语法

```python
func.to_bitmap( <expr> )
```

## Analyze 示例

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## SQL 语法

```sql
TO_BITMAP( <expr> )
```

## SQL 示例

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
