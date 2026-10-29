---
title: VARIANT_QUERY（Lakehouse v2）
description: "PlaidCloud Lakehouse で VARIANT_QUERY バリアント関数を使用します。パス式を使って VARIANT オブジェクトから値をクエリし、VARIANT として返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

パス式を使って VARIANT オブジェクトから値をクエリし、VARIANT として返します。

## Analyze 構文

```python
func.variant_query(<variant>, <path>)
```

## Analyze の例

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## SQL 構文

```sql
VARIANT_QUERY(<variant>, <path>)
```

## SQL の例

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
