---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — 日付に対する年と週番号を整数で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

日付に対する年と週番号を整数で返します。

## Analyzeの構文

```python
func.yearweek(<date>[, <mode>])
```

## Analyzeの例

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## SQLの構文

```sql
YEARWEEK(<date>[, <mode>])
```

## SQLの例

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
