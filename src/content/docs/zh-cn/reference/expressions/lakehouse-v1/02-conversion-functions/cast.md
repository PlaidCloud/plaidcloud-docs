---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, ::：将值从一种数据类型转换为另一种数据类型。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

将值从一种数据类型转换为另一种数据类型。`::` 是 CAST 的别名。

另请参阅：[TRY_CAST](../try-cast)

## Analyze 语法

```python
func.cast( <expr>, <data_type> )
```

## Analyze 示例

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## SQL 语法

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## SQL 示例

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
