---
title: SECONDS_DIFF (Lakehouse v2)
description: SECONDS_DIFF — 2つの日時の間の秒数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-diff.md
---

2つの日時の間の秒数を返します。

## Analyzeの構文

```python
func.seconds_diff(<end>, <start>)
```

## Analyzeの例

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## SQLの構文

```sql
SECONDS_DIFF(<end>, <start>)
```

## SQLの例

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
