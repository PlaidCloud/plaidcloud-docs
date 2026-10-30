---
title: TO_START_OF_HOUR（Lakehouse v1）
description: TO_START_OF_HOUR — 日時（タイムスタンプ/datetime）をその時間の開始時刻に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-hour.md
---

日時（タイムスタンプ/datetime）をその時間の開始時刻に切り捨てます。

## Analyze 構文

```python
func.to_start_of_hour(<expr>)
```

## Analyze の例

```python
func.to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_hour('2023-11-12 09:38:18.165575')            │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_START_OF_HOUR(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr>`  | タイムスタンプ   |

## 戻り値の型

`TIMESTAMP`。「YYYY-MM-DD hh:mm:ss.ffffff」形式の日付を返します。

## SQL の例

```sql
SELECT
  to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_hour('2023-11-12 09:38:18.165575') │
│                    Timestamp                   │
├────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                            │
└────────────────────────────────────────────────┘
```
