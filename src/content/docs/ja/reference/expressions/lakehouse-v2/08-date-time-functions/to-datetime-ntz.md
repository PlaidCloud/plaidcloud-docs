---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — 値をタイムゾーンなし（NTZ）の DATETIME に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

値をタイムゾーンなし（NTZ）の DATETIME に変換します。結果はセッションのタイムゾーン設定の影響を受けません。

## Analyzeの構文

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Analyzeの例

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## SQLの構文

```sql
TO_DATETIME_NTZ(<expr>)
```

## SQLの例

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
