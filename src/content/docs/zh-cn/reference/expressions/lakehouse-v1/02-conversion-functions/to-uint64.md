---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64：将值转换为 UINT64 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

将值转换为 UINT64 数据类型。

## Analyze 语法

```python
func.to_uint64( <expr> )
```

## Analyze 示例

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQL 语法

```sql
TO_UINT64( <expr> )
```

## SQL 示例

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
