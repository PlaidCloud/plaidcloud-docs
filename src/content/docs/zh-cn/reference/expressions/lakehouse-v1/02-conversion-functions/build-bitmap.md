---
title: BUILD_BITMAP (Lakehouse v1)
description: BUILD_BITMAP：将正整数数组转换为 BITMAP 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/build-bitmap.md
---

将正整数数组转换为 BITMAP 值。


## Analyze 语法

```python
func.build_bitmap( <expr> )
```

## Analyze 示例

```python
func.to_string(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.to_string(func.build_bitmap([1, 4, 5]))  │
├───────────────────────────────────────────────┤
│ 1,4,5                                         │
└───────────────────────────────────────────────┘
```

## SQL 语法

```sql
BUILD_BITMAP( <expr> )
```

## SQL 示例

```sql
SELECT BUILD_BITMAP([1,4,5])::String;

┌─────────────────────────────────┐
│ build_bitmap([1, 4, 5])::string │
├─────────────────────────────────┤
│ 1,4,5                           │
└─────────────────────────────────┘
```
