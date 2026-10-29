---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — 日付または日時の値を、指定した精度に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

日付または日時の値を、指定した精度に切り捨てます。

## Analyzeの構文

```python
func.date_trunc(<unit>, <datetime>)
```

## Analyzeの例

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## SQLの構文

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## SQLの例

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
