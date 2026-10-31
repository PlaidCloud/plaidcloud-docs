---
title: SECONDS_ADD (Lakehouse v2)
description: SECONDS_ADD — 日時に指定した秒数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/seconds-add.md
---

日時に指定した秒数を加算します。

## Analyzeの構文

```python
func.seconds_add(<datetime>, <n>)
```

## Analyzeの例

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## SQLの構文

```sql
SECONDS_ADD(<datetime>, <n>)
```

## SQLの例

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
