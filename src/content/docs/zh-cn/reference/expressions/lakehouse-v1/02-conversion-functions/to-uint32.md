---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32：将值转换为 UINT32 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

将值转换为 UINT32 数据类型。

## Analyze 语法

```python
func.to_uint32( <expr> )
```

## Analyze 示例

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 语法

```sql
TO_UINT32( <expr> )
```

## SQL 示例

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
