---
title: TO_DAY_OF_MONTH（Lakehouse v1）
description: TO_DAY_OF_MONTH — 日付または日時（タイムスタンプ/datetime）を UInt8 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

日付または日時（タイムスタンプ/datetime）を、月内の日番号（1～31）を表す UInt8 の数値に変換します。

## Analyze 構文

```python
func.to_day_of_month(<expr>)
```

## Analyze の例

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_DAY_OF_MONTH(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## エイリアス

- [DAY](../day)

## 戻り値の型

`TINYINT`

## SQL の例

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
