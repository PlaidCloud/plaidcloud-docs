---
title: MONTHNAME (Lakehouse v2)
description: MONTHNAME — 日付の月名を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/monthname.md
---

日付の月名を返します。

## Analyzeの構文

```python
func.monthname(<date>)
```

## Analyzeの例

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## SQLの構文

```sql
MONTHNAME(<date>)
```

## SQLの例

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
