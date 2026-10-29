---
title: HOURS_DIFF (Lakehouse v2)
description: HOURS_DIFF — 2 つの日時の間の時間数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-diff.md
---

2 つの日時の間の時間数を返します。

## Analyzeの構文

```python
func.hours_diff(<end>, <start>)
```

## Analyzeの例

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## SQLの構文

```sql
HOURS_DIFF(<end>, <start>)
```

## SQLの例

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
