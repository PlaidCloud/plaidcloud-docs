---
title: DAY (Lakehouse v2)
description: DAY — 日付から、月の何日目かを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/day.md
---

日付から、月の何日目かを返します。

## Analyzeの構文

```python
func.day(<date>)
```

## Analyzeの例

```python
func.day('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQLの構文

```sql
DAY(<date>)
```

## SQLの例

```sql
SELECT DAY('2024-06-15');

┌────┐
│ 15  │
└────┘
```
