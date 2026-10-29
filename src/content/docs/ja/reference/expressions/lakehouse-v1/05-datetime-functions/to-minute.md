---
title: TO_MINUTE（Lakehouse v1）
description: TO_MINUTE — 日時（タイムスタンプ/datetime）を、時間内の分（0～59）を表す UInt8 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

日時（タイムスタンプ/datetime）を、時間内の分（0～59）を表す UInt8 の数値に変換します。


## Analyze 構文

```python
func.to_minute(<expr>)
```

## Analyze の例

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_MINUTE(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr>`  | タイムスタンプ   |

## 戻り値の型

 `TINYINT`

## SQL の例

```sql
SELECT
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
