---
title: VARIANT_QUERY (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 VARIANT_QUERY Variant 函数。使用路径表达式从 VARIANT 对象中查询值，并返回 VARIANT。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

使用路径表达式从 VARIANT 对象中查询值，并返回 VARIANT。

## Analyze 语法

```python
func.variant_query(<variant>, <path>)
```

## Analyze 示例

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## SQL 语法

```sql
VARIANT_QUERY(<variant>, <path>)
```

## SQL 示例

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
