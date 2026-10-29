---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8：将值转换为 UINT8 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

将值转换为 UINT8 数据类型。

## Analyze 语法

```python
func.to_uint8( <expr> )
```

## Analyze 示例

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL 语法

```sql
TO_UINT8( <expr> )
```

## SQL 示例

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
