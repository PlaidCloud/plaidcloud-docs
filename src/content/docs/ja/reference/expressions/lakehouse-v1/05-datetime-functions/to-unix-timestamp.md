---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP — 日付/時刻形式のタイムスタンプを Unix タイムスタンプ形式に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

日付/時刻形式のタイムスタンプを Unix タイムスタンプ形式に変換します。Unix タイムスタンプは、1970年1月1日 00:00:00 UTC からの経過秒数を表します。

## Analyze の構文

```python
func.to_unix_timestamp(<expr>)
```

## Analyze の例

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## 引数

| 引数   | 説明         |
| ----------- | ------------------- |
| `<expr>`    | タイムスタンプ           |

タイムスタンプのデータ型の詳細については、「日付と時刻」を参照してください。

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
