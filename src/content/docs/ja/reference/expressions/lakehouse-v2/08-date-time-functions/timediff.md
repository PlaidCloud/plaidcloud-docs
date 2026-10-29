---
title: TIMEDIFF (Lakehouse v2)
description: TIMEDIFF — 2つの時刻値の差を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timediff.md
---

2つの時刻値の差を返します。

## Analyzeの構文

```python
func.timediff(<time1>, <time2>)
```

## Analyzeの例

```python
func.timediff('15:30:00', '10:00:00')

┌────────────┐
│ '05:30:00'  │
└────────────┘
```

## SQLの構文

```sql
TIMEDIFF(<time1>, <time2>)
```

## SQLの例

```sql
SELECT TIMEDIFF('15:30:00', '10:00:00');

┌──────────┐
│ 05:30:00  │
└──────────┘
```
