---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16：将值转换为 UINT16 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

将值转换为 UINT16 数据类型。

## Analyze 语法

```python
func.to_uint16( <expr> )
```

## Analyze 示例

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 语法

```sql
TO_UINT16( <expr> )
```

## SQL 示例

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
