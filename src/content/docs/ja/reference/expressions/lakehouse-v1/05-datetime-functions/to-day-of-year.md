---
title: TO_DAY_OF_YEAR（Lakehouse v1）
description: TO_DAY_OF_YEAR — 日付または日時（タイムスタンプ/datetime）を UInt16 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

日付または日時（タイムスタンプ/datetime）を、年内の日番号（1～366）を表す UInt16 の数値に変換します。

## Analyze 構文

```python
func.to_day_of_year(<expr>)
```

## Analyze の例

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_DAY_OF_YEAR(<expr>)
```

## 引数

| 引数   | 説明 |
| ----------- | ----------- |
| `<expr>` | 日付/タイムスタンプ |

## 戻り値の型

`SMALLINT`

## SQL の例

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
