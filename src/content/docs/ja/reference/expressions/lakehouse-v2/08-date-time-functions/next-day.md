---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — 指定した日付より後で、最初に迎える指定曜日の日付を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

指定した日付より後で、最初に迎える指定曜日の日付を返します。

## Analyzeの構文

```python
func.next_day(<date>, <weekday>)
```

## Analyzeの例

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## SQLの構文

```sql
NEXT_DAY(<date>, <weekday>)
```

## SQLの例

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
