---
title: DAYOFWEEK (Lakehouse v2)
description: DAYOFWEEK — 日付の曜日インデックスを返します（1 = 日曜日、7 = 土曜日）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofweek.md
---

日付の曜日インデックスを返します（1 = 日曜日、7 = 土曜日）。

## Analyzeの構文

```python
func.dayofweek(<date>)
```

## Analyzeの例

```python
func.dayofweek('2024-06-15')

┌───┐
│ 7  │
└───┘
```

## SQLの構文

```sql
DAYOFWEEK(<date>)
```

## SQLの例

```sql
SELECT DAYOFWEEK('2024-06-15');

┌───┐
│ 7  │
└───┘
```
