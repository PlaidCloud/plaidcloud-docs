---
title: DATE_ADD（Lakehouse v1）
description: DATE_ADD — 指定した日付または日時に、時間間隔または日付間隔を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

指定した日付または日時（タイムスタンプ/datetime）に、時間間隔または日付間隔を加算します。

## Analyze 構文

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Analyze の例

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## 引数

| 引数             | 説明                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | 次のいずれかの値を指定する必要があります：`YEAR`、`QUARTER`、`MONTH`、`DAY`、`HOUR`、`MINUTE`、`SECOND`                 |
| `<value>`             | 加算する時間の単位の数です。たとえば 2 日を加算する場合は 2 になります。 |
| `<date_or_time_expr>` | `DATE` 型または `TIMESTAMP` 型の値                                                                             |

## 戻り値の型

この関数は、`<date_or_time_expr>` 引数と同じ型の値を返します。

## SQL の例

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
