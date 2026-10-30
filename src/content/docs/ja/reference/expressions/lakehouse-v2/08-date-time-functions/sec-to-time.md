---
title: SEC_TO_TIME (Lakehouse v2)
description: SEC_TO_TIME — 秒数を時刻値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/sec-to-time.md
---

秒数を時刻値に変換します。

## Analyzeの構文

```python
func.sec_to_time(<seconds>)
```

## Analyzeの例

```python
func.sec_to_time(3661)

┌────────────┐
│ '01:01:01'  │
└────────────┘
```

## SQLの構文

```sql
SEC_TO_TIME(<seconds>)
```

## SQLの例

```sql
SELECT SEC_TO_TIME(3661);

┌──────────┐
│ 01:01:01  │
└──────────┘
```
