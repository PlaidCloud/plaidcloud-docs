---
title: TO_START_OF_MONTH（Lakehouse v1）
description: TO_START_OF_MONTH — 日付または日時（タイムスタンプ/datetime）をその月の初日に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

日付または日時（タイムスタンプ/datetime）をその月の初日に切り捨てます。
日付を返します。

## Analyze 構文

```python
func.to_start_of_month(<expr>)
```

## Analyze の例

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_START_OF_MONTH(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## 戻り値の型

`DATE`。「YYYY-MM-DD」形式の日付を返します。

## SQL の例

```sql
SELECT
  to_start_of_month('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_start_of_month('2023-11-12 09:38:18.165575') │
│                       Date                      │
├─────────────────────────────────────────────────┤
│ 2023-11-01                                      │
└─────────────────────────────────────────────────┘
```
