---
title: TIME_FORMAT (Lakehouse v2)
description: TIME_FORMAT — 書式文字列に従って時刻値を整形します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-format.md
---

書式文字列に従って時刻値を整形します。

## Analyzeの構文

```python
func.time_format(<time>, <format>)
```

## Analyzeの例

```python
func.time_format('14:30:00', '%H hours %i minutes')

┌───────────────────────┐
│ '14 hours 30 minutes'  │
└───────────────────────┘
```

## SQLの構文

```sql
TIME_FORMAT(<time>, <format>)
```

## SQLの例

```sql
SELECT TIME_FORMAT('14:30:00', '%H hours %i minutes');

┌─────────────────────┐
│ 14 hours 30 minutes  │
└─────────────────────┘
```
