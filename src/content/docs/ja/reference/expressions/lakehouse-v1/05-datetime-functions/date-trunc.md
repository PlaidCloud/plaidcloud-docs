---
title: DATE_TRUNC（Lakehouse v1）
description: DATE_TRUNC — 日付、時刻、またはタイムスタンプの値を、指定した精度に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

日付、時刻、またはタイムスタンプの値を、指定した精度に切り捨てます。たとえば、`2022-07-07` を `MONTH` に切り捨てると結果は `2022-07-01` になり、`2022-07-07 01:01:01.123456` を `SECOND` に切り捨てると結果は `2022-07-07 01:01:01.000000` になります。

## Analyze 構文

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Analyze の例

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## 引数

| 引数             | 説明                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | 次のいずれかの値を指定する必要があります：`YEAR`、`QUARTER`、`MONTH`、`DAY`、`HOUR`、`MINUTE`、`SECOND`  |
| `<date_or_time_expr>` | `DATE` 型または `TIMESTAMP` 型の値                                                              |

## 戻り値の型

この関数は、`<date_or_time_expr>` 引数と同じ型の値を返します。

## SQL の例

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
