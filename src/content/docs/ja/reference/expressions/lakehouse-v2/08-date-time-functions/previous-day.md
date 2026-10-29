---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — 指定した日付より前で、直近の指定曜日の日付を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

指定した日付より前で、直近の指定曜日の日付を返します。

## Analyzeの構文

```python
func.previous_day(<date>, <weekday>)
```

## Analyzeの例

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## SQLの構文

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## SQLの例

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
