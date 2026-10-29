---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32：将值转换为 INT32 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

将值转换为 INT32 数据类型。

## Analyze 语法

```python
func.to_int32( <expr> )
```

## Analyze 示例

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL 语法

```sql
TO_INT32( <expr> )
```

## SQL 示例

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
