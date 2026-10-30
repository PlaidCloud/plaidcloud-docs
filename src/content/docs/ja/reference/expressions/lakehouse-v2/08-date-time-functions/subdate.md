---
title: SUBDATE (Lakehouse v2)
description: SUBDATE — 日付から時間間隔を減算します。`DATE_SUB` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/subdate.md
---

日付から時間間隔を減算します。`DATE_SUB` のエイリアスです。

## Analyzeの構文

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Analyzeの例

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## SQLの構文

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## SQLの例

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
