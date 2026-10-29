---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "PlaidCloud Lakehouseで日付/時刻関数 TO_TERA_TIMESTAMP を使用します。Teradataの書式文字列に従って、VARCHAR値をDATETIME値に変換します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Teradataの書式文字列に従って、VARCHAR値をDATETIME値に変換します。

## Analyzeの構文

```python
func.to_tera_timestamp(<str>, <format>)
```

## Analyzeの例

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## SQLの例

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
