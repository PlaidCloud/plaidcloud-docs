---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32：将值转换为 FLOAT32 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

将值转换为 FLOAT32 数据类型。

## Analyze 语法

```python
func.to_float32( <expr> )
```

## Analyze 示例

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 语法

```sql
TO_FLOAT32( <expr> )
```

## SQL 示例

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
