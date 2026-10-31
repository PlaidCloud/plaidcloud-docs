---
title: MINUTES_SUB (Lakehouse v2)
description: MINUTES_SUB — 日時から指定した分数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-sub.md
---

日時から指定した分数を減算します。

## Analyzeの構文

```python
func.minutes_sub(<datetime>, <n>)
```

## Analyzeの例

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
MINUTES_SUB(<datetime>, <n>)
```

## SQLの例

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
