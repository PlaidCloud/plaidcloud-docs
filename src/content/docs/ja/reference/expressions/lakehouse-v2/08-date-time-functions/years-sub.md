---
title: YEARS_SUB (Lakehouse v2)
description: YEARS_SUB — 日付から指定した年数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-sub.md
---

日付から指定した年数を減算します。

## Analyzeの構文

```python
func.years_sub(<date>, <n>)
```

## Analyzeの例

```python
func.years_sub('2029-01-01', 5)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQLの構文

```sql
YEARS_SUB(<date>, <n>)
```

## SQLの例

```sql
SELECT YEARS_SUB('2029-01-01', 5);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
