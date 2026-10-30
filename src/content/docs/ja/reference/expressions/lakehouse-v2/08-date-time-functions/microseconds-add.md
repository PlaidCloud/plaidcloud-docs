---
title: MICROSECONDS_ADD (Lakehouse v2)
description: MICROSECONDS_ADD — 日時に指定したマイクロ秒数を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/microseconds-add.md
---

日時に指定したマイクロ秒数を加算します。

## Analyzeの構文

```python
func.microseconds_add(<datetime>, <n>)
```

## Analyzeの例

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## SQLの構文

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## SQLの例

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
