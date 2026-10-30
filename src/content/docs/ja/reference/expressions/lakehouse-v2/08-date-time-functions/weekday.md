---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — 日付に対する曜日のインデックスを返します（0=月曜日、6=日曜日）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

日付に対する曜日のインデックスを返します（0=月曜日、6=日曜日）。

## Analyzeの構文

```python
func.weekday(<date>)
```

## Analyzeの例

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## SQLの構文

```sql
WEEKDAY(<date>)
```

## SQLの例

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
