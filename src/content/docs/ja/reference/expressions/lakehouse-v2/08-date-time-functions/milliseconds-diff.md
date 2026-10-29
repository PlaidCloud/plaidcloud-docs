---
title: MILLISECONDS_DIFF (Lakehouse v2)
description: MILLISECONDS_DIFF — 2つの日時の間のミリ秒数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/milliseconds-diff.md
---

2つの日時の間のミリ秒数を返します。

## Analyzeの構文

```python
func.milliseconds_diff(<end>, <start>)
```

## Analyzeの例

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## SQLの構文

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## SQLの例

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
