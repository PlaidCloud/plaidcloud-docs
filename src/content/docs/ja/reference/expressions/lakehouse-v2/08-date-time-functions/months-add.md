---
title: MONTHS_ADD (Lakehouse v2)
description: MONTHS_ADD — 日付に指定した月数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/months-add.md
---

日付に指定した月数を加算します。

## Analyzeの構文

```python
func.months_add(<date>, <n>)
```

## Analyzeの例

```python
func.months_add('2024-01-15', 3)

┌──────────────┐
│ '2024-04-15'  │
└──────────────┘
```

## SQLの構文

```sql
MONTHS_ADD(<date>, <n>)
```

## SQLの例

```sql
SELECT MONTHS_ADD('2024-01-15', 3);

┌────────────┐
│ 2024-04-15  │
└────────────┘
```
