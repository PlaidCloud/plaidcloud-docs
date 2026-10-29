---
title: YEAR (Lakehouse v2)
description: YEAR — 日付から年を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

日付から年を返します。

## Analyzeの構文

```python
func.year(<date>)
```

## Analyzeの例

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## SQLの構文

```sql
YEAR(<date>)
```

## SQLの例

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
