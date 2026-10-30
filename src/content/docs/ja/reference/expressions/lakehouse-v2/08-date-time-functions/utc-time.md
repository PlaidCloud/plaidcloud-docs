---
title: UTC_TIME (Lakehouse v2)
description: UTC_TIME — 現在のUTC時刻を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/utc-time.md
---

現在のUTC時刻を返します。

## Analyzeの構文

```python
func.utc_time()
```

## Analyzeの例

```python
func.utc_time()

┌────────────┐
│ '18:30:00'  │
└────────────┘
```

## SQLの構文

```sql
UTC_TIME()
```

## SQLの例

```sql
SELECT UTC_TIME();

┌──────────┐
│ 18:30:00  │
└──────────┘
```
