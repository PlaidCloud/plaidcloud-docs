---
title: DAYOFWEEK_ISO (Lakehouse v2)
description: DAYOFWEEK_ISO — 日付の ISO 曜日インデックスを返します（1 = 月曜日、7 = 日曜日）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek-iso.md
---

日付の ISO 曜日インデックスを返します（1 = 月曜日、7 = 日曜日）。

## Analyzeの構文

```python
func.dayofweek_iso(<date>)
```

## Analyzeの例

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQLの構文

```sql
DAYOFWEEK_ISO(<date>)
```

## SQLの例

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
