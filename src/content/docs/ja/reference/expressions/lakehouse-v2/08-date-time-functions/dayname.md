---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — 日付に対応する曜日の名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

日付に対応する曜日の名前を返します。

## Analyzeの構文

```python
func.dayname(<date>)
```

## Analyzeの例

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## SQLの構文

```sql
DAYNAME(<date>)
```

## SQLの例

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
