---
title: WEEKS_SUB (Lakehouse v2)
description: WEEKS_SUB — 日付から指定した週数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weeks-sub.md
---

日付から指定した週数を減算します。

## Analyzeの構文

```python
func.weeks_sub(<date>, <n>)
```

## Analyzeの例

```python
func.weeks_sub('2024-01-15', 2)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQLの構文

```sql
WEEKS_SUB(<date>, <n>)
```

## SQLの例

```sql
SELECT WEEKS_SUB('2024-01-15', 2);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
