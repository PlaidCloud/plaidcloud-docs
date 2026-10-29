---
title: HOURS_ADD (Lakehouse v2)
description: HOURS_ADD — 日時に指定した時間数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hours-add.md
---

日時に指定した時間数を加算します。

## Analyzeの構文

```python
func.hours_add(<datetime>, <n>)
```

## Analyzeの例

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
HOURS_ADD(<datetime>, <n>)
```

## SQLの例

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
