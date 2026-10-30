---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — 日時に指定した分数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minutes-add.md
---

日時に指定した分数を加算します。

## Analyzeの構文

```python
func.minutes_add(<datetime>, <n>)
```

## Analyzeの例

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
MINUTES_ADD(<datetime>, <n>)
```

## SQLの例

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
