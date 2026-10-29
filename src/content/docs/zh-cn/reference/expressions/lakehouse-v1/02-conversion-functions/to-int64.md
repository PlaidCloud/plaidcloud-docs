---
title: TO_INT64 (Lakehouse v1)
description: TO_INT64：将值转换为 INT64 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

将值转换为 INT64 数据类型。

## Analyze 语法

```python
func.to_int64( <expr> )
```

## Analyze 示例

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQL 语法

```sql
TO_INT64( <expr> )
```

## SQL 示例

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
