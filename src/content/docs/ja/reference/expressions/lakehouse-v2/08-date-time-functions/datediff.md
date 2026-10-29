---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — 2 つの日付の間の日数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

2 つの日付の間の日数を返します。

## Analyzeの構文

```python
func.datediff(<end_date>, <start_date>)
```

## Analyzeの例

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQLの構文

```sql
DATEDIFF(<end_date>, <start_date>)
```

## SQLの例

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
