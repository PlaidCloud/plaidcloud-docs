---
title: VARIANT_TYPEOF（Lakehouse v2）
description: VARIANT_TYPEOF — VARIANT 値の型名を文字列として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

VARIANT 値の型名を文字列として返します。

## Analyze 構文

```python
func.variant_typeof(<variant>)
```

## Analyze の例

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## SQL 構文

```sql
VARIANT_TYPEOF(<variant>)
```

## SQL の例

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
