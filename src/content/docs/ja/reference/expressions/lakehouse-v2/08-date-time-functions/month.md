---
title: MONTH (Lakehouse v2)
description: MONTH — 日付から月を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/month.md
---

日付から月を返します。

## Analyzeの構文

```python
func.month(<date>)
```

## Analyzeの例

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQLの構文

```sql
MONTH(<date>)
```

## SQLの例

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
