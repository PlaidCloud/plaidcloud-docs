---
title: MICROSECONDS_SUB (Lakehouse v2)
description: MICROSECONDS_SUB — 日時から指定したマイクロ秒数を減算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-sub.md
---

日時から指定したマイクロ秒数を減算します。

## Analyzeの構文

```python
func.microseconds_sub(<datetime>, <n>)
```

## Analyzeの例

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## SQLの例

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
