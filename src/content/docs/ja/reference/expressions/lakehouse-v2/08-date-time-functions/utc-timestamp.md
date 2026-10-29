---
title: UTC_TIMESTAMP (Lakehouse v2)
description: UTC_TIMESTAMP — 現在のUTCの日付と時刻を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-timestamp.md
---

現在のUTCの日付と時刻を返します。

## Analyzeの構文

```python
func.utc_timestamp()
```

## Analyzeの例

```python
func.utc_timestamp()

┌───────────────────────┐
│ '2024-06-15 18:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
UTC_TIMESTAMP()
```

## SQLの例

```sql
SELECT UTC_TIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 18:30:00  │
└─────────────────────┘
```
