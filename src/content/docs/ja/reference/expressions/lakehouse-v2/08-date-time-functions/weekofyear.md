---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — 日付に対する年内の週を返します。`WEEK` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekofyear.md
---

日付に対する年内の週を返します。`WEEK` のエイリアスです。

## Analyzeの構文

```python
func.weekofyear(<date>)
```

## Analyzeの例

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQLの構文

```sql
WEEKOFYEAR(<date>)
```

## SQLの例

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
