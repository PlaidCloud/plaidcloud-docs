---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST：将值从一种数据类型转换为另一种数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

将值从一种数据类型转换为另一种数据类型。出错时返回 NULL。

另请参阅：[CAST](../cast)

## Analyze 语法

```python
func.try_cast( <expr>, <data_type> )
```

## Analyze 示例

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## SQL 语法

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQL 示例

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
