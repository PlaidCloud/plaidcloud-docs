---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — 2つの日時の間の分数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-diff.md
---

2つの日時の間の分数を返します。

## Analyzeの構文

```python
func.minutes_diff(<end>, <start>)
```

## Analyzeの例

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## SQLの構文

```sql
MINUTES_DIFF(<end>, <start>)
```

## SQLの例

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
