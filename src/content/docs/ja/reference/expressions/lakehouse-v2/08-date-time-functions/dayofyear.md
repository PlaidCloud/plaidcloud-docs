---
title: DAYOFYEAR (Lakehouse v2)
description: DAYOFYEAR — 日付から、年の何日目かを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayofyear.md
---

日付から、年の何日目かを返します。

## Analyzeの構文

```python
func.dayofyear(<date>)
```

## Analyzeの例

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQLの構文

```sql
DAYOFYEAR(<date>)
```

## SQLの例

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
