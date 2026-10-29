---
title: HOURS_SUB (Lakehouse v2)
description: HOURS_SUB — 日時から指定した時間数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-sub.md
---

日時から指定した時間数を減算します。

## Analyzeの構文

```python
func.hours_sub(<datetime>, <n>)
```

## Analyzeの例

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
HOURS_SUB(<datetime>, <n>)
```

## SQLの例

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
