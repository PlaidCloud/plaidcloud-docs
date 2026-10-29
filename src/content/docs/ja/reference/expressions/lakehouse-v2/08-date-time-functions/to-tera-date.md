---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — Teradataの書式文字列に従って、VARCHAR値をDATE値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Teradataの書式文字列に従って、VARCHAR値をDATE値に変換します。

## Analyzeの構文

```python
func.to_tera_date(<str>, <format>)
```

## Analyzeの例

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
TO_TERA_DATE(<str>, <format>)
```

## SQLの例

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
