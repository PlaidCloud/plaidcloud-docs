---
title: QUARTER (Lakehouse v2)
description: QUARTER — 日付から年の四半期（1～4）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/quarter.md
---

日付から年の四半期（1～4）を返します。

## Analyzeの構文

```python
func.quarter(<date>)
```

## Analyzeの例

```python
func.quarter('2024-06-15')

┌───┐
│ 2  │
└───┘
```

## SQLの構文

```sql
QUARTER(<date>)
```

## SQLの例

```sql
SELECT QUARTER('2024-06-15');

┌───┐
│ 2  │
└───┘
```
