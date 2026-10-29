---
title: DATE_ADD (Lakehouse v2)
description: DATE_ADD — 日付または日時に指定した時間間隔を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-add.md
---

日付または日時に指定した時間間隔を加算します。

## Analyzeの構文

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Analyzeの例

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQLの構文

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## SQLの例

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
