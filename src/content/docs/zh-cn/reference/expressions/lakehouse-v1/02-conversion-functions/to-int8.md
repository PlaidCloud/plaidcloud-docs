---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8：将值转换为 INT8 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

将值转换为 INT8 数据类型。

## Analyze 语法

```python
func.to_int8( <expr> )
```

## Analyze 示例

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## SQL 语法

```sql
TO_INT8( <expr> )
```

## SQL 示例

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
