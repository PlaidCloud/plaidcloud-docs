---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — Unix タイムスタンプを日時の文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Unix タイムスタンプを日時の文字列に変換します。

## Analyzeの構文

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Analyzeの例

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## SQLの例

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
