---
title: DAYOFMONTH (Lakehouse v2)
description: DAYOFMONTH — 日付から、月の何日目かを返します。`DAY` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofmonth.md
---

日付から、月の何日目かを返します。`DAY` の別名です。

## Analyzeの構文

```python
func.dayofmonth(<date>)
```

## Analyzeの例

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQLの構文

```sql
DAYOFMONTH(<date>)
```

## SQLの例

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
