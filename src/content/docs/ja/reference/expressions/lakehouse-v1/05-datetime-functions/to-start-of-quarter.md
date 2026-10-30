---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER — 日付または日時（timestamp/datetime）を、その四半期の初日に切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

日付または日時（timestamp/datetime）を、その四半期の初日に切り捨てます。
四半期の初日は、1月1日、4月1日、7月1日、10月1日のいずれかです。
結果として日付を返します。

## Analyze の構文

```python
func.to_start_of_quarter(<expr>)
```

## Analyze の例

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_START_OF_QUARTER(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`   | 日付/タイムスタンプ |

## 戻り値の型

`DATE`。「YYYY-MM-DD」形式の日付を返します。

## SQLの例

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
