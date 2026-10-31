---
title: TIME_SLICE (Lakehouse v2)
description: TIME_SLICE — 指定した時刻を、時間間隔の開始または終了に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-slice.md
---

指定した時刻を、時間間隔の開始または終了に変換します。

## Analyzeの構文

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyzeの例

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQLの例

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
