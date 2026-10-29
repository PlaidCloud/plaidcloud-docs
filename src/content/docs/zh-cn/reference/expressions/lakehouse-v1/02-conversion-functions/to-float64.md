---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64：将值转换为 FLOAT64 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

将值转换为 FLOAT64 数据类型。

## Analyze 语法

```python
func.to_float64( <expr> )
```

## Analyze 示例

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 语法

```sql
TO_FLOAT64( <expr> )
```

## SQL 示例

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
