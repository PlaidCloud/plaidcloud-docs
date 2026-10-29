---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF：以字符串形式返回 VARIANT 值的类型名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

以字符串形式返回 VARIANT 值的类型名称。

## Analyze 语法

```python
func.variant_typeof(<variant>)
```

## Analyze 示例

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## SQL 语法

```sql
VARIANT_TYPEOF(<variant>)
```

## SQL 示例

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
