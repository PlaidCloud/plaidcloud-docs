---
title: TO_DAY_OF_WEEK（Lakehouse v1）
description: TO_DAY_OF_WEEK — 日付または日時（タイムスタンプ/datetime）を UInt8 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

日付または日時（タイムスタンプ/datetime）を、曜日の番号（月曜日が 1、日曜日が 7）を表す UInt8 の数値に変換します。

## Analyze 構文

```python
func.to_day_of_week(<expr>)
```

## Analyze の例

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_DAY_OF_WEEK(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## 戻り値の型

``TINYINT`

## SQL の例

```sql

SELECT
    to_day_of_week('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_week('2023-11-12 09:38:18.165575') │
│                     UInt8                    │
├──────────────────────────────────────────────┤
│                                            7 │
└──────────────────────────────────────────────┘
```
