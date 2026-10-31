---
title: WEEK (Lakehouse v2)
description: WEEK — 日付に対する年内の週番号を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

日付に対する年内の週番号を返します。

## Analyzeの構文

```python
func.week(<date>[, <mode>])
```

## Analyzeの例

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQLの構文

```sql
WEEK(<date>[, <mode>])
```

## SQLの例

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
