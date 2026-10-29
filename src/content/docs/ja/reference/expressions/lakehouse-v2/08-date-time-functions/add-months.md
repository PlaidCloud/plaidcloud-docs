---
title: ADD_MONTHS (Lakehouse v2)
description: ADD_MONTHS — 日付に指定した月数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/add-months.md
---

日付に指定した月数を加算します。

## Analyzeの構文

```python
func.add_months(<date>, <months>)
```

## Analyzeの例

```python
func.add_months('2024-01-31', 1)

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQLの構文

```sql
ADD_MONTHS(<date>, <months>)
```

## SQLの例

```sql
SELECT ADD_MONTHS('2024-01-31', 1);

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
