---
title: TO_START_OF_FIVE_MINUTES（Lakehouse v1）
description: TO_START_OF_FIVE_MINUTES — 日時（タイムスタンプ/datetime）を 5 分間隔の開始時刻に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-five-minutes.md
---

日時（タイムスタンプ/datetime）を 5 分間隔の開始時刻に切り捨てます。

## Analyze 構文

```python
func.to_start_of_five_minutes(<expr>)
```

## Analyze の例

```python
func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')    │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_START_OF_FIVE_MINUTES(<expr>)
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
  to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────┐
│ to_start_of_five_minutes('2023-11-12 09:38:18.165575') │
│                        Timestamp                       │
├────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                    │
└────────────────────────────────────────────────────────┘
```
