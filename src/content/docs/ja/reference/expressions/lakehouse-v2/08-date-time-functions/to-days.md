---
title: TO_DAYS (Lakehouse v2)
description: TO_DAYS — 日付を日数に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-days.md
---

日付を日数に変換します。

## Analyzeの構文

```python
func.to_days(<date>)
```

## Analyzeの例

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQLの構文

```sql
TO_DAYS(<date>)
```

## SQLの例

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
