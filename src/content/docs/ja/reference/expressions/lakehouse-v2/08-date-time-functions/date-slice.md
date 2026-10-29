---
title: DATE_SLICE (Lakehouse v2)
description: "PlaidCloud Lakehouse で DATE_SLICE 日付・時刻関数を使用します。指定した期間に基づいて、与えられた時刻を時間間隔の開始または終了に変換します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-slice.md
---

指定した期間に基づいて、与えられた時刻を時間間隔の開始または終了に変換します。

## Analyzeの構文

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyzeの例

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQLの例

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
