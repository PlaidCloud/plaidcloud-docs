---
title: TIME_SLOT（Lakehouse v1）
description: TIME_SLOT — 時刻を 30 分単位に丸めます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/time-slot.md
---

時刻を 30 分単位に丸めます。

## Analyze 構文

```python
func.time_slot(<expr>)
```

## Analyze の例

```python
func.time_slot('2023-11-12 09:38:18.165575')
┌───────────────────────────────-───-───-──────┐
│ func.time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                     │
├─────────────────────────────────-───-────────┤
│ 2023-11-12 09:30:00                          │
└─────────────────────────────────-───-────────┘
```

## SQL 構文

```sql
time_slot(<expr>)
```

## 引数

| 引数   | 説明 |
| ----------- | ----------- |
| `<expr>`    | タイムスタンプ   |

## 戻り値の型

`TIMESTAMP`。「YYYY-MM-DD hh:mm:ss.ffffff」形式で返されます。

## SQL の例

```sql
SELECT
  time_slot('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ time_slot('2023-11-12 09:38:18.165575') │
│                Timestamp                │
├─────────────────────────────────────────┤
│ 2023-11-12 09:30:00                     │
└─────────────────────────────────────────┘
```
