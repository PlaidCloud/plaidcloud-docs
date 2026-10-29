---
title: YEARS_ADD (Lakehouse v2)
description: YEARS_ADD — 日付に指定した年数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/years-add.md
---

日付に指定した年数を加算します。

## Analyzeの構文

```python
func.years_add(<date>, <n>)
```

## Analyzeの例

```python
func.years_add('2024-01-01', 5)

┌──────────────┐
│ '2029-01-01'  │
└──────────────┘
```

## SQLの構文

```sql
YEARS_ADD(<date>, <n>)
```

## SQLの例

```sql
SELECT YEARS_ADD('2024-01-01', 5);

┌────────────┐
│ 2029-01-01  │
└────────────┘
```
