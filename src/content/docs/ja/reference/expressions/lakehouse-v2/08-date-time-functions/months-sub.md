---
title: MONTHS_SUB (Lakehouse v2)
description: MONTHS_SUB — 日付から指定した月数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-sub.md
---

日付から指定した月数を減算します。

## Analyzeの構文

```python
func.months_sub(<date>, <n>)
```

## Analyzeの例

```python
func.months_sub('2024-06-15', 3)

┌──────────────┐
│ '2024-03-15'  │
└──────────────┘
```

## SQLの構文

```sql
MONTHS_SUB(<date>, <n>)
```

## SQLの例

```sql
SELECT MONTHS_SUB('2024-06-15', 3);

┌────────────┐
│ 2024-03-15  │
└────────────┘
```
