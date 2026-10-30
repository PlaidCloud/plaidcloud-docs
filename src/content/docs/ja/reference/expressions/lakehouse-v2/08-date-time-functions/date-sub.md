---
title: DATE_SUB (Lakehouse v2)
description: DATE_SUB — 日付または日時から指定した時間間隔を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-sub.md
---

日付または日時から指定した時間間隔を減算します。

## Analyzeの構文

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Analyzeの例

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## SQLの構文

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## SQLの例

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
