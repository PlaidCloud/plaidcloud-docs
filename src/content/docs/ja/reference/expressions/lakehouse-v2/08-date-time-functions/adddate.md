---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — 日付に指定した時間間隔を加算します。`DATE_ADD` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/adddate.md
---

日付に指定した時間間隔を加算します。`DATE_ADD` の別名です。

## Analyzeの構文

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Analyzeの例

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQLの構文

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## SQLの例

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
