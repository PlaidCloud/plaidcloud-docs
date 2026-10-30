---
title: CONVERT_TZ (Lakehouse v2)
description: CONVERT_TZ — 日時をあるタイムゾーンから別のタイムゾーンに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/convert-tz.md
---

日時をあるタイムゾーンから別のタイムゾーンに変換します。

## Analyzeの構文

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Analyzeの例

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## SQLの例

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
