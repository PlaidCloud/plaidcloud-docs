---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — 2つの日付の間の週数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-diff.md
---

2つの日付の間の週数を返します。

## Analyzeの構文

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Analyzeの例

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## SQLの構文

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## SQLの例

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
