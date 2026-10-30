---
title: SECONDS_SUB (Lakehouse v2)
description: SECONDS_SUB — 日時から指定した秒数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-sub.md
---

日時から指定した秒数を減算します。

## Analyzeの構文

```python
func.seconds_sub(<datetime>, <n>)
```

## Analyzeの例

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
SECONDS_SUB(<datetime>, <n>)
```

## SQLの例

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
