---
title: DAYS_SUB (Lakehouse v2)
description: DAYS_SUB — 日付から指定した日数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-sub.md
---

日付から指定した日数を減算します。

## Analyzeの構文

```python
func.days_sub(<date>, <n>)
```

## Analyzeの例

```python
func.days_sub('2024-01-31', 30)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQLの構文

```sql
DAYS_SUB(<date>, <n>)
```

## SQLの例

```sql
SELECT DAYS_SUB('2024-01-31', 30);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
