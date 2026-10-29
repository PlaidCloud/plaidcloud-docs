---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO — 日付に対する年内のISO週番号を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

日付に対する年内のISO週番号を返します。

## Analyzeの構文

```python
func.week_iso(<date>)
```

## Analyzeの例

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQLの構文

```sql
WEEK_ISO(<date>)
```

## SQLの例

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
