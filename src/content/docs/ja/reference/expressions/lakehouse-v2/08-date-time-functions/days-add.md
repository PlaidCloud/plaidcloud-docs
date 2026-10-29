---
title: DAYS_ADD (Lakehouse v2)
description: DAYS_ADD — 日付に指定した日数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/days-add.md
---

日付に指定した日数を加算します。

## Analyzeの構文

```python
func.days_add(<date>, <n>)
```

## Analyzeの例

```python
func.days_add('2024-01-01', 30)

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQLの構文

```sql
DAYS_ADD(<date>, <n>)
```

## SQLの例

```sql
SELECT DAYS_ADD('2024-01-01', 30);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
