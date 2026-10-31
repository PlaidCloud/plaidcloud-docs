---
title: YEARS_DIFF (Lakehouse v2)
description: YEARS_DIFF — 2つの日付の間の年数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-diff.md
---

2つの日付の間の年数を返します。

## Analyzeの構文

```python
func.years_diff(<end_date>, <start_date>)
```

## Analyzeの例

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQLの構文

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## SQLの例

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
