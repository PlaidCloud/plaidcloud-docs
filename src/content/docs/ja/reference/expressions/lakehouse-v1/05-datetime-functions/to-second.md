---
title: TO_SECOND（Lakehouse v1）
description: TO_SECOND — 日時（タイムスタンプ/datetime）を、分内の秒（0～59）を表す UInt8 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

日時（タイムスタンプ/datetime）を、分内の秒（0～59）を表す UInt8 の数値に変換します。

## Analyze 構文

```python
func.to_second(<expr>)
```

## Analyze の例

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_SECOND(<expr>)
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
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
