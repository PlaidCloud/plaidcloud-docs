---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — 指定した日付が属する月の最終日を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

指定した日付が属する月の最終日を返します。

## Analyzeの構文

```python
func.last_day(<date>[, <unit>])
```

## Analyzeの例

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQLの構文

```sql
LAST_DAY(<date>[, <unit>])
```

## SQLの例

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
